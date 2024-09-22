import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Importar correctamente tkcalendar

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Crear el TreeView para mostrar los eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Crear los campos de entrada
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0)
date_entry = DateEntry(frame, date_pattern='dd/mm/yyyy')  # Usar DateEntry para la fecha
date_entry.grid(row=0, column=1)

tk.Label(frame, text="Hora (HH:MM):").grid(row=1, column=0)
time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1)

tk.Label(frame, text="Descripción:").grid(row=2, column=0)
desc_entry = tk.Entry(frame)
desc_entry.grid(row=2, column=1)

# Crear los botones
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Agregar Evento", command=lambda: add_event(tree, date_entry, time_entry, desc_entry))
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar Evento Seleccionado", command=lambda: delete_event(tree))
delete_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Salir", command=root.quit)
exit_button.grid(row=0, column=2, padx=5)

# Función para agregar eventos
def add_event(tree, date_entry, time_entry, desc_entry):
    date = date_entry.get()
    time = time_entry.get()
    desc = desc_entry.get()
    if date and time and desc:
        tree.insert("", "end", values=(date, time, desc))
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

# Función para eliminar eventos
def delete_event(tree):
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
        if confirm:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

# Ejecutar la aplicación
root.mainloop()
