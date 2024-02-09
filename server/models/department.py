from pydantic import BaseModel, Field


class DepartmentModel(BaseModel):
    department_name: str = Field(min_length=2)

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "department_name": "Accounts"
            }
        }


class DepartmentResponseModel(BaseModel):
    id: str
    department_name: str = Field(min_length=2)

    class ConfigDict:
        json_schema_extra = {
            "example": {
                "id": "65c490b995bed3ce95876fc2",
                "department_name": "Accounts"
            }
        }
