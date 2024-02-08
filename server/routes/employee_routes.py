from fastapi import APIRouter
from server.models.employee import EmployeeModel

from server.services.employee_service import create_employee, delete_employee, edit_employee, get_employee, get_employees

employee_router = APIRouter(prefix="/employees", tags=["Employee"])


@employee_router.get("")
async def get():
    return await get_employees()


@employee_router.get("/{id}")
async def get(id: str):
    return await get_employee(id)


@employee_router.post("")
async def create(employee: EmployeeModel):
    return await create_employee(employee)


@employee_router.put("/{id}")
async def edit(id: str, employee: EmployeeModel):
    return await edit_employee(id, employee)


@employee_router.delete("/{id}")
async def delete(id: str):
    return await delete_employee(id)
