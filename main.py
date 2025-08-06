import json
import os

# gestor_tareas/main.py


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Ver solo tareas completadas")
    print("6. Ver solo tareas pendientes")
    print("7. Salir")


def guardar_tareas(tareas):
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo, indent=4)


def cargar_tareas():
    if os.path.exists("tareas.json"):
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    return []


def ver_tareas(tareas):
    print("Mostrando las tareas...")
    if not tareas:
        print("\n No hay tareas pendientes")
        return

    print("\n Lista de tareas: ")
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea['completada'] else "❌"
        print(f"{i + 1}. {estado} {tarea['descripcion']}")


def agregar_tarea(tareas):
    desc = input("\nDescripción de la nueva tarea: ")
    tareas.append({"descripcion": desc, "completada": False})
    guardar_tareas(tareas)
    print("Tarea agregada.")


def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        i = int(input("\nNúmero de tarea a marcar como completada: ")) - 1
        if 0 <= i < len(tareas):
            tareas[i]['completada'] = True
            guardar_tareas(tareas)
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
            guardar_tareas(tareas)
            print("Tarea eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
        
        
def editar_tarea(tareas):
    ver_tareas(tareas)
    try:
        i = int(input("\n Numero de tarea a editar: ")) - 1
        if 0 <= i < len(tareas)
            nueva_desc = input("Nueva descripcion: ")
            tareas[i]["descripcion"] = nueva_desc
            guardar_tareas(tareas)
            print("Tarea actualizada")
        else:
            print("Numero invalido")
    except ValueError:
        print("Entrada invalida.")


def ver_tareas_filtradas(tareas, completadas=True):
    filtradas = [t for t in tareas if t["completada"] == completadas]

    if not filtradas:
        print("\n No hay tareas " +
              ("completadas." if completadas else "pendientes."))

    print("\n Lista de tareas: " +
          ("completadas: " if completadas else "pendientes:"))
    for i, tarea in enumerate(filtradas):
        estado = "✅" if tarea['completada'] else "❌"
        print(f"{i + 1}. {estado} {tarea['descripcion']}")


def main():
    tareas = cargar_tareas()

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
            ver_tareas_filtradas(tareas, completadas=True)
        elif opcion == "6":
            ver_tareas_filtradas(tareas, completadas=False)
        elif opcion == "7":
            editar_tarea(tareas)
        elif opcion == "8":
             print("\n¡Hasta luego!")
             break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
