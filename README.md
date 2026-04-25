# Task CLI 📝

A lightweight command-line task manager built with pure Python.
Manage your tasks directly from the terminal with zero dependencies.

---

## 🚀 Quick Start

```bash
git clone https://github.com/kamigokun/task-cli.git
cd task-cli

python -m task_cli.main add "Test task"
python -m task_cli.main list
```

---

## 📦 Features

* Add, update, delete tasks
* Mark tasks as `todo`, `in-progress`, or `done`
* Filter tasks by status
* Persistent storage using JSON
* Clean modular architecture
* No external libraries required

---

## 🗂 Project Structure

```
task-cli/
├── task_cli/
│   ├── __init__.py       # Marks folder as a Python package
│   ├── models.py         # Task structure and validation
│   ├── storage.py        # Read/write tasks.json
│   ├── commands.py       # Business logic (add, delete, update)
│   └── main.py           # CLI entry point
├── tasks.json            # Task database (auto-created)
└── README.md
```

---

## ⚙️ Usage

### Add a task

```bash
python -m task_cli.main add "Buy groceries"
```

### List all tasks

```bash
python -m task_cli.main list
```

### Filter tasks

```bash
python -m task_cli.main list todo
python -m task_cli.main list done
python -m task_cli.main list in-progress
```

### Update a task

```bash
python -m task_cli.main update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python -m task_cli.main delete 1
```

### Update status

```bash
python -m task_cli.main mark-in-progress 1
python -m task_cli.main mark-done 1
```

---

## 📄 Example Output

```
ID   Status         Description
----------------------------------------
1    done           Buy groceries
2    todo           Write code
```

---

## 🧠 How It Works

* CLI input is parsed via `sys.argv`
* Commands are routed in `main.py`
* Business logic lives in `commands.py`
* Data is stored in `tasks.json` via `storage.py`
* Validation handled in `models.py`

---

## ⚠️ Error Handling

* Invalid or missing arguments
* Non-existent task IDs
* Invalid status values
* Empty or oversized descriptions
* Corrupted JSON file (auto-recovers)

---

## 🧱 Design Philosophy

* **Separation of concerns** → each file has one job
* **No dependencies** → runs on any Python setup
* **Simple data layer** → easy to replace with a database later

---

## 🔧 Requirements

* Python 3.6+

---

## 📌 Future Improvements

* Installable CLI command (`task-cli`)
* Database support (PostgreSQL)
* REST API layer
* Web interface

---

## 👤 Author

**Harshit Rawat**
GitHub: https://github.com/kamigokun
https://roadmap.sh/projects/task-tracker
