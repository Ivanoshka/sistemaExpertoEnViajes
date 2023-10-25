import tkinter

#Datos que llena el usuario
nombre = ""
edad = 0
ciudadOrigen = ""
presupuesto = 0
intereses = []

#Nuestra Base De Datos
CiudadesDestino=""
AtraccionesDestino = ""
PresupuestoBase = 0

ventana = tkinter.Tk()
ventana.geometry("900x600")

#TOP
etiqueta = tkinter.Label(ventana, text="Bienvenido Al Sistema", background="#35BBCA")
etiqueta.pack(fill = tkinter.X)
#CONTENEDOR DE INPUTS
contenedor = tkinter.Label(ventana, background="white")
contenedor.pack(fill=tkinter.BOTH, expand=True)
#INPUT DE NOMBRE
labelNombre = tkinter.Label(ventana, text="Ingresa tu Nombre")
labelNombre.pack()
#INPUT DE EDAD
labelNombre = tkinter.Label(ventana, text="Ingresa tu Edad")
labelNombre.pack() #con el .pack centramos el texto 



ventana.mainloop()



