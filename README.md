## Clasificador Ambiental con Micro:bit e Inteligencia Artificial
Sistema de monitoreo ambiental en tiempo real que utiliza un Árbol de Decisión entrenado con scikit-learn para clasificar el nivel de riesgo en tres categorías: Seguro, Alerta y Peligro, según las lecturas de gas y temperatura.
Proyecto académico desarrollado para el curso de Inteligencia Artificial en la Universidad Industrial de Santander (UIS).

Descripcion general
El proyecto implementa un flujo completo de Machine Learning embebido:

Generación de datos sintéticos que simulan lecturas de un sensor de gas (rango 0-1023) y temperatura ambiente.
Entrenamiento de un Árbol de Decisión con scikit-learn que aprende a clasificar tres estados ambientales.
Despliegue del modelo en una tarjeta BBC micro:bit, donde el árbol se ejecuta como una cadena de condicionales en MakeCode/JavaScript.
Inferencia en tiempo real sobre la tarjeta, mostrando el estado en la matriz de LEDs.
