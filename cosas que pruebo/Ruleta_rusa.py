import random
import tkinter as tk

class Ruletarussa:
    def __init__(self):
        self.max_dine = 0
        self.dinero = 110
        self.ronda = 0
        self.escudo = 0
        self.vida_extra = 0
        self.bala = 0
        self.espias = 0
        self.dead = self.crear_bala()
        self.no_disparos_consecutivos = 0
        self.muertes_por_bala = 0
        self.game_over = False

        # Referencias a widgets de Tkinter
        self.etiqueta = None
        self.escudo_label = None
        self.espia_label = None
        self.balala = None
        self.rondas = None
        self.max_diner = None
        self.status_label = None

    def comprar_escudo(self):
        if self.escudo == 5:
            self.status_label.config(text="No puedes comprar más escudos (máx. 5).")
        elif self.dinero >= 500:
            self.escudo += 1
            self.dinero -= 500
            self.actualizar_interfaz()
            self.status_label.config(text="¡Has comprado un escudo!")
        else:
            self.status_label.config(text="No tienes suficiente dinero para comprar un escudo.")

    def comprar_espia(self):
        if self.dinero >= 1000:
            self.espias += 1
            self.dinero -= 1000
            self.actualizar_interfaz()
            self.status_label.config(text="¡Has comprado un espía!")
        else:
            self.status_label.config(text="No tienes suficiente dinero para comprar un espía.")

    def comprar_vida_extra(self):
        # Costo razonable para una revivida
        if self.dinero >= 1500:
            self.vida_extra += 1
            self.dinero -= 1500
            self.actualizar_interfaz()
            self.status_label.config(text="¡Has comprado una Vida Extra!")
        else:
            self.status_label.config(text="No tienes suficiente dinero para comprar Vida Extra.")

    def usar_espia(self):
        if self.espias > 0:
            self.espias -= 1
            self.actualizar_interfaz()
            self.status_label.config(text=f"La bala mortal está en el número: {self.dead}")
        else:
            self.status_label.config(text="No tienes espías para usar.")

    def usar_vida_extra(self):
        if self.vida_extra > 0:
            self.vida_extra -= 1
            # Revive al jugador con algo de dinero para seguir jugando
            self.dinero = max(self.dinero, 100)
            self.game_over = False
            self.no_disparos_consecutivos = 0
            self.actualizar_interfaz()
            self.status_label.config(text="Has usado Vida Extra: ¡reviviste!")
        else:
            self.status_label.config(text="No tienes Vida Extra para usar.")

    def boton_disparar(self):
        self.disparar()

    def boton_no(self):
        if self.game_over:
            self.status_label.config(text="El juego terminó. Reinicia para volver a jugar.")
            return
        self.no_disparos_consecutivos += 1
        # Actualiza estado: no disparar reinicia la bala mortal y avanza la ronda
        self.status_label.config(text=f"Decidiste no disparar. Rondas sin disparar: {self.no_disparos_consecutivos}")
        self.ruleta()
        self.ronda += 1
        # Nota: Ya no se muere por 10 'no disparar'. Solo las muertes por bala cuentan hacia el final.
        self.actualizar_interfaz()

    def verificar_muerte(self):
        if self.bala == self.dead and self.escudo == 0:
            # si hay vida extra, consume y revive
            if self.vida_extra > 0:
                self.vida_extra -= 1
                self.dinero = max(self.dinero, 100)
                self.status_label.config(text="Te tocó la bala mortal pero consumiste Vida Extra: reviviste.")
                self.bala = 0
                self.dead = self.crear_bala()
                self.no_disparos_consecutivos = 0
                self.ronda += 1
                self.actualizar_interfaz()
                return False
            # Cuenta una muerte por bala
            self.muertes_por_bala += 1
            if self.dinero >= self.max_dine:
                self.max_dine = self.dinero
            self.dinero = 0
            # Si alcanzó 10 muertes por bala, terminar juego
            if self.muertes_por_bala >= 10:
                self.status_label.config(text=f"Has sido impactado por bala 10 veces. Juego terminado.")
                self.game_over = True
            else:
                self.status_label.config(text=f"¡MORISTE! Te han matado {self.muertes_por_bala}/10 veces. Puedes seguir jugando.")
                # reiniciar una nueva ronda
                self.bala = 0
                self.dead = self.crear_bala()
                self.ronda += 1
            self.actualizar_interfaz()
            return True
        return False

    def usar_escudo(self):
        if self.escudo > 0 and self.bala == self.dead:
            self.status_label.config(text="¡Salvado por el escudo!")
            self.escudo -= 1
            self.bala = 0
            self.dead = self.crear_bala()
            self.ronda += 1
            self.actualizar_interfaz()
            return True
        return False

    def crear_bala(self):
        return random.randint(1, 8)

    def actualizar_interfaz(self):
        if self.etiqueta:
            self.etiqueta.config(text=f"Dinero actual: ${self.dinero}")
        if self.escudo_label:
            self.escudo_label.config(text=f"Escudos disponibles: {self.escudo}")
        if self.espia_label:
            self.espia_label.config(text=f"Espías disponibles: {self.espias}")
        if self.balala:
            self.balala.config(text=f"Número de bala actual: {self.bala}")
        if self.rondas:
            self.rondas.config(text=f"Número de ronda: {self.ronda}")
        if self.max_diner:
            self.max_diner.config(text=f"Máximo dinero alcanzado: ${self.max_dine}")
        if self.vida_label:
            self.vida_label.config(text=f"Vidas Extra: {self.vida_extra}")
        if hasattr(self, 'muertes_label') and self.muertes_label:
            self.muertes_label.config(text=f"Muertes por bala: {self.muertes_por_bala}/10")

    def act_dine(self):
        self.dinero += 100
        self.actualizar_interfaz()

    def ruleta(self):
        self.dead = self.crear_bala()
        self.bala = 0
        self.actualizar_interfaz()

    def disparar(self):
        self.bala += 1
        self.status_label.config(text="")

        if self.usar_escudo():
            return

        if self.verificar_muerte():
            self.ruleta()
            self.ronda += 1
            return

        self.act_dine()
        self.status_label.config(text="¡Sobreviviste! Ganaste $100.")
        self.actualizar_interfaz()

    def reiniciar_juego(self):
        # Reinicia el estado del juego para volver a jugar
        self.dinero = 110
        self.ronda = 0
        self.escudo = 0
        self.vida_extra = 0
        self.espias = 0
        self.bala = 0
        self.dead = self.crear_bala()
        self.no_disparos_consecutivos = 0
        self.muertes_por_bala = 0
        self.game_over = False
        self.status_label.config(text="Juego reiniciado. ¡Buena suerte!")
        self.actualizar_interfaz()

    def ventanas(self):
        ventana = tk.Tk()
        ventana.title("Ruleta Rusa")
        ventana.geometry("500x550")

        # Bind F2 to abrir ventana de debug
        ventana.bind('<F2>', lambda e: self.abrir_debug())

        # Frame de Información
        info_frame = tk.Frame(ventana)
        info_frame.pack(pady=10)
        self.balala = tk.Label(info_frame, text=f"Número de bala actual: {self.bala}", font=("Arial", 12))
        self.balala.pack()
        self.rondas = tk.Label(info_frame, text=f"Número de ronda: {self.ronda}", font=("Arial", 12))
        self.rondas.pack()
        self.muertes_label = tk.Label(info_frame, text=f"Muertes por bala: {self.muertes_por_bala}/10", font=("Arial", 12))
        self.muertes_label.pack()
        self.etiqueta = tk.Label(info_frame, text=f"Dinero actual: ${self.dinero}", font=("Arial", 12))
        self.etiqueta.pack()
        self.max_diner = tk.Label(info_frame, text=f"Máximo dinero: ${self.max_dine}", font=("Arial", 12))
        self.max_diner.pack()

        # Frame de Acciones
        action_frame = tk.Frame(ventana)
        action_frame.pack(pady=10)
        self.disparar_btn = tk.Button(action_frame, text="Disparar", font=("Arial", 12), command=self.boton_disparar)
        self.disparar_btn.grid(row=0, column=0, padx=5)
        self.no_disparar_btn = tk.Button(action_frame, text="No Disparar", font=("Arial", 12), command=self.boton_no)
        self.no_disparar_btn.grid(row=0, column=1, padx=5)

        # Frame de Tienda
        store_frame = tk.LabelFrame(ventana, text="Tienda", padx=10, pady=10)
        store_frame.pack(pady=10, padx=10, fill="x")
        
        self.escudo_label = tk.Label(store_frame, text=f"Escudos: {self.escudo}", font=("Arial", 10))
        self.escudo_label.grid(row=0, column=0, sticky="w", padx=5)
        comprar_escudo_btn = tk.Button(store_frame, text="Comprar Escudo ($500)", command=self.comprar_escudo)
        comprar_escudo_btn.grid(row=0, column=1, padx=5)

        self.espia_label = tk.Label(store_frame, text=f"Espías: {self.espias}", font=("Arial", 10))
        self.espia_label.grid(row=1, column=0, sticky="w", padx=5)
        comprar_espia_btn = tk.Button(store_frame, text="Comprar Espía ($1000)", command=self.comprar_espia)
        comprar_espia_btn.grid(row=1, column=1, padx=5)
        
        usar_espia_btn = tk.Button(store_frame, text="Usar Espía", command=self.usar_espia)
        usar_espia_btn.grid(row=1, column=2, padx=5)

        # Vida Extra
        self.vida_label = tk.Label(store_frame, text=f"Vidas Extra: {self.vida_extra}", font=("Arial", 10))
        self.vida_label.grid(row=2, column=0, sticky="w", padx=5)
        comprar_vida_btn = tk.Button(store_frame, text="Comprar Vida Extra ($1500)", command=self.comprar_vida_extra)
        comprar_vida_btn.grid(row=2, column=1, padx=5)
        usar_vida_btn = tk.Button(store_frame, text="Usar Vida Extra", command=self.usar_vida_extra)
        usar_vida_btn.grid(row=2, column=2, padx=5)

        # Etiqueta de Estado
        self.status_label = tk.Label(ventana, text="¡Bienvenido! ¿Te atreves a jugar?", font=("Arial", 12), fg="blue")
        self.status_label.pack(pady=20)

        # Guardar referencias para deshabilitar al game over
        self.comprar_escudo_btn = comprar_escudo_btn
        self.comprar_espia_btn = comprar_espia_btn
        self.usar_espia_btn = usar_espia_btn
        self.comprar_vida_btn = comprar_vida_btn
        self.usar_vida_btn = usar_vida_btn
        # Botón reiniciar
        reiniciar_btn = tk.Button(ventana, text="Reiniciar", command=self.reiniciar_juego)
        reiniciar_btn.pack(pady=5)
        self.reiniciar_btn = reiniciar_btn

        # Actualizar interfaz al iniciar
        self.actualizar_interfaz()

        # Función periódica para chequear estado de game over y actualizar botones
        def chequeo_periodico():
            if self.game_over:
                # deshabilitar botones de acción y tienda
                self.disparar_btn.config(state="disabled")
                self.no_disparar_btn.config(state="disabled")
                self.comprar_escudo_btn.config(state="disabled")
                self.comprar_espia_btn.config(state="disabled")
                self.usar_espia_btn.config(state="disabled")
                self.comprar_vida_btn.config(state="disabled")
                # permitir usar Vida Extra si se tiene (por si se compró antes de morir)
                self.usar_vida_btn.config(state=("normal" if self.vida_extra>0 else "disabled"))
                self.reiniciar_btn.config(state="normal")
            else:
                self.disparar_btn.config(state="normal")
                self.no_disparar_btn.config(state="normal")
                self.comprar_escudo_btn.config(state="normal")
                self.comprar_espia_btn.config(state=("normal" if self.dinero>=1000 else "disabled"))
                self.usar_espia_btn.config(state=("normal" if self.espias>0 else "disabled"))
                self.comprar_vida_btn.config(state=("normal" if self.dinero>=1500 else "disabled"))
                self.usar_vida_btn.config(state=("normal" if self.vida_extra>0 else "disabled"))
                self.reiniciar_btn.config(state="disabled")
            # actualizar labels dependientes
            if self.vida_label:
                self.vida_label.config(text=f"Vidas Extra: {self.vida_extra}")
            ventana.after(500, chequeo_periodico)

        chequeo_periodico()

        ventana.mainloop()

    def abrir_debug(self):
        # Ventana pequeña para probar funciones del juego
        debug = tk.Toplevel()
        debug.title("Debug - Herramientas")
        debug.geometry("300x300")

        tk.Label(debug, text="Debug Tools", font=("Arial", 12, "bold")).pack(pady=8)

        tk.Button(debug, text="+ $1000", command=lambda: self._debug_add_money(1000)).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Forzar muerte por bala", command=self._debug_force_death).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Mostrar bala mortal", command=lambda: self._debug_show_dead(debug)).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Añadir Escudo", command=lambda: self._debug_add_item('escudo')).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Añadir Espía", command=lambda: self._debug_add_item('espia')).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Añadir Vida Extra", command=lambda: self._debug_add_item('vida')).pack(fill='x', padx=10, pady=4)
        tk.Button(debug, text="Reset Muertes por Bala", command=self._debug_reset_deaths).pack(fill='x', padx=10, pady=4)

    # Métodos internos para debug
    def _debug_add_money(self, amount):
        self.dinero += amount
        self.actualizar_interfaz()
        self.status_label.config(text=f"DEBUG: +${amount}")

    def _debug_force_death(self):
        # Forzar que bala == dead y llamar a verificar_muerte
        self.bala = self.dead
        died = self.verificar_muerte()
        if died:
            self.status_label.config(text="DEBUG: Forzado muerte por bala")
        else:
            self.status_label.config(text="DEBUG: Vida Extra consumida, reviviste")

    def _debug_show_dead(self, parent_window=None):
        msg = f"La bala mortal actual es: {self.dead}"
        self.status_label.config(text=f"DEBUG: {msg}")
        # Si la ventana de debug está abierta, mostrar un label temporal
        if parent_window:
            tk.Label(parent_window, text=msg).pack()

    def _debug_add_item(self, item):
        if item == 'escudo':
            self.escudo += 1
            self.status_label.config(text="DEBUG: +1 Escudo")
        elif item == 'espia':
            self.espias += 1
            self.status_label.config(text="DEBUG: +1 Espía")
        elif item == 'vida':
            self.vida_extra += 1
            self.status_label.config(text="DEBUG: +1 Vida Extra")
        self.actualizar_interfaz()

    def _debug_reset_deaths(self):
        self.muertes_por_bala = 0
        self.status_label.config(text="DEBUG: Muertes por bala reseteadas")
        self.actualizar_interfaz()

if __name__ == "__main__":
    juego = Ruletarussa()
    juego.ventanas()
