from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
from server.helpers import check_objectId

from server.models.department import DepartmentResponseModel


# Enums
class Gender(str, Enum):
    Male = "male"
    Female = "female"


class HiringTrend(str, Enum):
    Growing = "growing"
    Stable = "stable"
    Declining = "declining"


class EmployeeModel(BaseModel):
    name: str = Field(min_length=3)
    gender: Gender
    email: EmailStr
    department_id: str
    salary: float = Field(gt=1000.0)
    tenure: int = Field(gt=0.0)
    hiring_trend: HiringTrend

    @validator("department_id")
    def validate_department_id(cls, v):
        output = check_objectId(v)
        if output is False:
            raise ValueError("Department_id should be a valid ID.")
        return v

    @validator("email")
    def validate_email_domain(cls, v):
        allowed_domains = ["gmail.com", "yahoo.com"]
        email_domain = v.split("@")[-1]
        if email_domain not in allowed_domains:
            raise ValueError(
                "Only email addresses from 'Gmail' or 'Yahoo' domains are allowed")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Bob",
                "gender": "Male",
                "email": "bob@gmail.com",
                "department_id": "65c490b995bed3ce95876fc2",
                "salary": "12000",
                "tenure": 3,
                "hiring_trend": "growing",
            }
        }


class EmployeeResponseModel(BaseModel):
    id: str
    name: str = Field(min_length=2)
    gender: Gender
    email: EmailStr
    department_id: Optional[str] = Field(default="")
    department: Optional[DepartmentResponseModel] = Field(default={})
    salary: float = Field(gt=1000.0)
    tenure: int = Field(gt=0.0)
    hiring_trend: HiringTrend

    class Config:
        json_schema_extra = {
            "example": {
                "id": "65c490b995bed3ce95876fc2",
                "name": "Bob",
                "gender": "Male",
                "email": "bob@gmail.com",
                "department_id": "65c490b995bed3ce95876fc2",
                "department": {
                    "id": "65c490b995bed3ce95876fc2",
                    "department_name": "Accounts"
                },
                "salary": "12000",
                "tenure": 3,
                "hiring_trend": "growing",
            }
        }
