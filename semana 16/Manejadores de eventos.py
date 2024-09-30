import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada para nuevas tareas
        self.entry_task = tk.Entry(root, width=35)
        self.entry_task.pack(pady=10)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=35, height=10)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Enlace de atajos de teclado
        self.entry_task.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<Escape>', lambda event: self.root.destroy())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('c', lambda event: self.complete_task())
        self.root.bind('d', lambda event: self.delete_task())

        # Lista interna para manejar tareas
        self.tasks = []

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            if not task.startswith("[Completada]"):
                self.tasks[selected_index[0]] = "[Completada] " + task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, self.tasks[selected_index[0]])
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para completar.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
