import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Entrada de texto para nuevas tareas
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
task_entry.bind('<Return>', add_task)  # Añadir tarea al presionar Enter

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir Tarea", width=48, command=add_task)
add_button.pack(pady=5)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Botón para marcar tarea como completada
complete_button = tk.Button(root, text="Marcar como Completada", width=48, command=mark_completed)
complete_button.pack(pady=5)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", width=48, command=delete_task)
delete_button.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
