"""Command-line interface for StudyFlow."""

from task_manager import TaskManager


def show_menu():
    print("\n=== StudyFlow ===")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Show progress")
    print("0. Exit")


def main():
    manager = TaskManager("tasks.json")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            subject = input("Subject: ").strip()
            due_date = input("Due date (YYYY-MM-DD, optional): ").strip() or None
            try:
                task = manager.add_task(title, subject, due_date)
                print(f"Added task #{task['id']}: {task['title']}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks yet. Add your first task!")
            for task in tasks:
                status = "Done" if task["completed"] else "Pending"
                due = task["due_date"] or "No due date"
                print(f"#{task['id']} [{status}] {task['title']} | {task['subject']} | {due}")

        elif choice == "3":
            try:
                task_id = int(input("Task ID to complete: "))
                manager.complete_task(task_id)
                print("Task marked as completed.")
            except (ValueError, KeyError) as error:
                print(f"Could not complete task: {error}")

        elif choice == "4":
            try:
                task_id = int(input("Task ID to delete: "))
                manager.delete_task(task_id)
                print("Task deleted.")
            except (ValueError, KeyError) as error:
                print(f"Could not delete task: {error}")

        elif choice == "5":
            summary = manager.summary()
            print(f"Total: {summary['total']} | Completed: {summary['completed']} | Pending: {summary['pending']}")
            print(f"Completion rate: {summary['completion_rate']}%")

        elif choice == "0":
            print("Good luck with your studies!")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
