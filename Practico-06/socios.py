from ejercicio_01 import Socio

from capa_negocio import NegocioSocio
import tkinter as tk
from tkinter import *
from tkinter import ttk

class ABMForm:

    def __init__(self, parent, cn_socio):
        self.parent= parent
        self.cn_socio= cn_socio

        self.tree = ttk.Treeview(parent, selectmode=tk.BROWSE)
        self.tree = ttk.Treeview(parent, columns= ("nom", "ape", "dni"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("nom", text="Nombre")
        self.tree.heading("ape", text="Apellido")
        self.tree.heading("dni", text="DNI")

        self.Alta= Button(parent, text="Alta", command= lambda: self.altaSocio())
        self.Baja=Button(parent, text="Baja", command=lambda: self.bajaSocio())
        self.Modif=Button(parent, text="Modificar", command= lambda:self.modifSocio())

        self.tree.grid(column=0, row=0, sticky=(E, W),columnspan=6, padx=5, pady=5)
        self.Alta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        self.Baja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
        self.Modif.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)

        self.refresh()

    def refresh(self):

        for c in self.tree.get_children():
            self.tree.delete(c)

        for s in cn_socio.todos():
            self.tree.insert("", END, text=s.id, values=(s.nombre,s.apellido, s.dni))

    def altaSocio(self):
        AltaModifForm(self.parent, self.refresh(), self.cn_socio)
        self.refresh()

    def bajaSocio(self):
        i=self.tree.focus()
        id=self.tree.item(i,"text")
        self.cn_socio.baja(id)
        self.refresh()

    def modifSocio(self):
        i=self.tree.focus()
        id=self.tree.item(i,"text")
        AltaModifForm(self.parent, self.refresh(),self.cn_socio, self.cn_socio.buscar(id))
        self.refresh()

class AltaModifForm:

    def __init__(self, parent, callback, cn_socio, socio=None):

        self.callback= callback
        self.cn_socio= cn_socio

        self.vent=Toplevel()
        self.vent.transient(master=parent)

        rotNom=Label(self.vent, text= "Nombre:")
        rotAp=Label(self.vent, text= "Apellido:")
        rotDni=Label(self.vent, text="DNI:")

        self.id=IntVar(value=getattr(socio, 'id', 0))
        self.nom= StringVar(value= getattr(socio, 'nombre', ''))
        self.ape=StringVar(value= getattr(socio, 'apellido', ''))
        self.dni=IntVar(value= getattr(socio, 'dni', 0))

        EN=Entry(self.vent, textvariable=self.nom)
        EA=Entry(self.vent, textvariable=self.ape)
        ED=Entry(self.vent, textvariable= self.dni)

        bot=Button(self.vent, text="Aceptar", command=lambda: self.aceptar())

        self.accion= self.modif if socio else self.alta

        rotNom.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
        rotAp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
        rotDni.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)

        EN.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
        EA.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
        ED.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)

        bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
        self.callback


    def aceptar(self):
        self.accion()
        self.callback
        self.vent.destroy()

    def alta(self):
        self.cn_socio.alta(Socio(nombre= self.nom.get(), apellido= self.ape.get(), dni =self.dni.get()))
        self.callback

    def modif(self):
        self.cn_socio.modificacion(Socio(id=self.id.get(), nombre= self.nom.get(),apellido= self.ape.get(),dni= self.dni.get()))


parent = tk.Tk()
parent.title("ABM Socios")
parent.marco = ttk.Frame(parent, borderwidth=1, relief="raised", padding=(10,10))

parent.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
cn_socio = NegocioSocio()

ABMForm(parent.marco, cn_socio)

parent.mainloop()
