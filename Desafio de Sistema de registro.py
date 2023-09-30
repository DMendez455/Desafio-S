import os

#Función para agregar una tarea
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    
    with open("tareas_pendientes.txt", "a") as archivo:
        archivo.write(f"Título: {titulo}\n")
        archivo.write(f"Descripción: {descripcion}\n")
        archivo.write("-" * 30 + "\n")

#Función para listar tareas pendientes
def listar_tareas_pendientes():
    if os.path.exists("tareas_pendientes.txt"):
        with open("tareas_pendientes.txt", "r") as archivo:
            tareas = archivo.read()
            print("Tareas Pendientes:\n")
            print(tareas)
    else:
        print("No hay tareas pendientes.")
        
#Función para marcar una tarea como completada
def marcar_completada():
    listar_tareas_pendientes()
    tarea_completada = input("Ingrese el número de la tarea que desea marcar como completada: ")
    
#Leer las tareas pendientes
    with open("tareas_pendientes.txt", "r") as archivo:
        lineas = archivo.readlines()
    
#Encontrar la tarea seleccionada y eliminarla de las pendientes
    tarea_encontrada = False
    with open("tareas_pendientes.txt", "w") as archivo:
        for i, linea in enumerate(lineas):
            if linea.strip() == f"Título: {tarea_completada}":
                tarea_encontrada = True
                continue
            if not tarea_encontrada:
                archivo.write(linea)
    
#Si se encontró y eliminó la tarea, agregarla a las tareas completadas
    if tarea_encontrada:
        with open("tareas_completadas.txt", "a") as archivo:
            archivo.write(f"Título: {tarea_completada}\n")
            archivo.write("-" * 30 + "\n")
        print(f"La tarea '{tarea_completada}' se ha marcado como completada.")
    else:
        print("Tarea no encontrada.")

# Función principal
def main():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas_pendientes()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
