# CIT-105 Week 7 Assignment 2
## Kanban Migration and SQLite Data Layer

**Student:** Matthew Espinel
**Course:** CIT-105

## Project Overview
This project is a Kanban Task Manager developed using Python, Flask, and SQLite. It allows users to create tasks, update their status, and delete tasks.

## Features
- Add tasks with a title and description.
- Organize tasks into To Do, In Progress, and Done.
- Update task status.
- Delete tasks.
- Store task information in an SQLite database.

## Technologies Used
- Python
- Flask
- SQLite
- HTML and CSS
- Git and GitHub

## Project Files
- app.py: Flask application and task management functionality.
- migrate.py: SQLite database initialization script.
- kanban.db: Local SQLite database generated when the application runs.

## Database Migration
The migrate.py script initializes the SQLite database. Task records are stored in the database and can be retrieved by the Flask application.

## How to Run
1. Install Python and Flask.
2. Run `python migrate.py` to initialize the database.
3. Run `python app.py` to start the application.
4. Open `http://127.0.0.1:5000` in a web browser.

## Testing
The application was tested locally by creating a baseball training task and moving it through To Do, In Progress, and Done. The SQLite database was also queried to confirm the task record and its final status.

## GitHub Repository
https://github.com/matdeimon44-cmyk/cit105-week6

## Conclusion
This project demonstrates how to use Flask with SQLite to build a task management application with persistent data storage.
