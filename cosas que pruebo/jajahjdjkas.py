import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_dias_que_viviste():
    try:
        fecha_nacimiento_str = entrada_fecha_nacimiento.get()  # Obtiene la fecha de la entrada
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        fecha_actual = datetime.now()
        diferencia = fecha_actual - fecha_nacimiento
        dias_que_viviste = diferencia.days
        resultado_var.set(f"Has vivido {dias_que_viviste} días.")  # Actualiza la etiqueta de resultado
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha inválido. Por favor, usa el formato dd/mm/aaaa.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Días Vividos")

# Variable para actualizar el resultado
resultado_var = tk.StringVar()

# Creación de widgets
etiqueta_instruccion = tk.Label(ventana, text="Ingresa tu fecha de nacimiento (dd/mm/aaaa):")
entrada_fecha_nacimiento = tk.Entry(ventana)
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_dias_que_viviste)
etiqueta_resultado = tk.Label(ventana, textvariable=resultado_var)

# Organizar los widgets en la ventana
etiqueta_instruccion.pack()
entrada_fecha_nacimiento.pack()
boton_calcular.pack()
etiqueta_resultado.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
