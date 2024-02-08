from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator

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

    @validator("email")
    def validate_email_domain(cls, v):
        allowed_domains = ["gmail.com", "yahoo.com"]
        email_domain = v.split("@")[-1]
        if email_domain not in allowed_domains:
            raise ValueError(
                "Only email addresses from 'Gmail' or 'Yahoo' domains are allowed")
        return v


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
