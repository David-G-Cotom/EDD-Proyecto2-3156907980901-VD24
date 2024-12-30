from tkinter import Tk, Menu, filedialog, Frame, Label, Entry, Button, StringVar, IntVar, DoubleVar, messagebox
from ..BackEnd.controllers.FileControl import FileControl
from ..BackEnd.ArbolB.ArbolB import ArbolB
from ..BackEnd.ArbolB.ReporteArbolB import ReporteArbolB
from ..BackEnd.ListaCircularDobleEnlazada.ListaClientes import ListaClientes
from ..BackEnd.ListaCircularDobleEnlazada.ReporteListaDoble import ReporteListaDoble
from ..BackEnd.Grafo.ListaAdyacencia import ListaAdyacencia
from ..BackEnd.Grafo.ReporteGrafo import ReporteGrafo
from ..BackEnd.models.Cliente import Cliente
from ..BackEnd.models.Vehiculo import Vehiculo

class InterfazPrincipal:
    def __init__(self):
        pass



def __limpiar_formulario():
    for widget in frame_formulario.winfo_children():
        widget.destroy()



#---------------------------------------- VARIABLES GLOBALES ----------------------------------------#
arbol_vehiculos: ArbolB = ArbolB(5)
reporte_arbol_b: ReporteArbolB = ReporteArbolB(arbol_vehiculos)
lista_clientes: ListaClientes = ListaClientes()
reporte_lista_doble: ReporteListaDoble = ReporteListaDoble(lista_clientes)
lista_adyacente: ListaAdyacencia = ListaAdyacencia()
reporte_grafo: ReporteGrafo = ReporteGrafo(lista_adyacente)

ventana = Tk()
ventana.title("Titulo de Prueba")
ventana.geometry("1200x800")
menu_barra = Menu(ventana, tearoff=0)

#---------------------------------------- CARGA DE ARCHIVOS ----------------------------------------#
def __cargar_archivo(tipo_archivo: int):
    controlador_archivos: FileControl = FileControl()
    file = filedialog.askopenfilename(title="Selecciona un archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    if file:
        try:
            with open(file, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if tipo_archivo == 1: controlador_archivos.procesar_clientes(contenido, lista_clientes)
                elif tipo_archivo == 2: controlador_archivos.procesar_vehiculos(contenido, arbol_vehiculos)
                elif tipo_archivo == 3: controlador_archivos.procesar_rutas(contenido, lista_adyacente)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")



menu_datos = Menu(menu_barra, tearoff=0)
menu_datos.add_command(label="Clientes", command=lambda: __cargar_archivo(1))
menu_datos.add_separator()
menu_datos.add_command(label="Vehiculos", command=lambda: __cargar_archivo(2))
menu_datos.add_separator()
menu_datos.add_command(label="Rutas", command=lambda: __cargar_archivo(3))
menu_barra.add_cascade(label="Carga de Datos", menu=menu_datos)





#---------------------------------------- MENU DEL CLIENTE ----------------------------------------#
def __formulario_agregar_cliente():
    __limpiar_formulario()
    Label(frame_formulario, text="FORMULARIO PARA CREACION DE CLIENTE", foreground="red").grid(row=0, columnspan=2, padx=5, pady=5)
    Label(frame_formulario, text="DPI: ").grid(row=1, column=0, padx=5, pady=5)
    dpi = IntVar()
    dpi_entry = Entry(frame_formulario, textvariable=dpi)
    dpi_entry.grid(row=1, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Nombre:").grid(row=2, column=0, padx=5, pady=5)
    nombre = StringVar()
    nombre_entry: Entry = Entry(frame_formulario, textvariable=nombre)
    nombre_entry.grid(row=2, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Apellidos: ").grid(row=3, column=0, padx=5, pady=5)
    apellidos = StringVar()
    apellidos_entry = Entry(frame_formulario, textvariable=apellidos)
    apellidos_entry.grid(row=3, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Genero:").grid(row=4, column=0, padx=5, pady=5)
    genero = StringVar()
    genero_entry = Entry(frame_formulario, textvariable=genero)
    genero_entry.grid(row=4, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Telefono: ").grid(row=5, column=0, padx=5, pady=5)
    telefono = IntVar()
    telefono_entry = Entry(frame_formulario, textvariable=telefono)
    telefono_entry.grid(row=5, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Direccion:").grid(row=6, column=0, padx=5, pady=5)
    direccion = StringVar()
    direccion_entry = Entry(frame_formulario, textvariable=direccion)
    direccion_entry.grid(row=6, column=1, padx=5, pady=5)
    Button(frame_formulario, text="Registrar", command=lambda: __procesar_agregar_cliente(dpi.get(), nombre.get(), apellidos.get(), genero.get(), telefono.get(), direccion.get())).grid(row=7, columnspan=3, pady=10)

def __procesar_agregar_cliente(dpi: int, nombre: str, apellidos: str, genero: str, telefono: int, direccion: str):
    nuevo_cliente: Cliente = Cliente(dpi, nombre, apellidos, genero, telefono, direccion)
    lista_clientes.insertar_cliente(nuevo_cliente)
    messagebox.showinfo("EXITO!!!", "Nuevo Cliente Registrado en el Sistema")
    __limpiar_formulario()



def __formulario_modificar_cliente():
    __limpiar_formulario()
    if lista_clientes.mostrar_lista(frame_formulario):
        Label(frame_formulario, text="FORMULARIO PARA MODIFICACION DE CLIENTE", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
        Label(frame_formulario, text="DPI: ").grid(row=2, column=0, padx=5, pady=5)
        dpi = IntVar()
        dpi_entry = Entry(frame_formulario, textvariable=dpi)
        dpi_entry.grid(row=2, column=1, padx=5, pady=5)
        Label(frame_formulario, text="Nombre:").grid(row=3, column=0, padx=5, pady=5)
        nombre = StringVar()
        nombre_entry: Entry = Entry(frame_formulario, textvariable=nombre)
        nombre_entry.grid(row=3, column=1, padx=5, pady=5)
        Label(frame_formulario, text="Apellidos: ").grid(row=4, column=0, padx=5, pady=5)
        apellidos = StringVar()
        apellidos_entry = Entry(frame_formulario, textvariable=apellidos)
        apellidos_entry.grid(row=4, column=1, padx=5, pady=5)
        Label(frame_formulario, text="Genero:").grid(row=5, column=0, padx=5, pady=5)
        genero = StringVar()
        genero_entry = Entry(frame_formulario, textvariable=genero)
        genero_entry.grid(row=5, column=1, padx=5, pady=5)
        Label(frame_formulario, text="Telefono: ").grid(row=6, column=0, padx=5, pady=5)
        telefono = IntVar()
        telefono_entry = Entry(frame_formulario, textvariable=telefono)
        telefono_entry.grid(row=6, column=1, padx=5, pady=5)
        Label(frame_formulario, text="Direccion:").grid(row=7, column=0, padx=5, pady=5)
        direccion = StringVar()
        direccion_entry = Entry(frame_formulario, textvariable=direccion)
        direccion_entry.grid(row=7, column=1, padx=5, pady=5)
        Button(frame_formulario, text="Modificar", command=lambda: __procesar_modificar_cliente(dpi.get(), nombre.get(), apellidos.get(), genero.get(), telefono.get(), direccion.get())).grid(row=8, columnspan=3, pady=10)

def __procesar_modificar_cliente(dpi: int, nombre: str, apellidos: str, genero: str, telefono: int, direccion: str):
    cliente_modificado: Cliente = Cliente(dpi, nombre, apellidos, genero, telefono, direccion)
    lista_clientes.modificar_cliente(cliente_modificado)
    __limpiar_formulario()



def __formulario_eliminar_cliente():
    __limpiar_formulario()
    if lista_clientes.mostrar_lista(frame_formulario):
        Label(frame_formulario, text="FORMULARIO PARA ELIMINACION DE CLIENTE", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
        Label(frame_formulario, text="DPI: ").grid(row=2, column=0, padx=5, pady=5)
        dpi = IntVar()
        dpi_entry = Entry(frame_formulario, textvariable=dpi)
        dpi_entry.grid(row=2, column=1, padx=5, pady=5)
        Button(frame_formulario, text="Eliminar", command=lambda: __procesar_eliminar_cliente(dpi.get())).grid(row=3, columnspan=3, pady=10)

def __procesar_eliminar_cliente(dpi: int):
    lista_clientes.eliminar_cliente(dpi)
    __limpiar_formulario()



def __formulario_mostrar_informacion_cliente():
    __limpiar_formulario()
    if lista_clientes.mostrar_dpis(frame_formulario):
        Label(frame_formulario, text="FORMULARIO PARA MOSTRAR INFORMACION DE CLIENTE", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
        Button(frame_formulario, text="Mostrar Informacion", command=lambda: __procesar_mostrar_informacion_cliente()).grid(row=2, columnspan=3, pady=10)

def __procesar_mostrar_informacion_cliente():
    lista_clientes.mostrar_informacion()



menu_cliente = Menu(menu_barra, tearoff=0)
menu_cliente.add_command(label="Agregar/Crear", command=__formulario_agregar_cliente)
menu_cliente.add_separator()
menu_cliente.add_command(label="Modificar", command=__formulario_modificar_cliente)
menu_cliente.add_separator()
menu_cliente.add_command(label="Eliminar", command=__formulario_eliminar_cliente)
menu_cliente.add_separator()
menu_cliente.add_command(label="Mostrar Informacion", command=__formulario_mostrar_informacion_cliente)
menu_cliente.add_separator()
menu_cliente.add_command(label="Mostrar Estructura de Datos", command=lambda: reporte_lista_doble.generar_reporte(frame_formulario))
menu_barra.add_cascade(label="Cliente", menu=menu_cliente)





#---------------------------------------- MENU DE VEHICULO ----------------------------------------#
def __formulario_agregar_vehiculo():
    __limpiar_formulario()
    Label(frame_formulario, text="FORMULARIO PARA CREACION DE VEHICULO", foreground="red").grid(row=0, columnspan=2, padx=5, pady=5)
    Label(frame_formulario, text="Placa: ").grid(row=1, column=0, padx=5, pady=5)
    placa = StringVar()
    placa_entry = Entry(frame_formulario, textvariable=placa)
    placa_entry.grid(row=1, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Marca:").grid(row=2, column=0, padx=5, pady=5)
    marca = StringVar()
    marca_entry = Entry(frame_formulario, textvariable=marca)
    marca_entry.grid(row=2, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Modelo: ").grid(row=3, column=0, padx=5, pady=5)
    modelo = IntVar()
    modelo_entry = Entry(frame_formulario, textvariable=modelo)
    modelo_entry.grid(row=3, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Precio:").grid(row=4, column=0, padx=5, pady=5)
    precio = DoubleVar()
    precio_entry = Entry(frame_formulario, textvariable=precio)
    precio_entry.grid(row=4, column=1, padx=5, pady=5)
    Button(frame_formulario, text="Registrar", command=lambda: __procesar_agregar_vehiculo(placa.get(), marca.get(), modelo.get(), precio.get())).grid(row=5, columnspan=3, pady=10)

def __procesar_agregar_vehiculo(placa: str, marca: str, modelo: int, precio: float):
    nuevo_vehiculo: Vehiculo = Vehiculo(placa, marca, modelo, precio)
    arbol_vehiculos.insertar_vehiculo(nuevo_vehiculo)
    messagebox.showinfo("EXITO!!!", "Nuevo Vehiculo Registrado en el Sistema")
    __limpiar_formulario()



def __formulario_modificar_vehiculo():
    __limpiar_formulario()
    arbol_vehiculos.recorrer_arbol(frame_formulario)
    Label(frame_formulario, text="FORMULARIO PARA MODIFICACION DE VEHICULO", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
    Label(frame_formulario, text="Placa: ").grid(row=2, column=0, padx=5, pady=5)
    placa = StringVar()
    placa_entry = Entry(frame_formulario, textvariable=placa)
    placa_entry.grid(row=2, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Marca:").grid(row=3, column=0, padx=5, pady=5)
    marca = StringVar()
    marca_entry = Entry(frame_formulario, textvariable=marca)
    marca_entry.grid(row=3, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Modelo: ").grid(row=4, column=0, padx=5, pady=5)
    modelo = IntVar()
    modelo_entry = Entry(frame_formulario, textvariable=modelo)
    modelo_entry.grid(row=4, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Precio:").grid(row=5, column=0, padx=5, pady=5)
    precio = DoubleVar()
    precio_entry = Entry(frame_formulario, textvariable=precio)
    precio_entry.grid(row=5, column=1, padx=5, pady=5)
    Button(frame_formulario, text="Modificar", command=lambda: __procesar_modificar_vehiculo(placa.get(), marca.get(), modelo.get(), precio.get())).grid(row=6, columnspan=3, pady=10)

def __procesar_modificar_vehiculo(placa: str, marca: str, modelo: int, precio: float):
    vehiculo_modificado: Vehiculo = Vehiculo(placa, marca, modelo, precio)
    arbol_vehiculos.modificar_vehiculo(vehiculo_modificado)
    __limpiar_formulario()



def __formulario_eliminar_vehiculo():
    __limpiar_formulario()
    arbol_vehiculos.recorrer_arbol(frame_formulario)
    Label(frame_formulario, text="FORMULARIO PARA ELIMINACION DE VEHICULO", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
    Label(frame_formulario, text="Placa: ").grid(row=2, column=0, padx=5, pady=5)
    placa = StringVar()
    placa_entry = Entry(frame_formulario, textvariable=placa)
    placa_entry.grid(row=2, column=1, padx=5, pady=5)
    Button(frame_formulario, text="Eliminar", command=lambda: __procesar_eliminar_vehiculo(placa)).grid(row=3, columnspan=3, pady=10)

def __procesar_eliminar_vehiculo(placa: str):
    vehiculo_eliminar: Vehiculo = Vehiculo(placa, "", 0, 0)
    arbol_vehiculos.eliminar_vehiculo(arbol_vehiculos.get_raiz(), vehiculo_eliminar)
    __limpiar_formulario()



def __formulario_mostrar_informacion_vehiculo():
    __limpiar_formulario()
    arbol_vehiculos.mostrar_placas(frame_formulario)
    Label(frame_formulario, text="FORMULARIO PARA MOSTRAR INFORMACION DE VEHICULO", foreground="red").grid(row=1, columnspan=2, padx=5, pady=5)
    Button(frame_formulario, text="Mostrar Informacion", command=lambda: __procesar_mostrar_informacion_vehiculo()).grid(row=2, columnspan=3, pady=10)

def __procesar_mostrar_informacion_vehiculo():
    arbol_vehiculos.mostrar_informacion()



menu_vehiculo = Menu(menu_barra, tearoff=0)
menu_vehiculo.add_command(label="Agregar/Crear", command=__formulario_agregar_vehiculo)
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Modificar", command=__formulario_modificar_vehiculo)
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Eliminar", command=__formulario_eliminar_vehiculo)
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Mostrar Informacion", command=__formulario_mostrar_informacion_vehiculo)
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Mostrar Estructura de Datos", command=lambda: reporte_arbol_b.generar_reporte(frame_formulario))
menu_barra.add_cascade(label="Vehiculo", menu=menu_vehiculo)





#---------------------------------------- MENU DE VIAJES ----------------------------------------#
def __formulario_agregar_viaje():
    __limpiar_formulario()
    Label(frame_formulario, text="FORMULARIO PARA CREACION DE VIAJE", foreground="red").grid(row=0, columnspan=2, padx=5, pady=5)
    Label(frame_formulario, text="Lugar de Origen: ").grid(row=1, column=0, padx=5, pady=5)
    origen = StringVar()
    origen_entry = Entry(frame_formulario, textvariable=origen)
    origen_entry.grid(row=1, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Lugar de Destino:").grid(row=2, column=0, padx=5, pady=5)
    destino = StringVar()
    destino_entry = Entry(frame_formulario, textvariable=destino)
    destino_entry.grid(row=2, column=1, padx=5, pady=5)
    Label(frame_formulario, text="DPI Cliente:").grid(row=3, column=0, padx=5, pady=5)
    dpi = IntVar()
    dpi_entry = Entry(frame_formulario, textvariable=dpi)
    dpi_entry.grid(row=3, column=1, padx=5, pady=5)
    Label(frame_formulario, text="Placa Vehiculo:").grid(row=4, column=0, padx=5, pady=5)
    placa = StringVar()
    placa_entry = Entry(frame_formulario, textvariable=placa)
    placa_entry.grid(row=4, column=1, padx=5, pady=5)
    Button(frame_formulario, text="Enviar", command=lambda: __procesar_agregar_viaje(origen.get(), destino.get(), dpi.get(), placa.get())).grid(row=5, columnspan=3, pady=10)
    #SE DEBE MOSTRAR EL VIAJE EN GRAPHIZ
    #ELIMINAR LA OPCION DE MOSTRAR ESTRUCTURA DE DATOS

def __procesar_agregar_viaje(origen: str, destino: str, doi: int, placa: str):
    pass



menu_viaje = Menu(menu_barra, tearoff=0)
menu_viaje.add_command(label="Agregar/Crear", command=__formulario_agregar_viaje)
menu_barra.add_cascade(label="Viaje", menu=menu_viaje)





#---------------------------------------- MENU DE RUTAS ----------------------------------------#
menu_ruta = Menu(menu_barra, tearoff=0)
menu_ruta.add_command(label="Mostrar Estructura de Datos", command=lambda: reporte_grafo.generar_reporte(frame_formulario))
menu_barra.add_cascade(label="Ruta", menu=menu_ruta)

#---------------------------------------- REPORTES ----------------------------------------#
menu_reporte = Menu(menu_barra, tearoff=0)
menu_reporte.add_command(label="Top Viajes")
menu_reporte.add_separator()
menu_reporte.add_command(label="Top Ganancias")
menu_reporte.add_separator()
menu_reporte.add_command(label="Top Clientes")
menu_reporte.add_separator()
menu_reporte.add_command(label="Top Vehiculos")
menu_reporte.add_separator()
menu_reporte.add_command(label="Ruta de un Viaje")
menu_barra.add_cascade(label="Reportes", menu=menu_reporte)

#---------------------------------------- RENDERIZACION ----------------------------------------#
frame_formulario = Frame(ventana)
frame_formulario.pack(pady=20)
ventana.config(menu=menu_barra)

ventana.mainloop()