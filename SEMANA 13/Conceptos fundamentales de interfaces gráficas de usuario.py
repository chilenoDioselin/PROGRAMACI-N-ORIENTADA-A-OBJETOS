import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar():
    info = entry.get()
    if info:
        lista.insert(tk.END, info)
        entry.delete(0, tk.END)

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Información")

# Crear y ubicar los componentes
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
