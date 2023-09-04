Backend Takehome Project

Prerequisites

    Docker: Ensure Docker is installed on your machine. If not, you can download it from Docker's official website.
    
    Python Virtual Environment: Set up a Python virtual environment by following these steps:

        python3 -m venv .env
        source .env/bin/activate
        pip install -r requirements.txt

Running the Application

    With Docker:
        Use the provided script to run the application with Docker:

            ./run_docker.sh

        This script leverages docker-compose.yml to orchestrate a service, which is made up of a FastAPI application. The backend uses PostgreSQL as the database and SQLAlchemy for the Object Relational Mapping (ORM) layer.

    Interacting with the API:
        Execute the ETL process by running the following script:

            ./run_etl.sh
            
        This script calls the API using a curl command targeting http://127.0.0.1:8000/etl/. A successful call will display {"status":"success"} in the terminal.

    Querying the Database within the Docker Container:
        To query the database directly from within the Docker container, use:

            ./query_db.sh

        Note: The script has backend_takehome-db-1 hard-coded as the container name. If your container name differs, ensure you modify the script accordingly.


If you'd like to restart from scratch you can use:

    docker-compose down -v

to take down the container along with its volume.