from typing import List
from fastapi import APIRouter, status
from server.models.employee import EmployeeModel, EmployeeResponseModel

from server.services.employee_service import create_employee, delete_employee, edit_employee, get_employee, get_employees

employee_router = APIRouter(prefix="/employees", tags=["Employee"])


@employee_router.get("", status_code=status.HTTP_200_OK, response_model=List[EmployeeResponseModel])
async def get():
    return await get_employees()


@employee_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeResponseModel)
async def get(id: str):
    return await get_employee(id)


@employee_router.post("", status_code=status.HTTP_201_CREATED, response_model=EmployeeResponseModel)
async def create(employee: EmployeeModel):
    return await create_employee(employee)


@employee_router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit(id: str, employee: EmployeeModel):
    return await edit_employee(id, employee)


@employee_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    return await delete_employee(id)
