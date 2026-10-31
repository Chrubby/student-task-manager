# Student Task Manager

A beginner-friendly coursework and assignment tracker built with Python and Streamlit.

## Features
- Add assignments with course, due date, and priority
- Mark assignments as completed
- Delete assignments
- Search by course or task name
- Filter completed and incomplete tasks
- View task statistics
- Save data locally in `tasks.json`

## Requirements
- Python 3.10 or newer
- pip

## Setup (Windows PowerShell)
1. Open this project folder in VS Code.
2. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

3. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and try again.

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   python -m streamlit run app.py
   ```

## Run tests
In the project folder, run:

```powershell
python -m unittest discover -s tests -v
```

## Project structure
- `app.py`: Streamlit user interface
- `task_manager.py`: task operations and JSON storage
- `tests/`: automated unit tests
- `tasks.json`: created automatically when tasks are saved

## Data note
Tasks are stored locally in `tasks.json` on the computer running the app. This starter version does not use a cloud database or user accounts.
