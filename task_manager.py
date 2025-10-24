class Task:
    
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
        
    def __str__(self):
        status = "✓" if self.completed else " "    
        return f"[{status}]  #{self.id}: {self.description}" 
    
    
class TaskManager:
    def __init__(self):
        self._tasks = [] #Lista vacia de tareas
        self._next_id = 1  #Contador privado para asignar IDs únicos a las tareas

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description}")
        
    
    def lst_tasks(self):
        if not self._tasks:
            print("No hay tareas pendientes.")
            return
        else:
            for task in self._tasks:
                print(task)
    
    def complete_task(self, id):
        for task in self._tasks:
            try:
                task_id = int(id)
                if task.id == task_id:
                    task.completed = True
                    print(f"Tarea #{id} marcada como completada.")
                    return
            except ValueError:
                print("ID inválido. Por favor ingrese un número entero.")
                return
        print(f"Tarea #{id} no encontrada.")
        
    
    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea #{id} eliminada.")
                return
            
        print(f"Tarea #{id} no encontrada.")
        
        