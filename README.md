# StudyFlow – Student Task Manager

StudyFlow is a simple command-line task manager built with Python. It helps students organize assignments, set due dates, track progress, and review completed work.

## Features
- Add tasks with a title, subject, and optional due date
- List tasks and filter by status
- Mark tasks as completed
- Delete tasks
- View a progress summary
- Save tasks locally in a JSON file

## Requirements
- Python 3.9 or newer
- No third-party packages required

## Run the application
```bash
python main.py
```

The application creates `tasks.json` automatically when you add your first task.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Project structure
```text
studyflow/
├── main.py
├── task_manager.py
├── README.md
├── LICENSE
├── .gitignore
└── tests/
    └── test_task_manager.py
```

## Contributing
Suggestions and improvements are welcome. Please open an issue to describe a bug or feature idea before making a substantial change.

## Roadmap
- [ ] Add task priority
- [ ] Add search by subject
- [ ] Add export to CSV
- [ ] Add a graphical interface

## License
This project is licensed under the MIT License. See `LICENSE`.
