# OOP_reto_05

Este reto consistía en imitar el ejercicio realizado en el [reto anterior](https://github.com/Unbo10/OOP_reto_04) usando módulos, tanto archivos como paquetes. Esto se llevó a cabo de dos modos:
- Por un lado, se usó un único módulo archivo [``AllinOne.py``](/Shape/AllinOne.py) dentro del módulo paquete [``Shape/``](/Shape/) que contenía todas las clases usadas para el ejercicio. Este se importó al archivo [``test_multimodules.py``](/test_multimodules.py), en el que se implementó una prueba de todas las clases tal cual como se hizo en el reto anterior.
- Por otro lado, se crearon múltiples módulos paquete y archivo para separar las clases de una manera mucho más legible y sostenible en el tiempo. De nuevo, todos están contenidos en [``Shape/``](/Shape/). Dentro de este directorio se encuentra [``shape.py``](/Shape/shape.py), el módulo que contiene la clase ``Shape``, que como se puede ver en el [diagrama de clase](https://github.com/Unbo10/OOP_reto_04/blob/main/README.md) del reto anterior, es la clase de la que casi todas las demás van a heredar. Dentro del paquete ``Shape/`` se encuentran tres subpaquetes: [``Edge/``](/Shape/Edge/), [``Rectangle/``](/Shape/Rectangle/), y [``Triangle/``](/Shape/Triangle/). 
  - ``Edge/`` contiene a los módulos [``edge.py``](/Shape/Edge/edge.py) y [``vertex.py``](/Shape/Edge/vertex.py), que respectivamente contienen a las clases ``Edge`` y ``Vertex``, que serán esenciales para la construcción de todas las demás clases (toda figura tiene aristas y vertices).
  - ``Rectangle/`` contiene a los módulos [``rectangle.py``](/Shape/Rectangle/rectangle.py) y [``square.py``](/Shape/Rectangle/square.py), que respectivamente contienen a la clase ``Rectangle``, que hereda de ``Shape``, y ``Square``, que hereda de la misma ``Rectangle``. Ambas importan las clases ``Vertex`` y ``Edge`` de ``Edge/``.
  - ``Triangle/`` contiene a los siguientes módulos (todos importan de ``Edge/`` las clases ``Vertex`` y ``Edge``):
    - [``triangle.py``](/Shape/Triangle/triangle.py) que hereda directamente de ``Shape`` para definir la clase ``Triangle``, heredada por todos los demás módulos de este paquete.
    - [``equilateral.py``](/Shape/Triangle/equilateral.py), que define la clase hija ``Equilateral``.
    - [``isosceles.py``](/Shape/Triangle/isosceles.py), que define la clase hija ``Isosceles``.
    - [``rectangle.py``](/Shape/Triangle/rectangle.py), que define la clase hija ``RightTriangle``.
    - [``scalene.py``](/Shape/Triangle/scalene.py), que define la clase hija ``Scalene``.

  Ahora bien, cada módulo cuenta con su propio bloque de código ejecutable que le sigue al ``if __name__ = "__main__"`` (si se está ejecutando como un script y no como un módulo) para probar las funcionalidades de cada uno. Además, se definen las funciones ``test_default()`` y ``test_user_input()`` para cada módulo. Esta última función, ``test_user_input()``, se importa a [``test_multimodules.py``](/test_multimodules.py), el archivo en el que el usuario puede evidenciar la funcionalidad de todos los módulos del paquete ``Shape/``  (a excepción del módulo que traía todas las clases incluidas). Ya que la función está definida en cada uno de los módulos, en el archivo de prueba simplemente se llama a la función de cada módulo (llamadas de modo diferente para distinguirlas) y en consola el usuario puede probar la funcionalidad de cada módulo del paquete de manera interactiva.

A continuación se muestra un diagrama de árbol de la estructura del repositorio y del paquete para que se entienda de mejor manera lo que se explicó hace un momento. 

<table>
<tr>
<th style="text-align: center"> Estructura del directorio (repositorio) </th>
<th style = "text-align: center"> Estructura del paquete </th>
</tr>
<tr>
<td>

```
.
|-- README.md
|-- Shape
|   |-- AllinOne.py     
|   |-- Edge
|   |   |-- edge.py     
|   |   `-- vertex.py   
|   |-- Rectangle       
|   |   |-- rectangle.py
|   |   `-- square.py   
|   |-- Triangle        
|   |   |-- equilateral.py
|   |   |-- isosceles.py
|   |   |-- rectangle.py
|   |   |-- scalene.py
|   |   `-- triangle.py
|   `-- shape.py
|-- test_AllinOne.py
`-- test_multimodules.py
```

</td>

<td>

```
.
|-- AllinOne.py
|-- Edge
|   |-- edge.py
|   `-- vertex.py
|-- Rectangle
|   |-- rectangle.py
|   `-- square.py
|-- Triangle
|   |-- equilateral.py
|   |-- isosceles.py
|   |-- rectangle.py
|   |-- scalene.py
|   `-- triangle.py
`-- shape.py
```
</td>
</tr>
</table>