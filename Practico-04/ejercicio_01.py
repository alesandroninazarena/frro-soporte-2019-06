#Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
#y 4 botones de operaciones para las operaciones respectivas + , - , * , /
#al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .


from tkinter import *
from tkinter import messagebox



def Suma():
    v1 = float(en1.get())
    v2 = float(en2.get())
    resultado = v1 + v2
    messagebox.showinfo("Mensaje", "El resultado  de la suma es: %.2f" %resultado)
    en1.delete(0, END)
    en2.delete(0, END)


def Resta():
    v1 = float(en1.get())
    v2 = float(en2.get())
    resultado = v1 - v2
    messagebox.showinfo("Mensaje", "El resultado de la resta es: %.2f" %resultado)
    en1.delete(0, END)
    en2.delete(0, END)


def Multiplicacion():
    v1 = float(en1.get())
    v2 = float(en2.get())
    resultado = v1 * v2
    messagebox.showinfo("Mensaje", "El resultado de la multiplicacion es: %.2f" %resultado)
    en1.delete(0, END)
    en2.delete(0, END)


def Division():
    v1 = float(en.get())
    v2 = float(en.get())
    try:
        resultado = v1 / v2
    except ZeroDivisionError:
        messagebox.showinfo("Mensaje", "Error división por cero")
    else:
        messagebox.showinfo("Mensaje", "El resultado de la divison es: %.2f" %resultado)
    finally:
        en1.delete(0, END)
        en2.delete(0, END)



calculadora = Tk()
calculadora.geometry("300x150")
calculadora.title('Calculadora')
var1 = StringVar()
var1.set('Valor Número 1')
lab1 = Label(calculadora, textvariable=var1, height=2, foreground='black')
lab1.place(x=15, y=10)
numero1 = StringVar()
en1 = Entry(calculadora, bd=3, textvariable=numero1)
en1.place(x=15, y=40)
var2 = StringVar()
var2.set('Valor Número 2')
lab2 = Label(calculadora, textvariable=var2, height=1, foreground='black')
lab2.place(x=15, y=70)
numero2 = StringVar()
en2 = Entry(calculadora, bd=3, textvariable=numero2)
en2.place(x=15, y=100)
bt1 = Button(calculadora, text="+", command=Suma, width=5)
bt1.place(x=170, y=50)
bt2 = Button(calculadora, text="-", command=Resta, width=5)
bt2.place(x=217, y=50)
bt3 = Button(calculadora, text="*", command=Multiplicacion, width=5)
bt3.place(x=170, y=80)
bt4 = Button(calculadora, text="/", command=Division, width=5)
bt4.place(x=217, y=80)
calculadora.mainloop()
