from fastapi import FastAPI
from server.routes.department_routes import department_router
from server.routes.employee_routes import employee_router

app = FastAPI()

app.include_router(employee_router)
app.include_router(department_router)
