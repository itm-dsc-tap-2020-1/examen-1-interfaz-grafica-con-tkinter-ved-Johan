import tkinter as tk
from tkinter import ttk
from tkinter import Menu   
from tkinter import messagebox as mbo

def im():
    a=0
    if(p1.get().lower()=="equilatero"):
        a=a+20
    if(p2.get().lower()=="isoceles"):
        a=a+20
    if(opcion_4.get()==1):
        a=a+20
    if(opcion_5.get()==2):
        a=a+20
    if((opcion_1.get()!=1 and opcion_7.get()!=1 and opcion_3.get()!=1) and (opcion_6.get()==1 or opcion_2.get()==1)):
        a=a+20
    mbo.showinfo("Calificacion","Calificacion: "+str(a))

ventana=tk.Tk()
ventana.title("Examen")

ttk.Label(ventana, text="1.-Triangulo con todos los lados iguales").grid(column=0,row=0)
p1=tk.StringVar()
p1c=ttk.Entry(ventana, width=12, textvariable=p1)
p1c.grid(column=0,row=1)

ttk.Label(ventana, text="2.-Triangulo con 2 lados iguales").grid(column=0,row=2)
p2=tk.StringVar()
p2c=ttk.Entry(ventana, width=12, textvariable=p2)
p2c.grid(column=0,row=3)

ttk.Label(ventana, text="3.-Seno").grid(column=0,row=4)
opcion_4=tk.IntVar()
radio1=tk.Radiobutton(ventana, text="cateto opuesto/hipotenusa", variable=opcion_4,value=1)
radio1.grid(column=0,row=5)
radio2=tk.Radiobutton(ventana, text="cateto adyacente/hipotenusa", variable=opcion_4,value=2)
radio2.grid(column=1,row=5)
radio3=tk.Radiobutton(ventana, text="cateto opuesto/cateto adyacente", variable=opcion_4,value=3)
radio3.grid(column=2,row=5)


ttk.Label(ventana, text="4.-Coseno").grid(column=0,row=6)
opcion_5=tk.IntVar()
radio4=tk.Radiobutton(ventana, text="cateto opuesto/hipotenusa", variable=opcion_5,value=1)
radio4.grid(column=0,row=7)
radio5=tk.Radiobutton(ventana, text="cateto adyacente/hipotenusa", variable=opcion_5,value=2)
radio5.grid(column=1,row=7)
radio5=tk.Radiobutton(ventana, text="cateto opuesto/cateto adyacente", variable=opcion_5,value=3)
radio5.grid(column=2,row=7)

ttk.Label(ventana, text="5.-Funcion Trigonometrica").grid(column=0,row=8)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(ventana,text="x^2",variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0,row=9)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(ventana,text="sen(x)",variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1,row=9)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(ventana,text="x+1",variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2,row=9)
opcion_6=tk.IntVar()
casilla_6=tk.Checkbutton(ventana,text="sec(x)",variable=opcion_6)
casilla_6.deselect()
casilla_6.grid(column=3,row=9)
opcion_7=tk.IntVar()
casilla_5=tk.Checkbutton(ventana,text="ln(x)",variable=opcion_7)
casilla_5.deselect()
casilla_5.grid(column=4,row=9)

pkkmn=ttk.Button(ventana,text="Calificar",command=im)
pkkmn.grid(column=0,row=10)

ventana.mainloop()
