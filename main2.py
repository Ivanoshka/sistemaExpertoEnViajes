import tkinter as tk

# Definimos las listas desplegables para la ciudad de origen y los gustos personales
ciudades = ["Ciudad de México", "Guadalajara", "Monterrey", "Hermosillo", "Tijuana"]
gustos = ["Música", "Cine", "Deportes", "Cocina", "Lectura"]

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Planeador de Viajes")
ventana.geometry("600x400")

# Creamos las etiquetas y los campos de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_ciudad = tk.Label(ventana, text="Ciudad de origen:")
etiqueta_presupuesto = tk.Label(ventana, text="Presupuesto:")
etiqueta_gustos = tk.Label(ventana, text="Gustos personales:")

campo_nombre = tk.Entry(ventana)
campo_edad = tk.Entry(ventana)
campo_ciudad = tk.OptionMenu(ventana, "", *ciudades)
campo_presupuesto = tk.Entry(ventana)
campo_gustos = tk.OptionMenu(ventana, "", *gustos)

# Colocamos las etiquetas y los campos de texto en la ventana
etiqueta_nombre.grid(row=0, column=0)
campo_nombre.grid(row=0, column=1)
etiqueta_edad.grid(row=1, column=0)
campo_edad.grid(row=1, column=1)
etiqueta_ciudad.grid(row=2, column=0)
campo_ciudad.grid(row=2, column=1)
etiqueta_presupuesto.grid(row=3, column=0)
campo_presupuesto.grid(row=3, column=1)
etiqueta_gustos.grid(row=4, column=0)
campo_gustos.grid(row=4, column=1)

# Creamos el botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command="enviar")
boton_enviar.grid(row=5, column=0)

# Creamos la función que se ejecuta al hacer clic en el botón de enviar
def enviar():
    # Obtenemos los datos del usuario
    nombre = campo_nombre.get()
    edad = campo_edad.get()
    ciudad = campo_ciudad.get()
    presupuesto = campo_presupuesto.get()
    gustos = campo_gustos.get()

    # Mostramos un mensaje con los datos del usuario
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad de origen: {ciudad}")
    print(f"Presupuesto: {presupuesto}")
    print(f"Gustos personales: {gustos}")

# Ejecutamos el bucle principal de la aplicación
ventana.mainloop()
