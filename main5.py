import tkinter as tk
from PIL import Image, ImageTk

ciudades = ["Ciudad de México", "Guadalajara", "Monterrey", "Hermosillo", "Tijuana"]
gustos = ["Música", "Cine", "Deportes", "Cocina", "Lectura"]

ventana = tk.Tk()
ventana.title("Planeador de Viajes")
ventana.geometry("500x400")

imagen_fondo = Image.open("./fondo_venecia.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

marco = tk.Frame(ventana, bg="white")
marco.pack(padx=20, pady=20)

fuente = ("Helvetica", 12)

def mostrar_resultado():
    nombre = campo_nombre.get()
    edad = campo_edad.get()
    ciudad = campo_ciudad.get()
    presupuesto = campo_presupuesto.get()
    gustos = campo_gustos.get()

    resultado_ventana = tk.Toplevel()
    resultado_ventana.title("Resultado")
    resultado_ventana.geometry("550x360")

    if int(presupuesto) >= 500:
        recomendacion = "CIUDAD DE MEXICO"
        imagen_ruta = "./cdmx.jpg"
    elif int(presupuesto) >= 3000:
        recomendacion = "Otra Ciudad"
        imagen_ruta = "./otra_ciudad.jpg"
     elif int(presupuesto) >= 4500:
        recomendacion = "Otra Ciudad"
        imagen_ruta = "./otra_ciudad.jpg"

    resultado_texto = f"Hola {nombre}, el sistema te recomienda en base a los datos ingresados:\n {recomendacion}"

    etiqueta_resultado = tk.Label(resultado_ventana, text=resultado_texto, font=fuente)
    etiqueta_resultado.pack(padx=20, pady=10)

    imagen = Image.open(imagen_ruta)
    imagen = imagen.resize((200, 150))
    imagen = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(resultado_ventana, image=imagen)
    etiqueta_imagen.image = imagen
    etiqueta_imagen.pack(padx=20, pady=10)

Label_nombre = tk.Label(marco, text="Ingresa tu Nombre", width=20)
etiqueta_nombre = tk.Label(marco, text="Nombre:", font=fuente, bg="white")
etiqueta_edad = tk.Label(marco, text="Edad:", font=fuente, bg="white")
etiqueta_ciudad = tk.Label(marco, text="Ciudad de origen:", font=fuente, bg="white")
etiqueta_presupuesto = tk.Label(marco, text="Presupuesto:", font=fuente, bg="white")
etiqueta_gustos = tk.Label(marco, text="Gustos personales", font=fuente, bg="white")

campo_nombre = tk.Entry(marco, font=fuente)
campo_edad = tk.Entry(marco, font=fuente)

campo_ciudad = tk.StringVar(ventana)
campo_ciudad.set(ciudades[0])
campo_ciudad_menu = tk.OptionMenu(marco, campo_ciudad, *ciudades)

campo_presupuesto = tk.Entry(marco, font=fuente)

campo_gustos = tk.StringVar(ventana)
campo_gustos.set(gustos[0])
campo_gustos_menu = tk.OptionMenu(marco, campo_gustos, *gustos)

boton_enviar = tk.Button(marco, text="Consultar", command=mostrar_resultado, font=fuente, bg="lightblue")

etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
campo_nombre.grid(row=0, column=1, padx=10, pady=5)
etiqueta_edad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
campo_edad.grid(row=1, column=1, padx=10, pady=5)
etiqueta_ciudad.grid(row=2, column=0, padx=10, pady=5, sticky="w")
campo_ciudad_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")
etiqueta_presupuesto.grid(row=3, column=0, padx=10, pady=5, sticky="w")
campo_presupuesto.grid(row=3, column=1, padx=10, pady=5)
etiqueta_gustos.grid(row=4, column=0, padx=10, pady=5, sticky="w")
campo_gustos_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")
boton_enviar.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()
