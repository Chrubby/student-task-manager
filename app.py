import streamlit as st
from datetime import date
from task_manager import load_tasks, add_task, update_task, delete_task, get_summary

st.set_page_config(page_title="Student Task Manager", page_icon="📚", layout="wide")
st.title("📚 Student Task Manager")
st.caption("A simple dashboard to organize coursework, assignments, and deadlines.")

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

tasks = st.session_state.tasks
summary = get_summary(tasks)

c1, c2, c3 = st.columns(3)
c1.metric("Total tasks", summary["total"])
c2.metric("Completed", summary["completed"])
c3.metric("Remaining", summary["remaining"])

st.divider()
st.subheader("Add a new task")
with st.form("add_task_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    course = col1.text_input("Course name", placeholder="e.g. Introduction to Finance")
    task_name = col2.text_input("Task name", placeholder="e.g. Homework 2")
    col3, col4 = st.columns(2)
    due_date = col3.date_input("Due date", value=date.today())
    priority = col4.selectbox("Priority", ["High", "Medium", "Low"], index=1)
    submitted = st.form_submit_button("Add task")
    if submitted:
        if not course.strip() or not task_name.strip():
            st.error("Please enter both a course name and a task name.")
        else:
            tasks = add_task(tasks, course.strip(), task_name.strip(), due_date.isoformat(), priority)
            st.session_state.tasks = tasks
            st.success("Task added.")
            st.rerun()

st.divider()
st.subheader("Your tasks")
search_text = st.text_input("Search by course or task name")
status_filter = st.selectbox("Show tasks", ["All", "Incomplete", "Completed"])
filtered_tasks = []
for task in tasks:
    matches_search = search_text.lower() in (task["course"] + " " + task["name"]).lower()
    matches_status = (
        status_filter == "All"
        or (status_filter == "Completed" and task["completed"])
        or (status_filter == "Incomplete" and not task["completed"])
    )
    if matches_search and matches_status:
        filtered_tasks.append(task)

if not filtered_tasks:
    st.info("No tasks found. Add a task above to get started.")
else:
    for task in filtered_tasks:
        with st.container(border=True):
            left, middle, right = st.columns([3, 2, 1])
            left.markdown(f"**{task['name']}**")
            left.caption(task["course"])
            middle.write(f"Due: {task['due_date']}")
            middle.write(f"Priority: {task['priority']}")
            new_status = right.checkbox(
                "Completed",
                value=task["completed"],
                key=f"completed_{task['id']}"
            )
            if new_status != task["completed"]:
                tasks = update_task(tasks, task["id"], completed=new_status)
                st.session_state.tasks = tasks
                st.rerun()
            if right.button("Delete", key=f"delete_{task['id']}"):
                st.session_state.tasks = delete_task(tasks, task["id"])
                st.rerun()

st.caption("Your tasks are saved locally in tasks.json.")
