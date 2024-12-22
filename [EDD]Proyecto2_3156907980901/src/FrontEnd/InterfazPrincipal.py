from tkinter import *

ventana = Tk()
ventana.title("Titulo de Prueba")
ventana.geometry("1200x800")

texto_elemento = Label(ventana, text="Hola Mundo")
texto_elemento.pack()

def Saludo():
    texto_elemento_dinamico = Label(ventana, text="Texto creado por el boton")
    texto_elemento_dinamico.pack()

boton_elemento = Button(ventana, text="Presioname", command=Saludo)
boton_elemento.pack()

ventana.mainloop()