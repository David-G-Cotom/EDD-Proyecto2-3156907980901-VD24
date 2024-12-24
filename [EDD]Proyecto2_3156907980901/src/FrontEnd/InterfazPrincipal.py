from tkinter import Tk, Menu, filedialog
from ..BackEnd.controllers.FileControl import FileControl
from ..BackEnd.ArbolB.ArbolB import ArbolB
from ..BackEnd.ListaCircularDobleEnlazada.ListaClientes import ListaClientes

class InterfazPrincipal:
    def __init__(self):
        pass



arbol_vehiculos: ArbolB = ArbolB(5)
lista_clientes: ListaClientes = ListaClientes()

ventana = Tk()
ventana.title("Titulo de Prueba")
ventana.geometry("1200x800")

menu_barra = Menu(ventana, tearoff=0)

def __cargar_archivo(tipo_archivo: int):
    controlador_archivos: FileControl = FileControl()
    file = filedialog.askopenfilename(title="Selecciona un archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    if file:
        try:
            with open(file, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if tipo_archivo == 1: controlador_archivos.procesar_clientes(contenido, lista_clientes)
                elif tipo_archivo == 2: controlador_archivos.procesar_vehiculos(contenido, arbol_vehiculos)
                elif tipo_archivo == 3: controlador_archivos.procesar_rutas(contenido)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")



menu_datos = Menu(menu_barra, tearoff=0)
menu_datos.add_command(label="Clientes", command=lambda: __cargar_archivo(1))
menu_datos.add_separator()
menu_datos.add_command(label="Vehiculos", command=lambda: __cargar_archivo(2))
menu_datos.add_separator()
menu_datos.add_command(label="Rutas", command=lambda: __cargar_archivo(3))
menu_barra.add_cascade(label="Carga de Datos", menu=menu_datos)

menu_cliente = Menu(menu_barra, tearoff=0)
menu_cliente.add_command(label="Agregar/Crear")
menu_cliente.add_separator()
menu_cliente.add_command(label="Modificar")
menu_cliente.add_separator()
menu_cliente.add_command(label="Eliminar")
menu_cliente.add_separator()
menu_cliente.add_command(label="Mostrar Informacion")
menu_cliente.add_separator()
menu_cliente.add_command(label="Mostrar Estructura de Datos")
menu_barra.add_cascade(label="Cliente", menu=menu_cliente)

menu_vehiculo = Menu(menu_barra, tearoff=0)
menu_vehiculo.add_command(label="Agregar/Crear")
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Modificar")
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Eliminar")
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Mostrar Informacion")
menu_vehiculo.add_separator()
menu_vehiculo.add_command(label="Mostrar Estructura de Datos")
menu_barra.add_cascade(label="Vehiculo", menu=menu_vehiculo)

menu_viaje = Menu(menu_barra, tearoff=0)
menu_viaje.add_command(label="Agregar/Crear")
menu_viaje.add_separator()
menu_viaje.add_command(label="Mostrar Estructura de Datos")
menu_barra.add_cascade(label="Viaje", menu=menu_viaje)

menu_ruta = Menu(menu_barra, tearoff=0)
menu_ruta.add_command(label="Agregar/Crear")
menu_ruta.add_separator()
menu_ruta.add_command(label="Modificar")
menu_ruta.add_separator()
menu_ruta.add_command(label="Eliminar")
menu_ruta.add_separator()
menu_ruta.add_command(label="Mostrar Informacion")
menu_ruta.add_separator()
menu_ruta.add_command(label="Mostrar Estructura de Datos")
menu_barra.add_cascade(label="Ruta", menu=menu_ruta)

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

ventana.config(menu=menu_barra)

ventana.mainloop()