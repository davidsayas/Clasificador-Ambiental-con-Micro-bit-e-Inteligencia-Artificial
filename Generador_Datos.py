
import random
import csv

# Para que los resultados sean siempre iguales si alguien corre el codigo de nuevo
random.seed(42)

# Lista vacia donde vamos a guardar todos los ejemplos
datos = []

# --- 30 ejemplos de SEGURO --- etiqueta 0 = seguro
# Gas bajo (0-300), temperatura normal (20-32)
for i in range(30):
    gas = random.randint(0, 300)
    temp = random.randint(20, 32)
    etiqueta = 0
    datos.append([gas, temp, etiqueta])

# --- 30 ejemplos de ALERTA --- etiqueta 1 = alerta
# Gas medio (300-700), temperatura tirando a alta (28-36)
for i in range(30):
    gas = random.randint(300, 700)
    temp = random.randint(28, 36)
    etiqueta = 1
    datos.append([gas, temp, etiqueta])

# --- 30 ejemplos de PELIGRO ---
# Gas alto (700-1023), temperatura alta (30-42)
for i in range(30):
    gas = random.randint(700, 1023)
    temp = random.randint(30, 42)
    etiqueta = 2
    datos.append([gas, temp, etiqueta])

# Mezclar los ejemplos para que no esten ordenados por clase
random.shuffle(datos)

# Guardar los datos en un archivo CSV (formato de tabla)
archivo = open('datos_ambientales.csv', 'w', newline='')
escritor = csv.writer(archivo)
escritor.writerow(['gas', 'temperatura', 'etiqueta'])  # Encabezados
for fila in datos:
    escritor.writerow(fila)
archivo.close()

# Mostrar mensaje de confirmacion
print("Se generaron", len(datos), "ejemplos en datos_ambientales.csv")
print("\nPrimeros 5 ejemplos:")
for fila in datos[:5]:
    print("  Gas:", fila[0], " Temp:", fila[1], " Etiqueta:", fila[2])



    #explicaciion de porque los sensores analogicos utilizan un rango de datos de 0-1023
    #Los sensores analógicos captan datos en un rango de \(0\) a \(1023\) debido a la 
    # resolución de 10 bits del Convertidor Analógico-Digital (ADC) integrado en 
    # microcontroladores estándar, como Arduino. Este componente traduce 
    # voltajes físicos (generalmente de \(0\) a \(5\text{ V}\)) en números discretos.