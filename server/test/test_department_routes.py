from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)


def test_retrieve_departments():
    response = client.get("/departments")
    assert response.status_code == 200


def test_retrieve_department():
    new_department = create_department()
    response = client.get(f"/departments/{new_department.json()["id"]}")
    assert response.status_code == 200


def test_create_department():
    new_department = create_department()
    assert new_department.status_code == 201
    assert new_department.json()['id'] is not None


def test_edit_department():
    new_department = create_department()

    data_to_be_updated = {
        "department_name": "Accounts",
    }

    edited_response = client.put(
        f"/departments/{new_department.json()["id"]}", json=data_to_be_updated)

    assert edited_response.status_code == 204

    department = client.get(f"/departments/{new_department.json()["id"]}")

    assert department.status_code == 200
    assert department.json()["department_name"] != new_department.json()[
        "department_name"]


def test_delete_department():
    new_department = create_department()
    response = client.delete(f"/departments/{new_department.json()["id"]}")
    assert response.status_code == 204


def dummy_department():
    department = {"department_name": "Electronics"}
    return department


def create_department():
    response = client.post("/departments", json=dummy_department())
    return response
