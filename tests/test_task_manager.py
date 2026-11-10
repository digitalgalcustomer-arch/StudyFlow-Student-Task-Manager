
import os
import tempfile
import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.temp.name, "tasks.json")
        self.manager = TaskManager(self.path)

    def tearDown(self):
        self.temp.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Study Python", "Programming")
        self.assertEqual(task["title"], "Study Python")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("", "Programming")

    def test_complete_task(self):
        self.manager.add_task("Homework", "Math")
        self.manager.complete_task(1)
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_delete_task(self):
        self.manager.add_task("Read book", "English")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.list_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
