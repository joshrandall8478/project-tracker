# project-tracker

Simple Task &amp; Project Tracker

---

The goal of

## Dependencies

- Python 3.12
- NodeJS 22

### Frameworks

- Backend
  - Flask
  - sqlite3
- Frontend
  - Vite
  - ReactJS
  - Bootstrap

## Deployment

### Docker

This project provides dockerfiles and a docker compose to build and launch to avoid the need to install dependencies and frameworks.

To clone, build, and launch the application:

```bash
git clone https://github.com/joshrandall8478/project-tracker
cd project-tracker
docker compose up -d --build
```

You should then be able to navigate to `http://localhost` and use the application as normal.

### Without Docker

To get the application running outside of docker, clone the repository and install the necessary dependencies.

#### Backend

> [!IMPORTANT]
> Make sure to run the following commands in the `backend` directory

A conda environment has been provided for your convenience. Conda provides a virutal environment to use in python without the need to create a `.venv`, and can be entirely based off of a .yml file. To install the conda environment, run this in the backend directory:

```bash
conda env create -f conda.yml
```

You can [install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) on practically any operating system. Miniconda or Anaconda Distribution should be sufficient. I am using conda version 25.11.0.

To activate the conda environment after installation, run this:

```bash
conda activate project-tracker
```

If you want to use python itself to create the python virtual environment and install requirements that way, you can do so like this:

```bash
python3 -m venv .venv
```

Then activate the virtual environment, and install the dependencies

```bash
source .venv/bin/activate
pip3 install -r requirements.txt
```

And finally, the API deployment commands.
Initialize the sqlite3 database first if it doesn't exist:

```bash
mkdir db
python3 init_db.py
```

Then, run the flask API.

```bash
flask --app api run --host 0.0.0.0
```

#### Frontend

> [!IMPORTANT]
> Make sure to run the following commands in the `frontend` directory
> Make sure you have nodejs and npm installed. Install the required dependencies, then run the vite development server.

```bash
npm i
npm run dev
```
