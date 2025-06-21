import tkinter as tk
"""ventana=tk.Tk()
ventana.title("Mi primera calculadora")
ventana.geometry("1200x800")

etiqueta=tk.Label(ventana,text="Escribe tu nombre:")
etiqueta.pack()

entrada=tk.Entry(ventana)
entrada.pack()

def mostrar_nombre():
    etiqueta2=tk.Label(ventana,text=f"Hola {entrada.get()}")
    etiqueta2.pack()

boton=tk.Button(ventana,text="Saludar",command=mostrar_nombre)
boton.pack()
ventana.mainloop()"""

def click(boton):
    actual=entrada.get()
    entrada.delete(0,tk.END)
    entrada.insert(0,actual+str(boton))

def limpiar():
    entrada.delete(0,tk.END)

def calcular():
    try:
        resultado=eval(entrada.get())
        entrada.delete(0,tk.END)
        entrada.insert(0,str(resultado))
    except:
        entrada.delete(0,tk.END)
        entrada.insert(0,"Error")

ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

entrada=tk.Entry(ventana,width=16,font=("Arial",24),bd=4,relief="ridge",justify="center")
entrada.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

botones=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
]

for(texto,fila,columna) in botones:
    if texto=="=":
        comando=calcular
    else:
        comando=lambda t=texto: click(t)
    tk.Button(ventana,text=texto,width=5,height=2,font=("Arial",18),command=comando).grid(row=fila,column=columna,padx=5,pady=5)
tk.Button(ventana,text="C",width=22,height=2,font=("Arial",18),command=limpiar).grid(row=5,column=0,columnspan=4,padx=5,pady=5)
ventana.mainloop()