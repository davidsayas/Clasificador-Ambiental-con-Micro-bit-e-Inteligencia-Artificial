# ============================================================
# ENTRENADOR DE MODELO - VERSION SIMPLE
# Lee los datos del CSV, entrena un Arbol de Decision
# y muestra las reglas que aprendio.
# ============================================================

import csv
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import matplotlib.pyplot as plt
from sklearn import tree as sktree

# --- PASO 1: Leer los datos del archivo CSV ---
caracteristicas = []  # Aqui van [gas, temperatura] de cada ejemplo
etiquetas = []        # Aqui va la clase de cada ejemplo (0, 1 o 2)

archivo = open('datos_ambientales.csv', 'r')
lector = csv.reader(archivo)
next(lector)  # Saltar la primera linea (encabezados)
for fila in lector:
    gas = int(fila[0])
    temp = int(fila[1])
    etiqueta = int(fila[2])
    caracteristicas.append([gas, temp])
    etiquetas.append(etiqueta)
archivo.close()

print("Datos cargados:", len(caracteristicas), "ejemplos")

# --- PASO 2: Crear el modelo Arbol de Decision ---
# max_depth=3 significa que el arbol tendra maximo 3 niveles
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)

# --- PASO 3: Entrenar el modelo con los datos ---
modelo.fit(caracteristicas, etiquetas)
print("Modelo entrenado correctamente")

# --- PASO 4: Probar el modelo con los mismos datos ---
predicciones = modelo.predict(caracteristicas)

# Contar cuantos acerto
aciertos = 0
for i in range(len(etiquetas)):
    if predicciones[i] == etiquetas[i]:
        aciertos = aciertos + 1

precision = aciertos / len(etiquetas) * 100
print("\nPrecision:", round(precision, 1), "%")
print("Acerto", aciertos, "de", len(etiquetas), "ejemplos")

# --- PASO 5: Mostrar las reglas que aprendio el arbol ---
print("\nReglas aprendidas por el arbol:")
print("(Estas son las que vas a copiar a la micro:bit)")
print("-" * 50)
print(export_graphviz(modelo, feature_names=['gas', 'temp']))

# --- PASO 6: Exportar imagen del arbol ---
plt.figure(figsize=(10, 6))
sktree.plot_tree(modelo,
                  feature_names=['gas', 'temp'],
                  class_names=[str(c) for c in modelo.classes_],
                  filled=True,
                  rounded=True)
plt.tight_layout()
plt.savefig('arbol_decision.png', dpi=300)
print("Imagen guardada en 'arbol_decision.png'")