#Al Formulario del Ejercicio 3,  agregue  los siguientes botones
# 1- un  botón  Alta que inicia otra ventana donde puedo ingresar una ciudad y su código postal.
# 2- un botón Baja que borra del listado de ciudades la ciudad que esta selecionada en Treeview.
# 3- un botón Modificar.
#Todos los cambios se deben ver reflejados en la lista que se muestra.


import tkinter
from tkinter import *
from tkinter import ttk


def Alta():
    root = tkinter.Tk()
    root.title('Nueva Ciudad')
    root.marco = ttk.Frame(root, borderwidth=2, relief='raised', padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
    root.ciudad = StringVar()
    root.codigo = StringVar()
    root.labCiu = Label(root.marco, text='Ciudad:')
    root.labCod = Label(root.marco, text='Código Postal:')
    root.enCiu = ttk.Entry(root.marco, textvariable=root.ciudad)
    root.enCod = ttk.Entry(root.marco, textvariable=root.codigo)
    root.botAceptar = ttk.Button(root.marco, text='Aceptar', command=lambda: CargarDatos(root))
    root.labCiu.grid(column=0, row=1, sticky='ew', padx=5, pady=5)
    root.labCod.grid(column=0, row=2, sticky='ew', padx=5, pady=5)
    root.enCiu.grid(column=1, row=1, sticky='ew', padx=5, pady=5)
    root.enCod.grid(column=1, row=2, sticky='ew', padx=5, pady=5)
    root.botAceptar.grid(column=1, row=3, sticky='ew', padx=5, pady=5)

def CargarDatos(root):
    app.treeview.insert('', 'end', text=root.enCiu.get(), values=root.enCod.get())
    root.destroy()

def Baja():
    i = app.treeview.focus()
    app.treeview.delete(i)

def Modificar():
    root = tkinter.Tk()
    root.title('Modificar Código Postal')
    root.marco = ttk.Frame(root, borderwidth=2, relief='raised', padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
    root.codigo = StringVar()
    root.labCod = Label(root.marco, text='Codigo Postal:')
    root.enCod = ttk.Entry(root.marco, textvariable=root.codigo)
    root.botAceptar = ttk.Button(root.marco, text='Aceptar', command=lambda: Editar(root))
    root.labCod.grid(column=0, row=1, sticky='ew', padx=5, pady=5)
    root.enCod.grid(column=1, row=1, sticky='ew', padx=5, pady=5)
    root.botAceptar.grid(column=1, row=2, sticky='ew', padx=5, pady=5)

def Editar(root):
    i = app.treeview.focus()
    app.treeview.item(i, values=root.enCod.get())
    root.destroy()

def InsertarDatos(treeview):
        ciudades = ['Rosario', 'Buenos Aires', 'Pergamino', 'Cordoba', 'Basavilbaso']
        codigos = ['2000', '1000', '2700', '5284', '3170']
        for i in range(0, 5):
            treeview.insert('', 'end', text=ciudades[i], values=codigos[i])


app = tkinter.Tk()
app.title('Ciudades Argentinas')
app.marco = ttk.Frame(app, borderwidth=2, relief='raised', padding=(10,10))
app.marco.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
app.treeview = ttk.Treeview(app.marco, selectmode=tkinter.BROWSE)
app.treeview = ttk.Treeview(app.marco, columns='#1')
app.treeview.heading("#0", text='Ciudad')
app.treeview.heading('#1', text='Código Postal')
InsertarDatos(app.treeview)
app.btAlta=Button(app.marco, text='Alta', command=Alta)
app.btBaja=Button(app.marco, text='Baja', command=Baja)
app.btModif=Button(app.marco, text='Modificar', command=Modificar)
app.treeview.grid(column=0, row=0, sticky="ew",columnspan=3, padx=5, pady=5)
app.btAlta.grid(column=0, row=1, sticky="ew", padx=5, pady=5)
app.btBaja.grid(column=1, row=1, sticky="ew", padx=5, pady=5)
app.btModif.grid(column=2, row=1, sticky="ew", padx=5, pady=5)
app.mainloop()

