# Soccer-Project
# Project structure
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

- `models.py` is the file which defines our models, the tables and their respective attributes of the database. `Player` and `Team` table are defined 