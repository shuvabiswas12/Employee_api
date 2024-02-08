from bson import ObjectId
from fastapi import HTTPException

from server.helpers import check_objectId
from ..database import departments_collection
from server.models.department import DepartmentModel, DepartmentResponseModel


def department_helper(department):
    return DepartmentResponseModel(id=str(department["_id"]), department_name=department["department_name"])


async def get_departments() -> list:
    departments: list[DepartmentResponseModel] = []
    for department in departments_collection.find():
        departments.append(department_helper(department))
    return departments


async def get_department(id: str):
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    result = departments_collection.find_one(ObjectId(id))
    if result is None:
        raise HTTPException(status_code=404, detail="Not found!")
    return department_helper(result)


async def create_department(department: DepartmentModel):
    result = departments_collection.insert_one(dict(department))
    return DepartmentResponseModel(id=str(result.inserted_id), department_name=department.department_name)


async def edit_department(id: str, department: DepartmentModel) -> bool:
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    result = departments_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": department.model_dump()})
    if result is None:
        raise HTTPException(status_code=404, detail="Not found!")
    return True


async def delete_department(id: str) -> bool:
    if not check_objectId(id):
        raise HTTPException(status_code=500, detail="Invalid Id!")

    result = departments_collection.find_one_and_delete(
        {"_id": ObjectId(id)})
    if result is None:
        raise HTTPException(status_code=404, detail="Not found!")
    return True
