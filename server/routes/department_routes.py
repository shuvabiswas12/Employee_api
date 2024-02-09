from typing import List
from fastapi import APIRouter, Query, status
from server.models.department import DepartmentModel, DepartmentResponseModel

from server.services.department_service import create_department, delete_department, edit_department, get_department, get_departments

department_router = APIRouter(prefix="/departments", tags=["Department"])


@department_router.get("", status_code=status.HTTP_200_OK, response_model=List[DepartmentResponseModel])
async def get():
    return await get_departments()


@department_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DepartmentResponseModel)
async def get(id: str):
    return await get_department(id)


@department_router.post("", status_code=status.HTTP_201_CREATED, response_model=DepartmentResponseModel)
async def create(department: DepartmentModel):
    return await create_department(department)


@department_router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit(id: str, department: DepartmentModel):
    return await edit_department(id, department)


@department_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    return await delete_department(id)
