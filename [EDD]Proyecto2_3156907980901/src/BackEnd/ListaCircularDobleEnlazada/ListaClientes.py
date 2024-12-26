from .NodoListaDoble import NodoListaDoble
from ..models.Cliente import Cliente
from tkinter import Frame, messagebox, ttk, Label

class ListaClientes:
    def __init__(self):
        self.__inicio: NodoListaDoble = None
        self.__fin: NodoListaDoble = None



    def get_inicio(self) -> NodoListaDoble:
        return self.__inicio

    def set_inicio(self, inicio: NodoListaDoble) -> None:
        self.__inicio = inicio

    

    def get_fin(self) -> NodoListaDoble:
        return self.__fin
    
    def set_fin(self, fin: NodoListaDoble) -> None:
        self.__fin = fin



    def __insertar_inicio(self, nodo: NodoListaDoble) -> None:
        nodo.set_siguiente(self.__inicio)
        nodo.set_anterior(self.__inicio.get_anterior())
        self.__inicio.get_anterior().set_siguiente(nodo)
        self.__inicio.set_anterior(nodo)
        self.__inicio = nodo



    def __insertar_medio(self, nodo: NodoListaDoble, nodo_siguiente: NodoListaDoble) -> None:
        nodo.set_siguiente(nodo_siguiente)
        nodo.set_anterior(nodo_siguiente.get_anterior())
        nodo_siguiente.get_anterior().set_siguiente(nodo)
        nodo_siguiente.set_anterior(nodo)



    def __insertar_final(self, nodo: NodoListaDoble) -> None:
        nodo.set_anterior(self.__fin)
        nodo.set_siguiente(self.__fin.get_siguiente())
        self.__fin.get_siguiente().set_anterior(nodo)
        self.__fin.set_siguiente(nodo)
        self.__fin = nodo



    def insertar_cliente(self, cliente: Cliente) -> None:
        nodo_nuevo: NodoListaDoble = NodoListaDoble(cliente)
        if not self.is_vacia():
            nodo_aux: NodoListaDoble = self.__inicio
            if nodo_aux == self.__inicio and nodo_aux == self.__fin:
                if nodo_nuevo.get_cliente().get_dpi() > nodo_aux.get_cliente().get_dpi():
                    self.__insertar_final(nodo_nuevo)
                else:
                    self.__insertar_inicio(nodo_nuevo)
            else:
                while nodo_aux != self.__fin:
                    if nodo_nuevo.get_cliente().get_dpi() > nodo_aux.get_cliente().get_dpi() and nodo_nuevo.get_cliente().get_dpi() < nodo_aux.get_cliente().get_dpi():
                        self.__insertar_medio(nodo_nuevo, nodo_aux.get_siguiente())
                        print("NUEVO CLIENTE REGISTRADO!!!")
                        return
                    
                    if nodo_nuevo.get_cliente().get_dpi() < nodo_aux.get_cliente().get_dpi():
                        self.__insertar_inicio(nodo_nuevo)
                        print("NUEVO CLIENTE REGISTRADO!!!")
                        return
                    
                    nodo_aux = nodo_aux.get_siguiente()
                self.__insertar_final(nodo_nuevo)
        else:
            nodo_nuevo.set_siguiente(nodo_nuevo)
            nodo_nuevo.set_anterior(nodo_nuevo)
            self.__inicio = self.__fin = nodo_nuevo
        print("NUEVO CLIENTE REGISTRADO!!!")



    def modificar_cliente(self, cliente_modificado: Cliente) -> None:
        nodo_aux: NodoListaDoble = self.__inicio
        while True:
            if nodo_aux.get_cliente().get_dpi() == cliente_modificado.get_dpi():
                nodo_aux.get_cliente().set_nombre(cliente_modificado.get_nombre())
                nodo_aux.get_cliente().set_apellido(cliente_modificado.get_apellido())
                nodo_aux.get_cliente().set_genero(cliente_modificado.get_genero())
                nodo_aux.get_cliente().set_telefono(cliente_modificado.get_telefono())
                nodo_aux.get_cliente().set_direccion(cliente_modificado.get_direccion())
                messagebox.showinfo("EXITO!!!", "Cliente Modificado Exitosamente")
                return
            
            nodo_aux = nodo_aux.get_siguiente()
            if nodo_aux == self.__inicio: break

        messagebox.showerror("ERROR!!!", "No se Encontro al Cliente para Modificar")



    def eliminar_cliente(self, dpi: int) -> None:
        nodo_aux: NodoListaDoble = self.__inicio
        while True:
            if nodo_aux.get_cliente().get_dpi() == dpi:
                if nodo_aux == self.__inicio and nodo_aux == self.__fin:    # HAY UN CLIENTE
                    self.__inicio = self.__fin = None
                elif nodo_aux == self.__inicio:
                    if nodo_aux.get_siguiente() == self.__fin:  # HAY DOS CLIENTES
                        nodo_aux.get_siguiente().set_siguiente(nodo_aux.get_siguiente())
                        nodo_aux.get_siguiente().set_anterior(nodo_aux.get_siguiente())
                        self.__inicio = self.__fin = nodo_aux.get_siguiente()
                    else:
                        nodo_aux.get_siguiente().set_anterior(nodo_aux.get_anterior())
                        nodo_aux.get_anterior().set_siguiente(nodo_aux.get_siguiente())
                        self.__inicio = nodo_aux.get_siguiente()
                elif nodo_aux == self.__fin:
                    if nodo_aux.get_anterior() == self.__inicio:    # HAY DOS CLIENTES
                        nodo_aux.get_anterior().set_siguiente(nodo_aux.get_anterior())
                        nodo_aux.get_anterior().set_anterior(nodo_aux.get_anterior())
                        self.__inicio = self.__fin = nodo_aux.get_anterior()
                    else:
                        nodo_aux.get_anterior().set_siguiente(nodo_aux.get_siguiente())
                        nodo_aux.get_siguiente().set_anterior(nodo_aux.get_anterior())
                        self.__fin = nodo_aux.get_anterior()
                else:   # SE ELIMINA UN NODO DE EN MEDIO
                    nodo_aux.get_siguiente().set_anterior(nodo_aux.get_anterior())
                    nodo_aux.get_anterior().set_siguiente(nodo_aux.get_siguiente())

                messagebox.showinfo("EXITO!!!", "Cliente Eliminado Exitosamente")
                return
            
            nodo_aux = nodo_aux.get_siguiente()
            if nodo_aux == self.__inicio: break

        messagebox.showerror("ERROR!!!", "No se Encontro al Cliente para Eliminar")



    def mostrar_lista(self, frame_formulario: Frame) -> bool:
        if not self.is_vacia():
            nodo_aux: NodoListaDoble = self.__inicio
            tabla = ttk.Treeview(frame_formulario, columns=("col1", "col2", "col3", "col4", "col5"))
            tabla.grid(row=0, padx=5, pady=5)
            tabla.column("#0", width=150)
            tabla.column("col1", width=150, anchor="center")
            tabla.column("col2", width=150, anchor="center")
            tabla.column("col3", width=150, anchor="center")
            tabla.column("col4", width=150, anchor="center")
            tabla.column("col5", width=150, anchor="center")
            tabla.heading("#0", text="DPI", anchor="center")
            tabla.heading("col1", text="Nombre", anchor="center")
            tabla.heading("col2", text="Apellidos", anchor="center")
            tabla.heading("col3", text="Genero", anchor="center")
            tabla.heading("col4", text="Telefono", anchor="center")
            tabla.heading("col5", text="Direccion", anchor="center")
            while True:
                tabla.insert("", "end", text=nodo_aux.get_cliente().get_dpi(), values=(nodo_aux.get_cliente().get_nombre(), nodo_aux.get_cliente().get_apellido(), nodo_aux.get_cliente().get_genero(), nodo_aux.get_cliente().get_telefono(), nodo_aux.get_cliente().get_direccion()))
                nodo_aux = nodo_aux.get_siguiente()
                if nodo_aux == self.__inicio: break
                
            return True
        
        messagebox.showwarning("CUIDADO!!!", "No hay Clientes por Mostrar")
        return False
    


    def mostrar_dpis(self, frame_formulario: Frame) -> bool:
        if not self.is_vacia():
            nodo_aux: NodoListaDoble = self.__inicio
            dpis: list[str] = []
            while True:
                dpis.append(nodo_aux.get_cliente().get_dpi().__str__())
                nodo_aux = nodo_aux.get_siguiente()
                if nodo_aux == self.__inicio: break

            self.__lista_dpis = ttk.Combobox(frame_formulario, width="20", values=dpis, state="readonly")
            self.__lista_dpis.grid(row=0, padx=5, pady=5)
            return True
        
        messagebox.showwarning("CUIDADO!!!", "No hay Clientes por Mostrar")
        return False
    


    def mostrar_informacion(self) -> None:
        if self.__lista_dpis.get() != "":
            nodo_aux: NodoListaDoble = self.__inicio
            while True:
                if nodo_aux.get_cliente().get_dpi() == int(self.__lista_dpis.get()):
                    messagebox.showinfo(f"Cliente: {self.__lista_dpis.get()}", f"""DPI: {nodo_aux.get_cliente().get_dpi()}
Nombre: {nodo_aux.get_cliente().get_nombre()}
Apellidos: {nodo_aux.get_cliente().get_apellido()}
Genero: {nodo_aux.get_cliente().get_genero()}
Telefono: {nodo_aux.get_cliente().get_telefono()}
Direccion: {nodo_aux.get_cliente().get_direccion()}""")
                    return

                nodo_aux = nodo_aux.get_siguiente()
                if nodo_aux == self.__inicio: break

            messagebox.showerror("ERROR!!!", "No se Encontro al Cliente con el DPI seleccionado")
        messagebox.showwarning("CUIDADO!!!", "Debe seleccionar un DPI valido dentro del listado")



    def is_vacia(self) -> bool:
        return self.__inicio == None