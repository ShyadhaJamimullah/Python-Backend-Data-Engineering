from sqlalchemy import Column,Integer,String
from database import Base

class Employee(Base):
    __tablename__="employees"
    EmployeeNumber=Column(Integer,primary_key=True,index=True)
    Age=Column(Integer,nullable=False)
    Gender=Column(String(10),nullable=False)
    Attrition=Column(String(10),nullable=False)
    Department=Column(String(50),nullable=False)
    MonthlyIncome=Column(Integer,nullable=False)
    PercentSalaryHike=Column(Integer,nullable=False)
    StockOptionLevel=Column(Integer,nullable=False)
    YearsAtCompany=Column(Integer,nullable=False)
    OverTime=Column(String(10),nullable=False)

    
