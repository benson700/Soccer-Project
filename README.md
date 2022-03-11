# Soccer-Project
# Project structure
Project structure
The project 1 folder, namely `football` and 3 files, `README.md`,
`requirements.txt` and `routes.py`

- `README.md`  is the file you're reading it now. It contain the briefy description of the project.

- `requirements.txt` is the text file which contains the libraries and modules required for the project to run, the dependencies. Instead of installing it one by one, running this file will install everything needed.

- `routes.py` is file contain the codebase of the API endpoints.

In the folder `football` there're 4 files namely `__init__.py`,
`crud.py`, `models.py` and `football.db`

- `__init__.py` is the file which setup and initialize our project. Initialize our database and the flask server.

- `crud.py` is the file contains the CRUD operations defined in functions
which are used in `routes.py` (our endpoints)

- `models.py` is the file which defines our models, the tables and their respective attributes of the database. `Player` and `Team` table are defined here.

- `football.db` is our sqlalchemy database for this project. 

# Getting started
- Clone the project

```
git clone https://github.com/benson700/Soccer-Project.git

- Navigate in the directory

```
cd Soccer-Project
```

# Run the project
In the directory `Soccer-Project`.
- Install the requirements
```
pip install -r requirements.txt
```
- Run the flask server
```
python3 routes.py
```

- Up to this point, all endpoints are live. You can check them

# Endpoints
- Endpoints are well explained in the detailed documentation.
You can read them [here](https://github.com)

# Running tests with Pytest

- Navigate in the folder `tests` from root directory
of the project
```
cd tests
```

- Run the tests with `Pytest`
```
pytest test_routes.py
```

# CI/CD with Jenkins
Now that we have our sweet Flask API, we're going to deploy them on Docker container. But this process will take place automatically, thanks to Jenkins. We will use Jenkins to auto-deploy our API.
Follow these steps:

- We will use Jenkins on GCP instance 
 with the public ssh you will be able to acess the jenkins website login .



# Licence
MIT licence
