Backend Takehome Project

Prerequisites

    Docker: Ensure Docker is installed on your machine. If not, you can download it from Docker's official website https://www.docker.com/.
    

Running the Application

    Make sure the bash files have execution privleges:

        chmod +x run_docker.sh run_etl.sh query_db.sh

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

        NOTE: The script has eikon-db-1 hard-coded as the container name. If your container name differs, ensure you modify the script accordingly.  It is usually
              something along the lines of {current_workspace}-db-1.

            Update script to: docker exec -it {your-db-container-name} psql -U eikon -d eikondb -x -c "SELECT * FROM users;"


If you'd like to restart from scratch you can use the CMD below to take down the container along with its volume to start with fresh DB.

    docker-compose down -v


Important Considerations for the Current Implementation:

    Handling Ties in Common Compounds:

        Current Scenario: In cases of a tie for the most common compound associated with a user, the system arbitrarily selects the first compound from the list.

        Potential Implications: This might not always yield the desired result, and the specific requirements should be clarified. The approach should be tailored accordingly to ensure data accuracy and user expectations.

    Data Loading Approach in the ETL Controller:

        Current Scenario: The ETL process loads the entire dataset into memory before processing.

        Potential Implications: While this is feasible for the current dataset size, it might become a bottleneck for larger datasets. If data volumes increase significantly, a batching mechanism would be more efficient and prevent memory exhaustion.

    Atomicity in Database Object Creation:

        Current Scenario: Objects are created based on their models. For instance, all User objects are created first, followed by all Experiment objects, and then all Compound objects. A commit to the database is made after each model's objects have been created.

        Potential Implications: Grouping objects by model type before committing can optimize performance but might also expose the system to partial data scenarios if there's an interruption after one model's objects are committed but before the others. Balancing performance optimization with data integrity is crucial.

    Error Handling:

        Current Scenario: The existing code primarily follows the "happy path" without comprehensive error or exception handling.

        Potential Implications: In real-world scenarios, unexpected issues can arise. The system should be robust enough to handle errors gracefully. This could include strategies like rolling back in case of failures, or providing detailed logs and feedback about specific data points or operations that encountered issues.






