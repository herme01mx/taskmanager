from task_manager import TaskManager  

def print_menu():
    print("\n----- Gestor de Tareas Inteligentes ---")
    print("\n----- Gestor de Tareas Inteligentes ---")
    print("1. Añadir Tarea")
    print("2. Listar Tareas")   
    print("3. Completar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
        
def main():
    
    manager = TaskManager()
    
    while True:
        print_menu()
        
        try:
            choice = int(input("\nSeleccione una opción: "))
        
            match choice:
                case 1:
                    descripcion = input("Ingrese la descripción de la tarea: ")
                    manager.add_task(descripcion)
                case 2:
                    manager.lst_tasks()
                case 3:
                    task_id = input("Id de la tarea a completar: ")
                    manager.complete_task(task_id)  
                case 4:
                    task_id = input("Id de la tarea a a eliminar: ")
                    manager.delete_task(task_id)
                case 5:
                    print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print(f"Opción no válida. Intente de nuevo:")

if __name__ == "__main__":
    main()
    