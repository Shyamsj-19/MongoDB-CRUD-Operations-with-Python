# MongoDB CRUD Operations with Python

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Python with MongoDB. A Docker container is set up with MongoDB, and Python scripts interact with the MongoDB instance to perform the CRUD operations.

Prerequisites
- Docker installed on your machine
- Python installed (version 3.x recommended)
- Project Structure
- Dockerfile: Contains the Docker configuration to set up a MongoDB container.
- init-mongo.js: Initialization script for MongoDB to set up the database and collection.
- main.py: Python script to perform CRUD operations.

## Setup Instructions
1. Build and Run MongoDB Docker Container
Navigate to the project directory and execute the following commands to build and run the Docker container:

### Build Docker image
**docker build -t mongodb-crud .**

### Run Docker container
**docker run -d -p 27017:27017 mongodb-crud**

2. Initialize MongoDB
The initialization script init-mongo.js will create a database named personal_details and a collection named details with a unique index on the unique_id field.

3. Run Python Script
Execute the Python script script.py to perform CRUD operations on the MongoDB database:

**python main.py**

The script performs the following operations for each data input:
Create: Inserts a new record into the details collection with a unique ID.
Read: Retrieves and prints the created record from the details collection.
Update: Updates the age of the record by incrementing it by 1.
Delete: Deletes the record from the details collection.

Expected Output
Upon running the Python script, you will see the CRUD operations performed for each data input, along with the corresponding database operations (Create, Read, Update, Delete) printed to the console.

Conclusion
This project provides a hands-on example of performing CRUD operations using Python with MongoDB. Follow the setup instructions to run the project and explore the basic database operations.

Happy coding!
