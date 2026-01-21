import tkinter as tk

def calcular(expresion):
    try:
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def agregar(valor):
    entrada.insert(tk.END, valor)

def borrar_todo(event=None):
    entrada.delete(0, tk.END)

def borrar_ultimo(event=None):
    entrada.delete(len(entrada.get())-1, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, width=40)
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'ESC', 'Backspace'
]

fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, command=lambda: calcular(entrada.get())).grid(row=fila, column=columna, sticky="nsew")
    elif boton == 'ESC':
        tk.Button(ventana, text=boton, command=borrar_todo).grid(row=fila, column=columna, sticky="nsew")
    elif boton == 'Backspace':
        tk.Button(ventana, text=boton, command=borrar_ultimo).grid(row=fila, column=columna, sticky="nsew")
    else:
        tk.Button(ventana, text=boton, command=lambda boton=boton: agregar(boton)).grid(row=fila, column=columna, sticky="nsew")
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

ventana.bind('<Escape>', borrar_todo)
ventana.bind('<BackSpace>', borrar_ultimo)
ventana.bind('<Return>', lambda event: calcular(entrada.get()))

ventana.mainloop()
