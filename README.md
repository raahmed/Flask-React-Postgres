# Flask + React + Postgres Starter 

This is a minimal sample Flask and React starter code that demonstrates how both frameworks can be used together in a single page web Application.

The code is based on https://github.com/dternyak/React-Redux-Flask and https://github.com/creativetimofficial/material-dashboard-react

## Tutorial

### Setting Up The Project

1. Clone the reponsitory
```bash
git clone https://github.com/jeffreymew/Flask-React-Postgres.git
cd Flask-React-Postgres
```

2. Create and activate a virtual environment

In Bash
```bash
python3 -m venv venv
source venv/bin/activate
```

In Powershell
```Powershell
py -3 -m venv env
env\scripts\activate
```

2. Install requirements.txt
```bash
pip install -r requirements.txt
```

3. Import the project folder into VS Code
```bash
code .
```

### Running The Code Locally

1. Build the react.js front-end.
```bash
npm install
npm run build
```
2. Create the SQL database
```bash
cd ..
python manage.py create_db
```

3. (optionally) provide an instrumentation key to send telemetry to Application Insights
```bash
export APPINSIGHTS_INSTRUMENTATIONKEY="<insert your instrumentation key here>"
```

4. Start the Flask server
```bash
python manage.py runserver
```
5. Check ```localhost:5000``` in your browser to view the web application.

### Deploying The Code To Azure

#### VSCode Setup

1. Go to the extensions tab on VS Code

2. Install the recommended extensions that show up (App Service Extension, Python Extension)

3. Reload the window and navigate to the Azure tab on the left

#### App Service Setup

1. Access Azure services through (1) Guest Mode, (2) Creating a free Azure account or (3) signing into Azure with an existing account

2. [Create an App Service](https://code.visualstudio.com/docs/python/tutorial-deploy-app-service-on-linux) instance with the parameters of a L`inux system with a Python 3.7 runtime

3. Navigate to the Azure portal for the App service instance that was just created, and under the "Application Settings" tab and uneder the "Runtime" section, set the "Startup File" parameter to be *scripts/startup.sh*

4. Set `POST_BUILD_SCRIPT_PATH=scripts/post.sh`  in app settings (VSCode or portal)

#### Database Setup

1. [Create a PostgreSQL database with Azure Database for Postgres](https://docs.microsoft.com/en-us/azure/postgresql/quickstart-create-server-database-portal) 

2. Navigate to the Azure portal for the Azure Database for Postgres instance and allow incoming connections:

   - Connection Security - Allow access to Azure Services (not sure this is needed)  
   - Connection Security - add local laptopIP to firewall rules 
   
3. Create a new empty database on the Postgres instance, e.g *team_standup*

4. Run the create_db script with a `DATABASE_URL` for the Azure database:
   ```
   DATABASE_URL=postgresql://<username>:<password>@<dbserver>.postgres.database.azure.com:5432/<database> python manage.py create_db
   ```
    *NOTE: the `<username>` is of the format `<name>@<dbserver>`*


#### Keyvault Setup

1. Create an Azure KeyVault with a secret named `database-url` which contains the entire Postgres database URL, e.g.
   ```
   postgresql://<username>:<password>@<dbserver>.postgres.database.azure.com:5432/<database>
   ```

2. Add the `KEY_VAULT_URI` as an application setting environment variable

#### Deployment

1. In VSCode, Configure Deployment Source as *LocalGit*

2. Optionally, under the "Application Settings", add a new environment variable for [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).

3. In VSCode, right-click the App Service, select *Deploy to Web App*

(See [Deploying your app using Git](right-click the App Service again, select Deploy to Web App) for more details)

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.
