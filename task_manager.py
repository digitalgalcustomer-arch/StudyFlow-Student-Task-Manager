"""Core task management logic for StudyFlow."""

import json
import os
from datetime import date


class TaskManager:
    def __init__(self, storage_path="tasks.json"):
        self.storage_path = storage_path
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(self.storage_path):
            return []
        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Task storage must contain a list.")
            return data
        except json.JSONDecodeError as error:
            raise ValueError("The tasks file contains invalid JSON.") from error

    def _save(self):
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=2, ensure_ascii=False)

    def add_task(self, title, subject, due_date=None):
        title = title.strip()
        subject = subject.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if not subject:
            raise ValueError("Subject cannot be empty.")
        if due_date:
            try:
                date.fromisoformat(due_date)
            except ValueError as error:
                raise ValueError("Due date must use YYYY-MM-DD format.") from error

        next_id = max((task["id"] for task in self.tasks), default=0) + 1
        task = {
            "id": next_id,
            "title": title,
            "subject": subject,
            "due_date": due_date,
            "completed": False,
        }
        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self, completed=None):
        if completed is None:
            return list(self.tasks)
        return [task for task in self.tasks if task["completed"] is completed]

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        task["completed"] = True
        self._save()
        return task

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        self.tasks.remove(task)
        self._save()
        return task

    def summary(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        rate = round((completed / total) * 100, 1) if total else 0
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": rate,
        }

    def _find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise KeyError(f"No task found with ID {task_id}.")
