# Task Manager

A command-line task management system built with Python that helps you track and organize your tasks using a SQL database.

## Features

- Create, update and delete tasks
- Mark tasks as in-progress or done 
- List all tasks with different filtering options:
  - All tasks
  - Done tasks
  - In-progress tasks
  - Todo tasks
- Persistent storage using SQL database
- Pretty-formatted console output

## Requirements

- Python 3.6+
- MySQL/PostgreSQL database
- PrettyTable library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. Install required dependencies:
```bash
pip install prettytable mysql-connector-python
```

3. Configure your database connection:
Create a file named `connector.py` with your database credentials:

```python
import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

def get_cursor(connection):
    return connection.cursor()
```

4. Create the tasks table in your database:
```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    status ENUM('todo', 'in-progress', 'done') DEFAULT 'todo',
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

## Usage

```python
from task_manager import TaskManager

# Initialize the task manager
manager = TaskManager()

# Create a new task
manager.create_task("Buy groceries")

# Update a task
manager.update_task(1, "Buy groceries and cook dinner")

# Mark task as in-progress
manager.mark_progress(1)

# Mark task as done
manager.mark_done(1)

# List all tasks
manager.list_all()

# List tasks by status
manager.list_done()
manager.list_in_progress()
manager.list_todo()

# Delete a task
manager.delete_task(1)

# Always close the connection when done
manager.close_connection()
```

## Task Properties

Each task contains the following properties:

- `id`: Unique identifier (auto-generated)
- `description`: Task description
- `status`: Current status (todo/in-progress/done)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Error Handling

The system includes comprehensive error handling for database operations. All methods will print success messages on completion or error messages if something goes wrong.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
