# Todo App

The Todo App is a simple web application built with React & Flask, which allows users to create and manage a list of todo items. This README provides an overview of the Todo App, its features, and its architecture.

## Features

- Add new todo items with a title and time.
- Display the list of todo items on the main page.
- Delete todo items from the list.

## Architecture

The Todo App follows a client-server architecture, with the following components:

1. **Client-side-react-app**: The client-side component consists of HTML, CSS, and JavaScript files that are rendered in the user's web browser using react framework. The HTML templates define the structure of the web pages, CSS provides styling and layout, and JavaScript handles client-side interactions, such as adding and deleting todo items.

2. **Server-side-flask-server**: The server-side component is built with the Flask framework, a lightweight web framework written in Python. It handles HTTP requests and responses, data processing, and interacts with list data structure to store and retrieve todo items. The server-side code includes the Flask application logic, routing, and database operations.


## Backend Workflow: Build, Test, and Deploy Todo Backend

This GitHub workflow is triggered on each push to the `main` branch and when changes occur in the `todo-app-backend` directory. It performs the following steps:

1. Checks out the code from the repository.
2. Builds and tests the Docker image for the backend.
3. Deploys the Docker image to Render, a cloud platform for hosting web applications.

For more details, refer to the [GitHub Workflow file](./.github/workflows/build_test_deploy_todo_backend.yml) for the backend.

## Frontend Workflow: Build, Test, and Deploy Todo Frontend

This GitHub workflow is triggered on each push to the `main` branch and when changes occur in the `todo-app-frontend` directory. It performs the following steps:

1. Checks out the code from the repository.
2. Builds and tests the Docker image for the frontend.
3. Deploys the Docker image to Render.

For more details, refer to the [GitHub Workflow file](./.github/workflows/build_test_deploy_todo_frontend.yml) for the frontend.


## Getting Started

Backend Server

To run the Todo Backend locally, follow these steps:

1. Clone the repository:

git clone <repository_url>

2. Navigate to the project directory:

cd todo_app_backend

3. Bulid Docker Image:

docker buld -t todo_app_backend .  

4. Run the application:

docker run -p 5000:5000 todo_app_backend


5. Open a web browser and go to `http://localhost:5000` to access the Todo App Backend.

Frontend Server

To run the Todo Frontend locally, follow these steps:

1. Clone the repository:

git clone <repository_url>

2. Navigate to the project directory:

cd todo_app_frontend

3. Bulid Docker Image:

docker buld -t todo_app_frontend .  

4. Run the application:

docker run -p 3000:3000 todo_app_frontend

5. Open a web browser and go to `http://localhost:3000` to access the Todo App Frontend.

## Dependencies

The Todo App has the following dependencies:

- Docker: To Build the systems
- Flask: A Python web framework used for developing the server-side component.
- React: A node framework for frontend

## Contributing

Contributions to the Todo App are welcome! If you find any issues, have suggestions, or want to contribute enhancements, feel free to open a pull request or submit an issue in the project repository.
