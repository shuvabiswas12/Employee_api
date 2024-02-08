from fastapi import APIRouter, Query
from server.models.department import DepartmentModel, DepartmentResponseModel

from server.services.department_service import create_department, delete_department, edit_department, get_department, get_departments

department_router = APIRouter(prefix="/departments", tags=["Department"])


@department_router.get("")
async def get():
    return await get_departments()


@department_router.get("/{id}")
async def get(id: str):
    return await get_department(id)


@department_router.post("")
async def create(department: DepartmentModel):
    return await create_department(department)


@department_router.put("/{id}")
async def edit(id: str, department: DepartmentResponseModel):
    return await edit_department(id, department)


@department_router.delete("/{id}")
async def delete(id: str):
    return await delete_department(id)
