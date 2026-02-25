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
