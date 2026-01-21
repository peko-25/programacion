import tkinter as tk
from tkinter import messagebox
import random
from time import time
import pyautogui
import json

class BuscaminasGUI:
    def __init__(self, filas=12, columnas=12, minas=25):
        self.historial_juego = []
        
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.minas_restantes = minas
        self.primer_click = True
        self.juego_terminado = False
        self.tiempo_inicio = 0
        self.tiempo_transcurrido = 0
        self.teclas_presionadas = {'Left': False, 'Down': False, 'Right': False}
        self.xray_activado = False
        self.autoresolviendo = False
        self.ventana_debug = None
        self.label_debug = None
        
        self.ventana = tk.Tk()
        self.ventana.title("buscaminas ☠️💀")
        
        # Configurar binds de teclado
        self.ventana.bind('<KeyPress>', self.manejar_tecla_presionada)
        self.ventana.bind('<KeyRelease>', self.manejar_tecla_liberada)
        self.ventana.bind('<F2>', self.abrir_ventana_minas)
        self.ventana.bind('<F3>', self.autosolucionar)
        self.ventana.bind('<F4>', self.autosolucionar_ia)
        
        # Panel superior
        self.panel_superior = tk.Frame(self.ventana)
        self.panel_superior.pack()
        
        self.contador_minas = tk.Label(self.panel_superior, 
                                    text=f"⛳ {self.minas_restantes}", 
                                    font=('Arial', 14, 'bold'),
                                    fg='white',
                                    bg='darkgreen')
        self.contador_minas.pack(side=tk.LEFT, padx=10)
        
        self.temporizador = tk.Label(self.panel_superior,
                                text="⏱ 0",
                                font=('Arial', 14, 'bold'),
                                fg='white',
                                bg='navy')
        self.temporizador.pack(side=tk.RIGHT, padx=10)
        
        # Tablero de juego
        self.tablero = tk.Frame(self.ventana)
        self.tablero.pack()
        
        self._setup_game() # Inicializar el juego aquí
        
    def _setup_game(self):
        """Inicializa o reinicia el estado del juego."""
        self.primer_click = True
        self.juego_terminado = False
        self.tiempo_inicio = 0
        self.tiempo_transcurrido = 0
        self.minas_restantes = self.minas
        self.minas_posiciones = set()
        self.banderas = set()
        self.autoresolviendo = False # Asegurarse de resetear esto para la IA
        
        # Limpiar y reconfigurar botones
        for widget in self.tablero.winfo_children():
            widget.destroy()
            
        self.celdas = {}
        for fila in range(self.filas):
            for columna in range(self.columnas):
                btn = tk.Button(self.tablero, 
                            text=' ', 
                            width=2, 
                            height=1,
                            font=('Arial', 12, 'bold'),
                            bg='green',
                            fg='white')
                btn.grid(row=fila, column=columna)
                btn.bind('<Button-1>', lambda e, f=fila, c=columna: self.click_izquierdo(f, c))
                btn.bind('<Button-3>', lambda e, f=fila, c=columna: self.click_derecho(f, c))
                self.celdas[(fila, columna)] = btn
        
        self.contador_minas.config(text=f"⛳ {self.minas_restantes}")
        self.temporizador.config(text="⏱ 0")
        self.actualizar_temporizador()
        
        # Cerrar ventana de debug si está abierta
        if self.ventana_debug:
            self.ventana_debug.destroy()
            self.ventana_debug = None
            self.label_debug = None
        
    def manejar_tecla_presionada(self, event):
        if event.keysym in self.teclas_presionadas:
            self.teclas_presionadas[event.keysym] = True
            self.verificar_combinacion()
            
    def manejar_tecla_liberada(self, event):
        if event.keysym in self.teclas_presionadas:
            self.teclas_presionadas[event.keysym] = False
            
    def verificar_combinacion(self):
        if all(self.teclas_presionadas.values()) and not self.primer_click and not self.juego_terminado:
            self.activar_modo_dios()
            
    def activar_modo_dios(self):
        for (fila, columna) in self.minas_posiciones:
            self.celdas[(fila, columna)].config(text='💣', bg='yellow')
        
    def actualizar_temporizador(self):
        if not self.primer_click and not self.juego_terminado:
            self.tiempo_transcurrido = int(time() - self.tiempo_inicio)
            self.temporizador.config(text=f"⏱ {self.tiempo_transcurrido}")
        self.ventana.after(1000, self.actualizar_temporizador)
        
    def generar_minas(self, fila_inicial, columna_inicial):
        self.tiempo_inicio = time()
        celdas_prohibidas = {(fila_inicial, columna_inicial)}
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = fila_inicial + dx
                y = columna_inicial + dy
                if 0 <= x < self.filas and 0 <= y < self.columnas:
                    celdas_prohibidas.add((x, y))
        
        todas_celdas = [(f, c) for f in range(self.filas) for c in range(self.columnas) 
                    if (f, c) not in celdas_prohibidas]
        self.minas_posiciones = set(random.sample(todas_celdas, self.minas))
        
    def calcular_vecinos(self, fila, columna):
        if (fila, columna) in self.minas_posiciones:
            return -1
        contador = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = fila + dx
                y = columna + dy
                if 0 <= x < self.filas and 0 <= y < self.columnas:
                    contador += (x, y) in self.minas_posiciones
        return contador
    
    def revelar_celda(self, fila, columna):
        if (fila, columna) in self.banderas:
            return
        
        vecinos = self.calcular_vecinos(fila, columna)
        
        if vecinos == -1:
            self.juego_terminado = True
            self.mostrar_minas()
            
            # Si la IA está jugando, reiniciar automáticamente sin messagebox
            if self.autoresolviendo:
                self._actualizar_debug("¡Boom! 💣 IA perdió. Reiniciando...")
                self._setup_game()
                self.ventana.after(500, self.autosolucionar_ia) # Reiniciar la IA después de un breve retraso
            else:
                # Si no es la IA, dar opción de reiniciar
                messagebox.showerror("Game Over", "¡Boom! 💣 Has pisado una mina")
                if messagebox.askyesno("Game Over", "¿Quieres intentar de nuevo?"):
                    self._setup_game()
                else:
                    self.ventana.destroy()
            return
        
        celda = self.celdas[(fila, columna)]
        color_texto = 'black' if vecinos > 0 else 'white'
        
        celda.config(text=str(vecinos) if vecinos > 0 else ' ',
                state=tk.DISABLED,
                bg='white',
                disabledforeground=color_texto)
        
        if vecinos == 0:
            self.revelar_vecinos(fila, columna)
    
    def revelar_vecinos(self, fila, columna):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = fila + dx
                y = columna + dy
                if 0 <= x < self.filas and 0 <= y < self.columnas:
                    if self.celdas[(x, y)]['state'] == tk.NORMAL:
                        self.revelar_celda(x, y)
    
    def verificar_auto_revelado(self, fila, columna):
        vecinos = self.calcular_vecinos(fila, columna)
        if vecinos <= 0:
            return
        
        banderas_contador = 0
        minas_contador = 0
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = fila + dx
                y = columna + dy
                if 0 <= x < self.filas and 0 <= y < self.columnas:
                    if (x, y) in self.banderas:
                        banderas_contador += 1
                    if (x, y) in self.minas_posiciones:
                        minas_contador += 1
        
        if banderas_contador == vecinos:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x = fila + dx
                    y = columna + dy
                    if 0 <= x < self.filas and 0 <= y < self.columnas:
                        if (x, y) not in self.banderas:
                            self.revelar_celda(x, y)
                            
            if minas_contador > 0 and banderas_contador != minas_contador:
                self.juego_terminado = True
                self.mostrar_minas()
                messagebox.showerror("Game Over", "¡Bandera incorrecta! 💥")
                self.ventana.destroy()
    
    def click_izquierdo(self, fila, columna):
        if self.juego_terminado:
            return
        
        celda = self.celdas[(fila, columna)]
        
        if self.primer_click:
            self.generar_minas(fila, columna)
            self.primer_click = False
        
        if celda['state'] == tk.DISABLED:
            self.verificar_auto_revelado(fila, columna)
            if self.juego_terminado: return # Añadido: Salir si el juego terminó
        else:
            self.revelar_celda(fila, columna)
            if self.juego_terminado: return # Añadido: Salir si el juego terminó
        
        self.verificar_victoria()
    
    def click_derecho(self, fila, columna):
        if self.juego_terminado or self.primer_click:
            return
        
        celda = self.celdas[(fila, columna)]
        
        if celda['state'] == tk.DISABLED:
            return
        
        if (fila, columna) in self.banderas:
            celda.config(text=' ', bg='green')
            self.banderas.remove((fila, columna))
            self.minas_restantes += 1
        else:
            celda.config(text='🚩', bg='darkorange')
            self.banderas.add((fila, columna))
            self.minas_restantes -= 1
        
        self.contador_minas.config(text=f"⛳ {self.minas_restantes}")
    
    def mostrar_minas(self):
        for (fila, columna) in self.minas_posiciones:
            self.celdas[(fila, columna)].config(text='💣', bg='red')
    
    def abrir_ventana_minas(self, event=None):
        self.xray_activado = not self.xray_activado
        
        if self.xray_activado:
            # Activar xray - mostrar minas
            for (fila, columna) in self.minas_posiciones:
                self.celdas[(fila, columna)].config(text='💣', bg='yellow', fg='red')
        else:
            # Desactivar xray - ocultar minas
            for (fila, columna) in self.minas_posiciones:
                if self.celdas[(fila, columna)]['state'] == tk.NORMAL:
                    self.celdas[(fila, columna)].config(text=' ', bg='green', fg='white')
    
    def autosolucionar(self, event=None):
        if self.primer_click or self.juego_terminado or self.autoresolviendo:
            return
        
        self.autoresolviendo = True
        
        # Crear ventana de debug
        self._crear_ventana_debug()
        
        # Lista de casillas a revelar (no minas)
        casillas_a_revelar = []
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if (fila, columna) not in self.minas_posiciones:
                    if self.celdas[(fila, columna)]['state'] == tk.NORMAL:
                        casillas_a_revelar.append((fila, columna))
        
        self._actualizar_debug(f"Iniciando... Casillas a revelar: {len(casillas_a_revelar)}")
        
        # Revelar casillas de forma inteligente y aleatoria
        self.revelar_casillas_inteligentemente(casillas_a_revelar, 0)
    
    def _crear_ventana_debug(self):
        """Crea una ventana de debug para monitorear el progreso"""
        if self.ventana_debug:
            self.ventana_debug.destroy()
        
        self.ventana_debug = tk.Toplevel(self.ventana)
        self.ventana_debug.title("DEBUG F3")
        self.ventana_debug.geometry("400x200")
        
        self.label_debug = tk.Label(self.ventana_debug, 
                                   text="Iniciando autosolución...",
                                   font=('Arial', 10),
                                   justify=tk.LEFT,
                                   wraplength=380)
        self.label_debug.pack(padx=10, pady=10)
    
    def _actualizar_debug(self, mensaje):
        """Actualiza el label de debug"""
        if self.label_debug:
            self.label_debug.config(text=mensaje)
        print(f"[DEBUG] {mensaje}")

    
    def obtener_casillas_cercanas_a_vacias(self):
        """Obtiene casillas cercanas (máximo 2 bloques) a casillas vacías"""
        casillas_cercanas = set()
        
        for fila in range(self.filas):
            for columna in range(self.columnas):
                celda = self.celdas[(fila, columna)]
                # Si es una casilla vacía (revelada sin números)
                if celda['state'] == tk.DISABLED and celda['text'] == ' ':
                    # Agregar todas las casillas dentro de 2 bloques de distancia
                    for dx in range(-2, 3):
                        for dy in range(-2, 3):
                            x = fila + dx
                            y = columna + dy
                            if 0 <= x < self.filas and 0 <= y < self.columnas:
                                if (x, y) not in self.minas_posiciones:
                                    if self.celdas[(x, y)]['state'] == tk.NORMAL:
                                        casillas_cercanas.add((x, y))
        
        return casillas_cercanas
    
    def revelar_casillas_inteligentemente(self, todas_casillas, indice):
        if indice >= len(todas_casillas):
            self._actualizar_debug("✓ Autosolución completada!")
            self.autoresolviendo = False
            return
        
        if self.juego_terminado:
            self._actualizar_debug("✓ ¡Juego ganado!")
            self.autoresolviendo = False
            return
        
        # Obtener casillas cercanas a vacías
        casillas_cercanas = self.obtener_casillas_cercanas_a_vacias()
        
        # Casillas no reveladas
        casillas_no_reveladas = [c for c in todas_casillas if self.celdas[c]['state'] == tk.NORMAL]
        
        if not casillas_no_reveladas:
            self._actualizar_debug("✓ Todas las casillas reveladas!")
            self.autoresolviendo = False
            return
        
        casilla = None
        tipo_seleccion = ""
        
        # Prioridad 1: Casillas cercanas a vacías
        if casillas_cercanas:
            casillas_cercanas_no_reveladas = [c for c in casillas_cercanas if c in casillas_no_reveladas]
            if casillas_cercanas_no_reveladas:
                casilla = random.choice(casillas_cercanas_no_reveladas)
                tipo_seleccion = "Cercana a vacía"
        
        # Prioridad 2: Si no hay cercanas, elegir aleatoriamente para explorar
        if not casilla:
            casilla = random.choice(casillas_no_reveladas)
            tipo_seleccion = "Exploración aleatoria"
        
        fila, columna = casilla
        btn = self.celdas[casilla]
        
        # Obtener la posición del botón en la pantalla
        x = btn.winfo_rootx() + btn.winfo_width() // 2
        y = btn.winfo_rooty() + btn.winfo_height() // 2
        
        # Mover el mouse más rápido (50ms)
        pyautogui.moveTo(x, y, duration=0.10)
        
        # Hacer el click
        self.click_izquierdo(fila, columna)
        
        # Actualizar debug
        casillas_restantes = len([c for c in todas_casillas if self.celdas[c]['state'] == tk.NORMAL])
        self._actualizar_debug(f"Casilla: ({fila}, {columna})\nTipo: {tipo_seleccion}\nRestantes: {casillas_restantes}")
        
        # Después de 30ms, revelar la siguiente casilla
        self.ventana.after(30, self.revelar_casillas_inteligentemente, todas_casillas, indice + 1)
    
    def autosolucionar_ia(self, event=None):
        """Activa el modo de autosolución con IA de Gemini"""
        if self.primer_click or self.juego_terminado or self.autoresolviendo:
            return
        
        self.autoresolviendo = True
        self._crear_ventana_debug()
        self._actualizar_debug("Iniciando IA Gemini...\nAprendiendo mecánica...")
        
        # Primer click para generar minas (si no está hecho)
        if self.primer_click:
            self.click_izquierdo(6, 6)
        
        # Iniciar loop de IA
        self.loop_ia()
    
    def obtener_estado_tablero(self):
        """Obtiene representación del tablero actual para enviar a la IA"""
        estado = []
        for fila in range(self.filas):
            fila_datos = []
            for columna in range(self.columnas):
                celda = self.celdas[(fila, columna)]
                if celda['state'] == tk.DISABLED:
                    # Casilla revelada
                    texto = celda['text'].strip()
                    if texto == '':
                        fila_datos.append('0')  # Vacía
                    else:
                        fila_datos.append(texto)  # Número
                else:
                    fila_datos.append('?')  # No revelada
            estado.append(fila_datos)
        return estado
    
    def decidir_casilla_ia(self):
        """Usa lógica PURA del buscaminas - CONSERVADOR, va por lo seguro"""
        try:
            tablero = self.obtener_estado_tablero()
            casillas_no_reveladas = [(f, c) for f in range(self.filas) for c in range(self.columnas) 
                                     if self.celdas[(f, c)]['state'] == tk.NORMAL]
            
            if not casillas_no_reveladas:
                return None
            
            # Prioridad 1: Buscar casillas 100% seguras con lógica pura
            casilla_segura = self._encontrar_casilla_segura_logica(tablero, casillas_no_reveladas)
            if casilla_segura:
                self.historial_juego.append(casilla_segura + ("Casilla segura ✓",))
                return casilla_segura
            
            # Prioridad 2: Si no hay casillas 100% seguras, buscar casillas cercanas a un 0
            for f, c in casillas_no_reveladas:
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nf, nc = f + df, c + dc
                        if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                            celda_adyacente = self.celdas[(nf, nc)]
                            if celda_adyacente['state'] == tk.DISABLED and celda_adyacente['text'] == ' ':
                                self.historial_juego.append((f, c, "Cercana a 0"))
                                self._actualizar_debug(f"Seleccionando ({f},{c}) - Cercana a 0")
                                return (f, c)
            
            # Prioridad 3: Si no hay casillas cercanas a 0, buscar casillas cercanas a números bajos (1, 2)
            for f, c in casillas_no_reveladas:
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nf, nc = f + df, c + dc
                        if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                            celda_adyacente = self.celdas[(nf, nc)]
                            if celda_adyacente['state'] == tk.DISABLED and celda_adyacente['text'] in ['1', '2']:
                                self.historial_juego.append((f, c, f"Cercana a {celda_adyacente['text']}"))
                                self._actualizar_debug(f"Seleccionando ({f},{c}) - Cercana a {celda_adyacente['text']}")
                                return (f, c)
            
            # Último recurso: Elegir una casilla aleatoria para explorar (romper estancamiento)
            casilla_aleatoria = random.choice(casillas_no_reveladas)
            self.historial_juego.append(casilla_aleatoria + ("Exploración aleatoria",))
            self._actualizar_debug(f"Seleccionando ({casilla_aleatoria[0]},{casilla_aleatoria[1]}) - Exploración aleatoria")
            return casilla_aleatoria
            
        except Exception as e:
            self._actualizar_debug(f"Error: {str(e)}\nRecurriendo a exploración aleatoria...")
            casillas_no_reveladas = [(f, c) for f in range(self.filas) for c in range(self.columnas) 
                                     if self.celdas[(f, c)]['state'] == tk.NORMAL]
            return random.choice(casillas_no_reveladas) if casillas_no_reveladas else None
    
    def _encontrar_casilla_segura_logica(self, tablero, casillas_no_reveladas):
        """Aplica lógica pura de buscaminas para encontrar casillas 100% seguras"""
        casillas_seguras = set()
        
        for fila in range(self.filas):
            for columna in range(self.columnas):
                celda = self.celdas[(fila, columna)]
                
                # Si es un número revelado (1-8)
                if celda['state'] == tk.DISABLED and celda['text'].isdigit() and int(celda['text']) > 0:
                    numero = int(celda['text'])
                    
                    unknown_neighbors = []  # Vecinos sin revelar
                    flagged_neighbors_count = 0  # Vecinos marcados como mina (banderas)
                    
                    for df in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if df == 0 and dc == 0:
                                continue
                            nf, nc = fila + df, columna + dc
                            if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                                neighbor_cell = self.celdas[(nf, nc)]
                                
                                if (nf, nc) in self.banderas:  # Si el usuario ha puesto una bandera
                                    flagged_neighbors_count += 1
                                elif neighbor_cell['state'] == tk.NORMAL:  # Si la casilla está sin revelar
                                    unknown_neighbors.append((nf, nc))
                    
                    # Lógica: Si el número de la casilla es igual a las banderas adyacentes,
                    # entonces todas las casillas sin revelar restantes son SEGURAS.
                    if numero == flagged_neighbors_count:
                        casillas_seguras.update(unknown_neighbors)
                        
                elif celda['state'] == tk.DISABLED and celda['text'] == ' ':  # Si es un 0 (casilla vacía)
                    # Todas las casillas adyacentes a un 0 sin revelar son SEGURAS.
                    for df in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if df == 0 and dc == 0:
                                continue
                            nf, nc = fila + df, columna + dc
                            if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                                neighbor_cell = self.celdas[(nf, nc)]
                                if neighbor_cell['state'] == tk.NORMAL:  # Si está sin revelar
                                    casillas_seguras.add((nf, nc))
        
        # Retornar la primera casilla 100% segura encontrada de entre las no reveladas
        for casilla in casillas_seguras:
            if casilla in casillas_no_reveladas:
                return casilla
        
        return None
    
    def loop_ia(self):
        """Loop principal de la IA"""
        if self.juego_terminado or not self.autoresolviendo:
            self._actualizar_debug("Juego terminado")
            self.autoresolviendo = False
            return
        
        casillas_no_reveladas = [(f, c) for f in range(self.filas) for c in range(self.columnas) 
                                 if self.celdas[(f, c)]['state'] == tk.NORMAL]
        
        if not casillas_no_reveladas:
            self._actualizar_debug("✓ ¡IA completó el juego!")
            self.autoresolviendo = False
            return
        
        # Obtener decisión de la IA
        casilla = self.decidir_casilla_ia()
        
        if casilla:
            fila, columna = casilla
            btn = self.celdas[casilla]
            
            # Mover mouse y hacer click
            x = btn.winfo_rootx() + btn.winfo_width() // 2
            y = btn.winfo_rooty() + btn.winfo_height() // 2
            pyautogui.moveTo(x, y, duration=0.1)
            self.click_izquierdo(fila, columna)
            
            casillas_restantes = len([c for c in casillas_no_reveladas if c != casilla])
            self._actualizar_debug(f"IA seleccionó: ({fila}, {columna})\nRestantes: {casillas_restantes}\n\n📚 Aprendiendo patrones...")
        
        # Siguiente movimiento después de 200ms
        self.ventana.after(200, self.loop_ia)







    
    def verificar_victoria(self):
        if self.juego_terminado: return # Añadido: Salir si el juego ya terminó y la ventana se destruyó
        celdas_seguras = (self.filas * self.columnas) - self.minas
        celdas_reveladas = sum(1 for celda in self.celdas.values() if celda['state'] == tk.DISABLED)
        
        if celdas_reveladas == celdas_seguras:
            self.juego_terminado = True
            
            # Si la IA está jugando, reiniciar automáticamente sin messagebox
            if self.autoresolviendo:
                self._actualizar_debug(f"¡Victoria! 🎉 IA ganó en {self.tiempo_transcurrido} segundos. Reiniciando...")
                self._setup_game()
                self.ventana.after(500, self.autosolucionar_ia) # Reiniciar la IA después de un breve retraso
            else:
                # Si no es la IA, dar opción de reiniciar
                messagebox.showinfo("¡Ganaste!", f"¡Victoria en {self.tiempo_transcurrido} segundos! 🎉")
                if messagebox.askyesno("¡Ganaste!", "¿Quieres jugar de nuevo?"):
                    self._setup_game()
                else:
                    self.ventana.destroy()

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = BuscaminasGUI(filas=12, columnas=12, minas=25)
    juego.iniciar()