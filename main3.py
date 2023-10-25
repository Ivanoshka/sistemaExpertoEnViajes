import tkinter as tk

# Definimos las listas desplegables para la ciudad de origen y los gustos personales
ciudades = ["Ciudad de México", "Guadalajara", "Monterrey", "Hermosillo", "Tijuana"]
gustos = ["Música", "Cine", "Deportes", "Cocina", "Lectura"]

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Planeador de Viajes")
ventana.geometry("600x400")

# Función para manejar el botón de enviar
def enviar():
    nombre = campo_nombre.get()
    edad = campo_edad.get()
    ciudad = campo_ciudad.get()
    presupuesto = campo_presupuesto.get()
    gustos = campo_gustos.get()

    # Mostrar los datos en un cuadro de diálogo
    mensaje = f"Nombre: {nombre}\nEdad: {edad}\nCiudad de origen: {ciudad}\nPresupuesto: {presupuesto}\nGustos personales: {gustos}"
    tk.messagebox.showinfo("Información del Usuario", mensaje)

# Etiquetas y campos de entrada
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_ciudad = tk.Label(ventana, text="Ciudad de origen:")
etiqueta_presupuesto = tk.Label(ventana, text="Presupuesto:")
etiqueta_gustos = tk.Label(ventana, text="Gustos personales:")

campo_nombre = tk.Entry(ventana)
campo_edad = tk.Entry(ventana)
campo_ciudad = tk.StringVar(ventana)
campo_ciudad.set(ciudades[0])
campo_presupuesto = tk.Entry(ventana)
campo_gustos = tk.StringVar(ventana)
campo_gustos.set(gustos[0])

# Botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)

# Organización de widgets en la ventana
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5)
campo_nombre.grid(row=0, column=1, padx=10, pady=5)
etiqueta_edad.grid(row=1, column=0, padx=10, pady=5)
campo_edad.grid(row=1, column=1, padx=10, pady=5)
etiqueta_ciudad.grid(row=2, column=0, padx=10, pady=5)
campo_ciudad_menu = tk.OptionMenu(ventana, campo_ciudad, *ciudades)
campo_ciudad_menu.grid(row=2, column=1, padx=10, pady=5)
etiqueta_presupuesto.grid(row=3, column=0, padx=10, pady=5)
campo_presupuesto.grid(row=3, column=1, padx=10, pady=5)
etiqueta_gustos.grid(row=4, column=0, padx=10, pady=5)
campo_gustos_menu = tk.OptionMenu(ventana, campo_gustos, *gustos)
campo_gustos_menu.grid(row=4, column=1, padx=10, pady=5)
boton_enviar.grid(row=5, column=0, columnspan=2, pady=10)

# Ejecución de la aplicación
ventana.mainloop()
