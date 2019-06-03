#Crear un Formulario que usando el control Treeview muestre una lista con los nombres de
#Ciudades Argentinas y su código postal (por lo menos 5 ciudades).


import tkinter
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Ciudades Argentinas")
        self.marco=ttk.Frame(self, borderwidth=2, relief="raised", padding=(10,10))
        self.tree = ttk.Treeview(self.marco, columns=('Ciudad', 'Código Postal'))
        self.tree.heading('#0', text='Id Ciudad')
        self.tree.heading('#1', text='Ciudad')
        self.tree.heading('#2', text='Código Postal')
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.treeview = self.tree
        self.insert_data()
        self.marco.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
        self.treeview.grid(row=4, columnspan=3, sticky='nsew')
        self.pack()


    def insert_data(self):
        ciudades = ['Rosario', 'Buenos Aires', 'Pergamino', 'Cordoba', 'Basavilbaso']
        codigos = ['2000', '1000', '2700', '5284', '3170']
        for i in range(0, 5):
            self.treeview.insert('', 'end', text=i+1, values=(ciudades[i], codigos[i]))



def main():
    main_window = tkinter.Tk()
    app = Application(main_window)
    app.mainloop()


if __name__ == '__main__':
    main()
