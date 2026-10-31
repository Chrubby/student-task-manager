# HW2 Report — Student Task Manager

## 1. Project Purpose
The purpose of Student Task Manager is to help students organize coursework and assignment deadlines in one place. Users can add tasks with a course name, task name, due date, and priority. They can search and filter tasks, mark tasks as completed, delete tasks, and view a summary of their progress.

The project addresses the common problem of tracking assignments across multiple courses. The application uses a simple web interface so that users do not need to interact with the command line during normal use.

## 2. AI Collaboration
AI was used as a programming assistant during project planning, implementation, explanation, and debugging. The development process should be described truthfully using the actual prompts and changes made during this assignment.

Complete this section with:
- Which AI tool you used.
- What you asked it to help with.
- Which suggestions or code you accepted.
- What you changed yourself.
- At least one example of a problem you encountered and how you resolved it.

Do not claim that AI suggestions were tested or accepted unless you actually did so.

## 3. Software Engineering Practices
The project separates the user interface (`app.py`) from core task operations (`task_manager.py`). This makes the task-management functions easier to understand and test independently.

Unit tests are provided in `tests/test_task_manager.py`. They cover:
- Creating and saving a task.
- Updating a task's completion status.
- Deleting a task.
- Calculating task statistics.

Before submission, run the tests and record the actual result here:
- Test command: `python -m unittest discover -s tests -v`
- Actual result: [Write the number of tests passed and any failures after running the command.]

## 4. How to Run
1. Install the dependencies with `python -m pip install -r requirements.txt`.
2. Run the app with `python -m streamlit run app.py`.
3. Open the local web address shown in the terminal.

## 5. GitHub Repository
Repository URL: [Paste your GitHub repository URL here]

GitHub commit history: [Briefly describe the commits you actually made.]
