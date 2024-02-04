# Forecast de Ventas

Esta empresa fabrica y distribuye colores alrededor de todo el mundo, su producto principal es el color negro, del cual depende la 60% de su producción y el 50% de sus ventas.

![alt text](https://github.com/stevenallus/Portfolio/blob/main/PROJECTS/Forecast_Ventas/01_Documentos/forecasventas_final.png)



## Motivo del caso

Para el departamente de produccion y de ventas es critico poder mejorar la previsibilidad de ventas de los diferentes productos, 

* Para ventas a fin de poder estimar la ventas en lo siguientes meses y detectar las acciones clave a realizar

* Para produccion para realizar un correcto aprovisionamiento de materias primas y ocupacion de las lineas de produccion.

Tambien servirá para la parte logística para decidir donde se tiene que almancenar el producto a fin de llegar a no tener roturas de stock y no perder oportunidades.

## Objetivo del caso

En este proyecto el objetivo es crear un algoritmo para saber cuanto va a vender la empresa.

Si se lo que voy a vender se lo que tengo que comprar y tener el stock correcto, si hago menos stock del que debo entonces puedo perder ventas. Si hago un sobrestock pongo demasiados recursos y costes innecesarios, tengo menos caja para operar.

Predecir las ventas es ayudar al correcto funcionamiento de toda las cadenas de la empresa

Por temas de confidencialidad de datos de la empresa se ha hecho sobre un dataset modificado que no puede revelar ninguna informacion de la empresa real. (dataset de empresa RETAIL)

BASE de datos SQL con 3 años de ventas


### RETOS 

* Forecasting Jerarquico categoria, subcategoria, en la modelizacion de cada cuando uno la preivison no coincide, problema para la empresa para estar de acuerdo en todo. Por ejemplo el de compras le interesa el dato agregado para comprar la materia prima pero el de logisitica le interesa el dato desagregado por producto.

* Demanda intermitente, no todos los dias se tiene ventas del producto, hay dias que se compran 0 productos porque el cliente no ha comprado, problema de demanda, y otro puede ser que no haya comprado porque no habia stock, por lo tanto problema de oferta.

* Generar modelos para cientos o milos de SKUs, como arreglar esto para modelizar de manera vista

* Generar predicciones a varios dias vista. La produccion y la compra de materia prima no se puede hacer el mismo dia por lo que se tienes que hacer la prevision a varios dias vista a fin de que esos departamentos puedan organizarse de manera adecuada, es decir, predecir las ventas de solo mañana no nos ayuda.

* El forecast con ARIMA me hace prediccion de ese horizonte en adelante pero en Machine Learning una de las dificultades es que solo me predicen a 1 dias vista, hay dos maneras de solucionarlo y explico el porque elijo una.

