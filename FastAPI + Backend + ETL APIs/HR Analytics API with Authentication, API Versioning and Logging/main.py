from fastapi import FastAPI,UploadFile,File,Depends,Request,HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import func,Integer,case
import pandas as pd
import logging

from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse


from auth import create_access_token,verify_jwt,hashed_password,verify_password
from database import engine,sessionlocal
from schemas import LoginRequest
import schemas
import models
from models import Employee,User

logging.basicConfig(filename="api.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

app=FastAPI()


models.Base.metadata.create_all(bind=engine)
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/v1/auth/register")
def register(data: LoginRequest, db: Session = Depends(get_db)):
    hashed_pw=hashed_password(data.password)
    user=User(username=data.username,hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    return {"message":"User created"}

@app.post("/v1/auth/token")
def login(data:LoginRequest,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==data.username).first()
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    if not verify_password(data.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/protected")
def protected_route(payload: dict = Depends(verify_jwt)):
    return {
        "message": "Access granted",
        "user": payload["sub"]
    }


limiter=Limiter(key_func=get_remote_address)
app.state.limiter=limiter
app.add_middleware(SlowAPIMiddleware)
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc):
    return PlainTextResponse(
        "Too many requests. Please try again later.",
        status_code=429
    )



@app.middleware("http")
async def log_requests(request,call_next):
    logging.info(f"Request:{request.method}{request.url}")
    response=await call_next(request)
    logging.info(f"Response:{response.status_code}")
    return response



@app.post("/v1/etl/upload")
@limiter.limit("5/minute")
def upload_hr_csv(
    request: Request,
    file:UploadFile=File(...),
    db:Session=Depends(get_db),
    user:str=Depends(verify_jwt)):
  
    df=pd.read_csv(file.file)

    required_columns=[
        "EmployeeNumber",
        "Age",
        "Gender",
        "Attrition",
        "Department",
        "MonthlyIncome",
        "PercentSalaryHike",
        "StockOptionLevel",
        "YearsAtCompany",
        "OverTime"
    ]

    df=df[required_columns]

    #cleaning

    df=df.drop_duplicates(subset=["EmployeeNumber"])
    df=df.dropna()

    df["Gender"]=df["Gender"].str.lower()
    df["Attrition"]=df["Attrition"].str.lower()
    df["OverTime"]=df["OverTime"].str.lower()

    df=df[df["Age"] > 0]
    df=df[df["MonthlyIncome"] > 0]
    df=df[df["PercentSalaryHike"] >= 0]

    df=df.astype({
        "EmployeeNumber": int,
        "Age": int,
        "MonthlyIncome": int,
        "PercentSalaryHike": int,
        "StockOptionLevel": int,
        "YearsAtCompany": int
    })

    #transformation

    df["SalaryHikeCategory"]="Low"
    df.loc[df["PercentSalaryHike"]>=15,"SalaryHikeCategory"]="High"

    df_for_db=df.drop(columns=["SalaryHikeCategory"])

    
    records=df_for_db.to_dict(orient="records")

    existing_ids={
        emp[0] for emp in db.query(Employee.EmployeeNumber).all()
    }

    employees=[]

    for record in records:
        validated=schemas.EmployeeSchema(**record)

        if validated.EmployeeNumber in existing_ids:
            continue

        employees.append(
            Employee(**validated.model_dump())
        )

    if employees:
        db.add_all(employees)
        db.commit()

    #kpi
    total_employees=db.query(Employee).count()

    attrition_count=(
        db.query(Employee).filter(Employee.Attrition=="yes").count()
    )

    attrition_rate=round(
        (attrition_count/total_employees) * 100, 2
    ) if total_employees else 0

    gender_attrition=(
        db.query(
            Employee.Gender,
            func.avg(
                (Employee.Attrition=="yes").cast(Integer)
            ).label("rate")
        )
        .group_by(Employee.Gender)
        .all()
    )

    gender_kpi={
        gender:round(rate * 100, 2)
        for gender,rate in gender_attrition
    }

    overtime_attrition=(
        db.query(
            Employee.OverTime,
            func.avg(
                (Employee.Attrition=="yes").cast(Integer)
            ).label("rate")
        )
        .group_by(Employee.OverTime)
        .all()
    )

    overtime_kpi={
        ot: round(rate * 100, 2)
        for ot, rate in overtime_attrition
    }

    salary_hike_attrition=(
        db.query(
            case(
                (Employee.PercentSalaryHike>= 15,"High"),
                else_="Low"
            ).label("HikeCategory"),
            func.avg(
                (Employee.Attrition=="yes").cast(Integer)
            ).label("rate")
        )
        .group_by("HikeCategory")
        .all()
    )


    salary_hike_kpi={
        category:round(rate*100, 2)
        for category,rate in salary_hike_attrition
    }

    return {
        "inserted_records":len(employees),
        "total_employees":total_employees,
        "attrition_rate_percent":attrition_rate,
        "gender_wise_attrition_percent":gender_kpi,
        "overtime_attrition_percent":overtime_kpi,
        "salary_hike_attrition_percent":salary_hike_kpi
    }



