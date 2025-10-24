import json



class Task:
    
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
        
    def __str__(self):
        status = "✓" if self.completed else " "    
        return f"[{status}]  #{self.id}: {self.description}" 
    
    
class TaskManager:
    
    FILENAME="tasks.json"
    
    def __init__(self):
        self._tasks = [] #Lista vacia de tareas
        self._next_id = 1  #Contador privado para asignar IDs únicos a las tareas
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description}")
        self.save_tasks()
        
    
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
                    self.save_tasks()
                    return
            except ValueError:
                print("ID inválido. Por favor ingrese un número entero.")
                return
        print(f"Tarea #{id} no encontrada.")
        
    
    def delete_task(self, id):
        for task in self._tasks:
            try:
                task_id = int(id)
                if task.id == task_id:
                    self._tasks.remove(task)
                    print(f"Tarea #{id} eliminada.")
                    self.save_tasks()
                    return
            except ValueError:
                print("ID inválido. Por favor ingrese un número entero.")
                return
            
        print(f"Tarea #{id} no encontrada.")
        
        
    
    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as file:
                data = json.load(file)
            self._tasks = [Task(item['id'], item['description'], item['completed']) for item in data]
            if self._tasks:
                self._next_id = self._tasks[-1].id +1
            else:
                self._next_id = 1       
        except FileNotFoundError:
            self._tasks = []
            self._next_id = 1
        except json.JSONDecodeError:
            print("Error al cargar las tareas. El archivo puede estar corrupto.")
            self._tasks = []
            self._next_id = 1

    def save_tasks(self):
        try:
            with open(self.FILENAME, 'w') as file:
                json.dump([{"id": task.id, "description": task.description, "completed": task.completed} 
                           for task in self._tasks], file, indent=4)              
              
        except FileNotFoundError:
            self._tasks = []
            self._next_id = 1
        except json.JSONDecodeError:
            print("Error al cargar las tareas. El archivo puede estar corrupto.")
            self._tasks = []
            self._next_id = 1