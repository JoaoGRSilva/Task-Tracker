from connector import create_connection,get_cursor
from datetime import datetime

class TaskManager:

    status = ("todo", "in-progress", "done")

    def __init__(self):
        self.connection = create_connection()
        if self.connection:
            self.cursor = get_cursor(self.connection)
        else:
            raise Exception("Failed to connect to the database")
        
    def create_task(self, description, status: str="todo"):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_at = created_at

        add_query = (
            "INSET INTO tasks (description, status, created_at, updated_at) "
            "VALUES (%s, %s, %s, %s)"
        )
        task_data = (description, status, created_at, update_at)

        try:
            self.cursor.execute(add_query, task_data)
            self.connection.commit()
            print("Task created successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def update_task(self, id, description):
        update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_query = (
            "UPDATE tasks SET description= %s, update_at = %s WHERE id= %s"
        )

        update_data = (description, update_at, id)

        try:
            self.cursor.execute(update_query, update_data)
            self.connection.commit()
            print("Task update sucessffully.")
        except Exception as e:
            print(F"Error: {e}")

    def delete_task(self, id):
        delete_query = (
            "DELETE FROM tasks WHERE id = %d"
        )

        try:
            self.cursor.execute(delete_query, id)
            self.connection.commit()
            print("Task deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")