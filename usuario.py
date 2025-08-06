class Usuario:
    def __init__ (self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def listar_tareas(self):
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")
