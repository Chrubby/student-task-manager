import tempfile
import unittest
from pathlib import Path

from task_manager import add_task, update_task, delete_task, get_summary, load_tasks


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "test_tasks.json"
        self.tasks = []

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task_creates_task_and_saves_it(self):
        result = add_task(
            self.tasks, "Finance", "Homework 2", "2026-11-10", "High",
            file_path=self.data_file
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Homework 2")
        self.assertFalse(result[0]["completed"])
        self.assertEqual(len(load_tasks(self.data_file)), 1)

    def test_update_task_changes_completion_status(self):
        tasks = add_task(
            self.tasks, "Finance", "Homework 2", "2026-11-10", "High",
            file_path=self.data_file
        )
        task_id = tasks[0]["id"]
        updated = update_task(
            tasks, task_id, file_path=self.data_file, completed=True
        )
        self.assertTrue(updated[0]["completed"])

    def test_delete_task_removes_task(self):
        tasks = add_task(
            self.tasks, "Finance", "Homework 2", "2026-11-10", "High",
            file_path=self.data_file
        )
        result = delete_task(tasks, tasks[0]["id"], file_path=self.data_file)
        self.assertEqual(result, [])

    def test_summary_counts_tasks(self):
        tasks = [
            {"id": "1", "completed": True},
            {"id": "2", "completed": False},
            {"id": "3", "completed": False},
        ]
        self.assertEqual(
            get_summary(tasks),
            {"total": 3, "completed": 1, "remaining": 2}
        )


if __name__ == "__main__":
    unittest.main()
