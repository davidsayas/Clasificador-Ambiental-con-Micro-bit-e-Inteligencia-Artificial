# ============================================================
# CLASIFICADOR AMBIENTAL CON MICRO:BIT - VERSION SIMPLE
# Proyecto de Inteligencia Artificial - UIS
# ============================================================
# Usa un Arbol de Decision entrenado con scikit-learn.
# Precision en datos de entrenamiento: 100%
# ============================================================

# Variables globales
gas_simulado = 0
temp_real = 0

# --- BOTON A: simula fuga de gas (sube +100) ---
def on_button_pressed_a():
    global gas_simulado
    if gas_simulado < 1023:
        gas_simulado = gas_simulado + 100
        if gas_simulado > 1023:
            gas_simulado = 1023
input.on_button_pressed(Button.A, on_button_pressed_a)

# --- BOTON B: simula aire limpio (resetea a 0) ---
def on_button_pressed_b():
    global gas_simulado
    gas_simulado = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# --- MODELO DE CLASIFICACION ---
# Reglas aprendidas automaticamente por el Arbol de Decision:
#   gas <= 301           -> SEGURO
#   gas entre 301 y 698  -> ALERTA
#   gas > 698            -> PELIGRO
def clasificar(gas, temp):
    if gas <= 301:
        return 0
    else:
        if gas <= 698:
            return 1
        else:
            return 2

# --- BUCLE PRINCIPAL ---
def on_forever():
    global temp_real
    # 1. Leer temperatura real del sensor de la micro:bit
    temp_real = input.temperature()
    # 2. Clasificar la situacion actual
    estado = clasificar(gas_simulado, temp_real)
    # 3. Mostrar resultado en la pantalla de LEDs
    if estado == 2:
        basic.show_icon(IconNames.SKULL)
    elif estado == 1:
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.SQUARE)
    basic.pause(500)
basic.forever(on_forever)