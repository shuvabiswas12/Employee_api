from pydantic import BaseModel, Field


class DepartmentModel(BaseModel):
    department_name: str = Field(min_length=2)


class DepartmentResponseModel(BaseModel):
    id: str
    department_name: str = Field(min_length=2)
