# Covid 19 Flask App

This is a flask restful api for covid 19 data. It contains endpoints for getting data about covid 19 cases from different countries. 

This project gets all its data from an external  [Media Group API](https://github.com/M-Media-Group/Covid-19-API) and caches it a postgress database.

This API contains 3 endpoints

1. GET `/countries`
   This is to get confirmed cases, recovered cases and death case of covid 19 for all countries.

   ```json
   {
    "status": "success",
    "message": "Countries retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Afghanistan",
            "confirmed_cases": 178901,
            "recovered_cases": 0,
            "deaths": 7683,
            "population": 35530081,
            "sq_km_area": 652090,
            "continent": "Asia",
            "abbreviation": "AF",
            "location": "Southern and Central Asia",
            "iso": 4,
            "capital_city": "Kabul",
            "lat": "33.93911",
            "long": "67.709953",
            "last_updated_at": "2022-05-05 04:20:55"
        },
        ...
    ]
    }
   ```

2. GET `/countries/refresh`
   This refreshes the data. can be used by a clone to update the data from the original dataset.

   ```json
   {
     "status": "success",
     "message": "Succesfull",
     "data": {
       "total_deaths": 6189121,
       "total_recovered_cases": 0,
       "total_confirmed_cases": 510366766,
       "total_population": 7320542947
     }
   }
   ```

3. GET `/summary `  
   This is to get the summary of the data. It returns the total confirmed, recovered and death cases.
   ```json{
   "status": "success",
   "message": "Succesfull",
   "data": {
       "total_deaths": 1,
       "total_cases_recovered": 1,
       "total_cases_confirmed": 1,
       "total_population": 1
    }
   }
   ```

> A frontend that utilises this api is available at [kamasuPaul/covid-19-dashboard-react-app](https://github.com/kamasuPaul/covid-19-dashboard-react-app)

### Project Setup

Follow these steps to have a local running copy of the app.

##### Clone The Repo

`git clone <url-to-repo>`

##### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create a development database and call it `dev_db`.

##### Create a Virtual Environment

create virtual enviroment called venv

Run `virtualenv venv`

> Windows: `python -m venv venv` or c:\Python35\python -m venv venv

##### Activate the virtual environment.

Run `. venv/bin/activate`

> Windows: `. venv\Scripts\activate`

Make sure you have `pip` installed on your machine.

##### Install the dependencies.

`pip install -r requirements.txt`

##### Create a .env file

Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```
export FLASK_APP=server.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
SQLALCHEMY_DATABASE_URI="postgresql://postgres:root@localhost/dev_db"

```

##### Run Database migrations

Run migrations for the database

`python manage.py db upgrade`

##### Run Application

Run the application with this command

`flask run`

##### Test the API

Through your browser or postman go to link `localhost:<flask_port>/`.

##### Checkout Api docs

Through your browser go to link `localhost:<flask_port>/apidocs`.

### Deployment using docker
The project has a Dockerfile in the root of the project which can be used to deploy the app to a docker container.
