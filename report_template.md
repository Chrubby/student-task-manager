# HW2 Report — Student Task Manager

## 1. Project Purpose

The purpose of Student Task Manager is to help students organize coursework and assignment deadlines in one place.

Users can:
- Add tasks with a course name, task name, due date, and priority.
- Search tasks by course name or task name.
- Filter tasks by completion status.
- Mark tasks as completed.
- Delete tasks.
- View task statistics, including total tasks, completed tasks, and remaining tasks.

The application provides a simple and user-friendly web interface using Python and Streamlit.

It also saves task information in a JSON file, allowing users to keep their data after closing and reopening the application.

## 2. AI Collaboration

ChatGPT was used as an AI programming assistant during this assignment.

The AI assistant helped with:
- Understanding the project requirements.
- Setting up the Python development environment.
- Learning how to use VS Code and the terminal.
- Understanding Git and GitHub commands.
- Explaining the project structure and software testing process.
- Troubleshooting GitHub connection problems.

Some AI suggestions and instructions were followed, including setting up a virtual environment, installing dependencies, running unit tests, and connecting the local project to GitHub.

The student independently performed the installation, executed the commands, tested the application, created the GitHub repository, and checked the results.

One problem occurred when pushing the project to GitHub. The remote repository URL contained an incorrect GitHub username. The problem was resolved by checking the correct username and updating the remote URL using `git remote set-url origin`.

AI assistance was used to support learning and problem-solving throughout the development process.

## 3. Software Engineering Practices

The project separates the user interface (`app.py`) from core task operations (`task_manager.py`).

This separation makes the code easier to understand, maintain, and test.

Unit tests are provided in `tests/test_task_manager.py`.

The tests cover:
- Creating and saving a task.
- Updating a task's completion status.
- Deleting a task.
- Calculating task statistics.

**Test command:**

`python -m unittest discover -s tests -v`

**Actual result:**

4 tests passed successfully with no failures.

The application was also tested manually. Adding, deleting, searching, filtering, and completing tasks worked as expected.

Task information remained available after closing and reopening the application.

## 4. How to Run

Follow these steps to run the application:

1. Install Python.
2. Open the project folder in VS Code.
3. Create a virtual environment:

   `python -m venv .venv`

4. Activate the virtual environment:

   `.\.venv\Scripts\Activate.ps1`

5. Install the dependencies:

   `python -m pip install -r requirements.txt`

6. Run the application:

   `python -m streamlit run app.py`

7. Open the local web address shown in the terminal, usually `http://localhost:8501`.

## 5. GitHub Repository

**Repository URL:**

https://github.com/Chrubby/student-task-manager

**GitHub commit history:**

The initial commit was created successfully and pushed to GitHub.

- `7299799` — Initial commit: create student task manager

The project uses Git for version control and GitHub for remote code storage.

The repository is publicly accessible so that the project files and development history can be reviewed.