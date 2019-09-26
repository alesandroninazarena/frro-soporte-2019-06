from ejercicio_01 import Socio
from capa_negocio import NegocioSocio
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mbox



class PresentacionSocios:

    def __init__(self, parent, cn_socio):
        self.parent = parent
        self.cn_socio = cn_socio
        self.tree = ttk.Treeview(parent, selectmode=tk.BROWSE)
        self.tree = ttk.Treeview(parent, columns=('#1', '#2', '#3'))
        self.tree.heading('#0', text='Id')
        self.tree.heading('#1', text='Nombre')
        self.tree.heading('#2', text='Apellido')
        self.tree.heading('#3', text='DNI')
        self.btAlta = Button(parent, text='Alta', command=lambda: self.altaSocio())
        self.btBaja = Button(parent, text='Baja', command=lambda: self.bajaSocio())
        self.btAct = Button(parent, text='Actualizar', command=lambda: self.actualizarSocio())
        self.tree.grid(column=0, row=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.btAlta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        self.btBaja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
        self.btAct.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)
        self.refresh()


    def refresh(self):
        for c in self.tree.get_children():
            self.tree.delete(c)
        for ls in cn_socio.todos():
            self.tree.insert('', END, text=ls.id, values=(ls.nombre, ls.apellido, ls.dni))


    def altaSocio(self):
        AMForm(self.parent, self.refresh(), self.cn_socio)
        self.refresh()


    def bajaSocio(self):
        item_id = self.tree.focus()
        if item_id:
            baja = mbox.askyesno('Confirmación Baja de Socio', '¿Realmente desea dar de baja?', default='no', parent=self.parent)
            if baja:
                id = self.tree.item(item_id, 'text')
                self.cn_socio.baja(id)
                self.refresh()


    def actualizarSocio(self):
        item_id = self.tree.focus()
        id = self.tree.item(item_id, 'text')
        AMForm(self.parent, self.refresh(), self.cn_socio, self.cn_socio.buscar(id))
        self.refresh()


class AMForm:

    def __init__(self, parent, callback, cn_socio, socio=None):

        self.callback = callback
        self.cn_socio = cn_socio

        self.vent = Toplevel()
        self.vent.transient(master=parent)

        labNom = Label(self.vent, text='Nombre:')
        labAp = Label(self.vent, text='Apellido:')
        labDni = Label(self.vent, text='DNI:')

        self.id = IntVar(value=getattr(socio, 'id', 0))
        self.nombre = StringVar(value=getattr(socio, 'nombre', ''))
        self.apellido = StringVar(value=getattr(socio, 'apellido', ''))
        self.dni = IntVar(value=getattr(socio, 'dni', 0))

        enNom = Entry(self.vent, textvariable=self.nombre)
        enAp = Entry(self.vent, textvariable=self.apellido)
        enDni = Entry(self.vent, textvariable=self.dni)

        botAcep = Button(self.vent, text='Aceptar', command=lambda: self.aceptar())

        self.accion = self.modif if socio else self.alta

        labNom.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        labAp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
        labDni.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)
        enNom.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
        enAp.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
        enDni.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
        botAcep.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
        self.callback


    def aceptar(self):
        self.accion()
        self.callback
        self.vent.destroy()


    def alta(self):
        self.cn_socio.alta(Socio(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get()))
        self.callback


    def modif(self):
        self.cn_socio.modificacion(Socio(id=self.id.get(), nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get()))
        self.callback



if __name__ == '__main__':
    parent = tk.Tk()
    parent.title('Gestión de Socios')
    parent.marco = ttk.Frame(parent, borderwidth=1, relief='raised', padding=(10,10))
    parent.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    cn_socio = NegocioSocio()
    PresentacionSocios(parent.marco, cn_socio)
    parent.mainloop()

