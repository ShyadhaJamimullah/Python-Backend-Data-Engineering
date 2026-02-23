from pydantic import BaseModel,ConfigDict

class EmployeeSchema(BaseModel):
    EmployeeNumber: int
    Age:int
    Gender:str
    Attrition:str
    Department:str
    MonthlyIncome:int
    PercentSalaryHike:int
    StockOptionLevel:int
    YearsAtCompany:int
    OverTime:str

    model_config=ConfigDict(from_attributes=True)

    
