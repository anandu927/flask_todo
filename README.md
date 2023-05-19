# Todo App

The Todo App is a simple web application built with React & Flask, which allows users to create and manage a list of todo items. This README provides an overview of the Todo App, its features, and its architecture.

## Features

- Add new todo items with a title and time.
- Display the list of todo items on the main page.
- Delete todo items from the list.

## Architecture

The Todo App follows a client-server architecture, with the following components:

1. **Client-side**: The client-side component consists of HTML, CSS, and JavaScript files that are rendered in the user's web browser. The HTML templates define the structure of the web pages, CSS provides styling and layout, and JavaScript handles client-side interactions, such as adding and deleting todo items.

2. **Server-side**: The server-side component is built with the Flask framework, a lightweight web framework written in Python. It handles HTTP requests and responses, data processing, and interacts with list data structure to store and retrieve todo items. The server-side code includes the Flask application logic, routing, and database operations.


Live Server :

React Forented : https://todo-frontend-djew.onrender.com
Flask Backed   : https://todo-backend-o2ar.onrender.com

## Getting Started

To run the Todo App locally, follow these steps:

1. Clone the repository:

git clone <repository_url>

2. Navigate to the project directory:

cd todo_app


3. Install the required dependencies:

pip install -r requirements.txt

4. Run the application:

python app.py


5. Open a web browser and go to `http://localhost:5000` to access the Todo App.

## Dependencies

The Todo App has the following dependencies:

- Flask: A Python web framework used for developing the server-side component.

## Contributing

Contributions to the Todo App are welcome! If you find any issues, have suggestions, or want to contribute enhancements, feel free to open a pull request or submit an issue in the project repository.
