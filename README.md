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
- Interactive menu interface

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

Run the program:
```bash
python main.py
```

You'll see an interactive menu with the following options:

```
=== Task Manager ===
1. Criar nova tarefa
2. Atualizar tarefa
3. Deletar tarefa
4. Marcar tarefa como em progresso
5. Marcar tarefa como concluída
6. Listar todas as tarefas
7. Listar tarefas concluídas
8. Listar tarefas em progresso
9. Listar tarefas pendentes
0. Sair
==================
```

### Example Usage Flow:

1. **Creating a new task**:
   - Select option 1
   - Enter task description when prompted
   - System will confirm task creation

2. **Updating a task**:
   - Select option 2
   - Enter the task ID
   - Enter the new description
   - System will confirm update

3. **Marking a task as in-progress**:
   - Select option 4
   - Enter the task ID
   - System will confirm status change

4. **Viewing all tasks**:
   - Select option 6
   - System will display a formatted table with all tasks

5. **Marking a task as done**:
   - Select option 5
   - Enter the task ID
   - System will confirm completion

6. **Viewing specific task lists**:
   - Select options 7, 8, or 9 to view done, in-progress, or pending tasks respectively
   - System will display a filtered table of tasks

7. **Exiting the program**:
   - Select option 0
   - System will close database connection and exit

### Error Handling
The program handles various types of errors:
- Invalid menu selections
- Invalid input types (non-numeric when number expected)
- Database operation errors
- Connection errors

## Task Properties

Each task contains the following properties:

- `id`: Unique identifier (auto-generated)
- `description`: Task description
- `status`: Current status (todo/in-progress/done)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
