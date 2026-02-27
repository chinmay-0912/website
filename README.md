# website
## 

commands: 
- 'docker compose up -d' : 
    description: 'Start the website using Docker Compose.'
    details: 'This command will start all the necessary services defined in the docker-compose.yml file. Make sure you have Docker installed and running on your machine before executing this command.'

create virtual environment:
- 'python -m venv {virtual_environment_name}' : 
    description: 'Create a virtual environment for your Python project.'
    details: 'Replace {virtual_environment_name} with the desired name for your virtual environment. This command will create a new directory with the specified name, containing the isolated Python environment.'
- backend_env\Scripts\activate : 
    description: 'Activate the virtual environment on Windows.'
    details: 'Run this command in your terminal to activate the virtual environment. Once activated, any Python packages you install will be contained within this environment.'

start server 
-  uvicorn backend.src.main:app --reload : 
    description: 'Start the FastAPI server with auto-reload enabled.'
    details: 'This command will start the FastAPI server defined in the main.py file located in the backend/src directory. The --reload flag allows the server to automatically restart whenever you make changes to the code, making development easier.'



# STEPS - 
### Step 1: 
- Create a virtual environment for your Python project using the command: `python -m venv {virtual_environment_name}`. Replace `{virtual_environment_name}` with your desired name for the virtual environment.
- Activate the virtual environment using the command: `backend_env\Scripts\activate` (for Windows) or `source backend_env/bin/activate` (for Unix/Linux/Mac). This will ensure that any Python packages you install are contained within this environment.
- Install the required dependencies for your project using the command: `pip install -r requirements.txt`. This will read the requirements.txt file and install all the necessary packages for your project.

### Step 2:
- Run `docker compose up --build` to start the website using Docker Compose. This command will start all the necessary services defined in the docker-compose.yml file. Make sure you have Docker installed and running on your machine before executing this command.
- `docker exec -it blog_db psql -U postgres -d blogdb` to access the PostgreSQL database container. This command allows you to interact with the database using the psql command-line tool. You can run SQL queries, manage tables, and perform other database operations from this interface.
- `python -m backend.src.create_tables` to create the necessary tables in the PostgreSQL database. This command will execute the create_tables.py script located in the backend/src directory, which contains the logic to create the required tables for your application.
- \dt in database to list all the tables in the PostgreSQL database. This command will show you a list of all the tables that have been created in the database, allowing you to verify that the tables were created successfully.

### Step 3:
- Start the FastAPI server with auto-reload enabled using the command: `uvicorn backend.src.main:app --reload`. This command will start the FastAPI server defined in the main.py file located in the backend/src directory. The `--reload` flag allows the server to automatically restart whenever you make changes to the code, making development easier.

### Step 4:
- `npm run dev` to start the frontend development server. This command will run the development server for your frontend application, allowing you to view and interact with your website in a web browser. Make sure you have Node.js and npm installed on your machine before executing this command.

### Step 5:
- `taskkill /F /IM python.exe /T` nuclear option to forcefully terminate all Python processes. This command is useful when you want to stop the FastAPI server or any other Python processes that may be running in the background. Use this command with caution, as it will terminate all Python processes without prompting for confirmation.
- `netstat -ano | findstr :8000` to find the process ID (PID) of any process using port 8000. This command will display a list of all processes that are currently using port 8000, along with their corresponding PIDs. You can use this information to identify which process is running on that port.
- `taskkill /PID {PID} /F` to terminate a specific process using its
- 