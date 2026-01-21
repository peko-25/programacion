import tkinter as tk

class Juego:
    def __init__(self):
        self.dinero = 1000
        self.escudos = 1
        self.respuesta = ""
        self.bala = 0
        self.dead = self.crear_bala()
        self.ventanas()

    def crear_bala(self):
        """Simula la creación de una bala."""
        return 3  # Solo un ejemplo, puedes modificar la lógica según tu juego.

    def verifucar_muerte(self, bala, dead):
        """Verifica si el jugador muere con la bala creada."""
        return bala == dead

    def usar_esc(self, bala, dead):
        """Si tiene escudo, lo usa y reinicia la bala a 0."""
        if self.escudos > 0:
            self.escudos -= 1
            return 0  # Resetea la bala, usando el escudo
        return bala

    def act_dine(self, bala):
        """Actualiza el dinero después de disparar."""
        self.dinero -= 100  # Ejemplo de deducción de dinero
        print(f"Dinero restante: ${self.dinero}")

    def disparar(self):
        """Función que simula el disparo al hacer clic en el botón."""
        while self.respuesta == "s":
            self.bala += 1
            if self.verifucar_muerte(self.bala, self.dead):
                print(f"¡Moriste con ${self.dinero}!")
                break
        

            self.bala = self.usar_esc(self.bala, self.dead)
            if self.bala == 0:
                self.dead = self.crear_bala()

            self.act_dine(self.bala)
            # Aquí le pides al jugador si quiere disparar nuevamente (simulado por el botón)
            print(f"¿Quieres disparar? Tienes ${self.dinero}.")
            break

        else:
            print(f"Te fuiste en la bala {self.bala} con ${self.dinero}.")
        

    def boton_disparar(self):
        """Función que ejecuta la lógica del disparo al presionar el botón."""
        self.respuesta = "s"  # Se activa la opción de disparar
        self.disparar()

    def ventanas(self):
        ventana = tk.Tk()
        ventana.title("Ruleta Rusa")
        ventana.geometry("300x200")

        # Etiqueta de dinero
        etiqueta = tk.Label(ventana, text=f"Dinero actual: ${self.dinero}")
        etiqueta.pack(pady=20)

        # Preguntar si quieres disparar
        pregunta = tk.Label(ventana, text="¿Quieres disparar?")
        pregunta.pack(pady=10)

        # Crear botón de disparo
        boton_disparar = tk.Button(ventana, text="Disparar", command=self.boton_disparar)
        boton_disparar.pack(pady=10)

        # Mostrar ventana
        ventana.mainloop()

# Crear una instancia del juego
juego = Juego()