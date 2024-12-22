from connector import create_connection, get_cursor
from datetime import datetime
from prettytable import PrettyTable


def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class TaskManager:
    status = ("todo", "in-progress", "done")

    def __init__(self):
        self.connection = create_connection()
        if self.connection:
            self.cursor = get_cursor(self.connection)
        else:
            raise Exception("Failed to connect to the database")

    def create_task(self, description, status: str = "todo"):
        created_at = get_time()
        update_at = created_at

        add_query = (
            "INSERT INTO tasks (description, status, created_at, updated_at) "
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
        update_at = get_time()

        update_query = (
            "UPDATE tasks SET description = %s, updated_at = %s WHERE id = %s"
        )

        update_data = (description, update_at, id)

        try:
            self.cursor.execute(update_query, update_data)
            self.connection.commit()
            print("Task updated successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_task(self, id):
        delete_query = "DELETE FROM tasks WHERE id = %s"

        try:
            self.cursor.execute(delete_query, (id,))
            self.connection.commit()
            print("Task deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def mark_progress(self, id):
        update_at = get_time()
        progress_query = (
            "UPDATE tasks SET status = 'in-progress', updated_at = %s WHERE id = %s"
        )

        progress_data = (update_at, id)

        try:
            self.cursor.execute(progress_query, progress_data)
            self.connection.commit()
            print("Task marked as in-progress successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def mark_done(self, id):
        update_at = get_time()
        done_query = (
            "UPDATE tasks SET status = 'done', updated_at = %s WHERE id = %s"
        )
        done_data = (update_at, id)

        try:
            self.cursor.execute(done_query, done_data)
            self.connection.commit()
            print("Task marked as done successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def list_all(self):
        list_all_query = "SELECT * FROM tasks"
        try:
            self.cursor.execute(list_all_query)
            all_list = self.cursor.fetchall()
            
            table = PrettyTable()
            table.field_names = ["ID", "Descrição", "Status", "Criado em", "Atualizado em"]
            
            for task in all_list:
                table.add_row(task)
            
            print(table)
        except Exception as e:
            print(f"Error: {e}")

    def list_done(self):
        list_done_query = "SELECT * FROM tasks WHERE status = 'done'"
        try:
            self.cursor.execute(list_done_query)
            done_list = self.cursor.fetchall()
            
            table = PrettyTable()
            table.field_names = ["ID", "Descrição", "Status", "Criado em", "Atualizado em"]
            
            for task in done_list:
                table.add_row(task)
            
            print(table)
        except Exception as e:
            print(f"Error: {e}")

    def list_in_progress(self):
        in_progress_query = "SELECT * FROM tasks WHERE status = 'in-progress'"
        try:
            self.cursor.execute(in_progress_query)
            in_progress_list = self.cursor.fetchall()
            
            table = PrettyTable()
            table.field_names = ["ID", "Descrição", "Status", "Criado em", "Atualizado em"]
            
            for task in in_progress_list:
                table.add_row(task)
            
            print(table)
        except Exception as e:
            print(f"Error: {e}")

    def list_todo(self):
        todo_query = "SELECT * FROM tasks WHERE status = 'todo'"
        try:
            self.cursor.execute(todo_query)
            todo_list = self.cursor.fetchall()
            
            table = PrettyTable()
            table.field_names = ["ID", "Descrição", "Status", "Criado em", "Atualizado em"]
            
            for task in todo_list:
                table.add_row(task)
            
            print(table)
        except Exception as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()