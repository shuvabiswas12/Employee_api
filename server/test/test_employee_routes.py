from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)


def test_retrieve_employees():
    response = client.get("/employees")
    assert response.status_code == 200


def test_retrieve_employee():
    new_employee = create_employee()
    response = client.get(f"/employees/{new_employee.json()["id"]}")
    assert response.status_code == 200


def test_create_employee():
    new_employee = create_employee()
    assert new_employee.status_code == 201
    assert new_employee.json()['id'] is not None


def test_edit_employee():
    new_employee = create_employee()

    data_to_be_updated = {
        "name": "User1",
        "gender": "female",
        "email": "user1@yahoo.com",
        "department_id": _create_department()["id"],
        "salary": "15000.0",
        "tenure": 5,
        "hiring_trend": "stable"
    }

    edited_response = client.put(
        f"/employees/{new_employee.json()["id"]}", json=data_to_be_updated)

    assert edited_response.status_code == 204

    employee = client.get(f"/employees/{new_employee.json()["id"]}")

    assert employee.status_code == 200
    assert employee.json()["id"] == new_employee.json()["id"]
    assert employee.json()["name"] != new_employee.json()["name"]
    assert employee.json()["gender"] != new_employee.json()["gender"]
    assert employee.json()["email"] != new_employee.json()["email"]
    assert employee.json()["department_id"] != new_employee.json()[
        "department_id"]
    assert employee.json()["salary"] != new_employee.json()["salary"]
    assert employee.json()["tenure"] != new_employee.json()["tenure"]
    assert employee.json()["hiring_trend"] != new_employee.json()[
        "hiring_trend"]


def test_delete_employee():
    new_employee = create_employee()
    response = client.delete(f"/employees/{new_employee.json()["id"]}")
    assert response.status_code == 204


def _create_department():
    response = client.post(
        "/departments", json={"department_name": "Accounts"})
    return response.json()


def dummy_employee():
    employee = {"name": "Bob",
                "gender": "male",
                "email": "bob@gmail.com",
                "department_id": _create_department()["id"],
                "salary": 12000.0,
                "tenure": 3,
                "hiring_trend": "growing",
                }
    return employee


def create_employee():
    response = client.post("/employees", json=dummy_employee())
    return response
