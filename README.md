## Clasificador Ambiental con Micro:bit e Inteligencia Artificial
Sistema de monitoreo ambiental en tiempo real que utiliza un Árbol de Decisión entrenado con scikit-learn para clasificar el nivel de riesgo en tres categorías: Seguro, Alerta y Peligro, según las lecturas de gas y temperatura.
Proyecto académico desarrollado para el curso de Inteligencia Artificial en la Universidad Industrial de Santander (UIS).

## Descripcion general

El proyecto implementa un flujo completo de Machine Learning

- Generación de datos sinteticos que simulan lecturas convertidas analogicamente de un sensor de gas (rango 0-1023) y temperatura ambiente.
- Entrenamiento de un Árbol de Decisión con scikit-learn que aprende a clasificar tres estados ambientales.
- Despliegue del modelo en una tarjeta BBC micro:bit, donde el árbol se ejecuta como una cadena de condicionales en MakeCode.
- Resultado en tiempo real reflejado en la matriz de leds de la Micro:bit

## 🧮Umbrales aprendidos por el modelo de clasificacion

| Etiqueta | Estado | Icono de led | Condicion aprendida |
| :--- | :---: | --- | ---:|
| Fila 1, Dato 1 | Fila 1, Dato 2 | Fila 1, Dato 3 |
| Fila 2, Dato 1 | Fila 2, Dato 2 | Fila 2, Dato 3 |
