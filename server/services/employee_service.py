from bson import ObjectId
from fastapi import HTTPException

from server.helpers import check_objectId
from server.services.department_service import department_helper
from ..database import employees_collection, departments_collection
from server.models.employee import EmployeeModel, EmployeeResponseModel


def employee_helper(employee, department):
    return EmployeeResponseModel(
        id=str(employee["_id"]),
        name=employee["name"],
        gender=employee["gender"],
        email=employee["email"],
        department_id=employee["department_id"],
        department=department_helper(department),
        salary=employee["salary"],
        tenure=employee["tenure"],
        hiring_trend=employee["hiring_trend"])


async def get_employees() -> list:
    employees: list(EmployeeResponseModel) = []
    for employee in employees_collection.find():
        department_id = employee["department_id"]
        department = departments_collection.find_one(
            {"_id": ObjectId(department_id)})
        employees.append(employee_helper(employee, department))
    return employees


async def get_employee(id: str):
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    employee = employees_collection.find_one({"_id": ObjectId(id)})
    department = departments_collection.find_one(
        {"_id": ObjectId(employee["department_id"])})
    return employee_helper(employee, department)


async def delete_employee(id: str) -> bool:
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    result: dict or None = employees_collection.find_one_and_delete(
        {"_id": ObjectId(id)})
    if result is None:
        raise HTTPException(status_code=404, detail="Not found!")
    return True


async def edit_employee(id: str, employee: EmployeeModel) -> bool:
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    result = employees_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": employee.model_dump()})
    if result is None:
        raise HTTPException(status_code=404, detail="Not found!")
    return True


async def create_employee(employee: EmployeeModel):
    result = employees_collection.insert_one(dict(employee))
    return EmployeeResponseModel(
        id=str(result.inserted_id),
        department_id=employee.department_id,
        email=employee.email,
        name=employee.name,
        salary=employee.salary,
        gender=employee.gender,
        tenure=employee.tenure,
        hiring_trend=employee.hiring_trend)
