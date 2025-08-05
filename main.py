# gestor_tareas/main.py

def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ver_tareas(tareas):
    print("📋 Mostrando la lista de tareas...")
    if not tareas:
        print("\nNo hay tareas todavía.")
        return
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea['completada'] else "❌"
        print(f"{i+1}. {estado} {tarea['descripcion']}")

def agregar_tarea(tareas):
    desc = input("\nDescripción de la nueva tarea: ")
    tareas.append({"descripcion": desc, "completada": False})
    print("Tarea agregada.")

def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        i = int(input("\nNúmero de tarea a marcar como completada: ")) - 1
        if 0 <= i < len(tareas):
            tareas[i]['completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        i = int(input("\nNúmero de tarea a eliminar: ")) - 1
        if 0 <= i < len(tareas):
            tareas.pop(i)
            print("Tarea eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
