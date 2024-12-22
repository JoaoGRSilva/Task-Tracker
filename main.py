from taskmanager import TaskManager

def print_menu():
    print("\n=== Task Manager ===")
    print("1. Criar nova tarefa")
    print("2. Atualizar tarefa")
    print("3. Deletar tarefa")
    print("4. Marcar tarefa como em progresso")
    print("5. Marcar tarefa como concluída")
    print("6. Listar todas as tarefas")
    print("7. Listar tarefas concluídas")
    print("8. Listar tarefas em progresso")
    print("9. Listar tarefas pendentes")
    print("0. Sair")
    print("==================")

def main():
    task_manager = TaskManager()
    
    while True:
        print_menu()
        try:
            option = int(input("Escolha uma opção: "))
            
            if option == 0:
                print("Encerrando o programa...")
                task_manager.close_connection()
                break
                
            elif option == 1:
                description = input("Digite a descrição da tarefa: ")
                task_manager.create_task(description)
                
            elif option == 2:
                task_id = int(input("Digite o ID da tarefa: "))
                new_description = input("Digite a nova descrição: ")
                task_manager.update_task(task_id, new_description)
                
            elif option == 3:
                task_id = int(input("Digite o ID da tarefa a ser deletada: "))
                task_manager.delete_task(task_id)
                
            elif option == 4:
                task_id = int(input("Digite o ID da tarefa a ser marcada em progresso: "))
                task_manager.mark_progress(task_id)
                
            elif option == 5:
                task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
                task_manager.mark_done(task_id)
                
            elif option == 6:
                print("\nTodas as tarefas:")
                task_manager.list_all()
                
            elif option == 7:
                print("\nTarefas concluídas:")
                task_manager.list_done()
                
            elif option == 8:
                print("\nTarefas em progresso:")
                task_manager.list_in_progress()
                
            elif option == 9:
                print("\nTarefas pendentes:")
                task_manager.list_todo()
                
            else:
                print("Opção inválida! Por favor, tente novamente.")
                
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
        except Exception as e:
            print(f"Erro: {e}")
            
if __name__ == "__main__":
    main()