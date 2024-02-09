
# Employee API

My First API which is built on top of FastAPI. In this API I use mongoDb as Database. Here in this project, I do Unit Test using PyTest.


## Run Locally

Clone the project

```bash
  git clone https://github.com/shuvabiswas12/Employee_api
```

Go to the project directory

```bash
  cd Employee_api
```

Create virtual env

```bash
  python -m venv .venv
```

Activate the env

```bash
  .venv\Scripts\activate.bat
```

Install dependencies 

```bash
  pip install -r requirements.txt
```

Run the project

```bash
  python main.py
```

Run the project

```bash
  python main.py
```

## Accessing the API from Browser
Goto browser and type 

```bash
  localhost:8000/docs
```
and hit enter. You can see all endpoint.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_URL`

For Example:
DB_URL="Your mongoDb url"

## Running Tests

To run tests, run the following command

```bash
  pytest -v -s
```
This command will run all test cases.


