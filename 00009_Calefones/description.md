Ahora te toca a vos: tenemos que cargar un calefón con agua :potable_water:. No parece una tarea difícil pero tenemos que tener en cuenta algunas cosas:

* La capacidad del calefón es de 25 litros
* No está completamente vacío, sino que tiene algo de agua
* Si cargo el calefón con más agua de la que cabe en el recipiente, rebalsa.

Por eso, necesitamos una función que tome la cantidad de agua que tiene actualmente el tanque y la cantidad de agua que quiero cargar, y me diga cuánta agua carga efectivamente. Veamos algunos ejemplos:

```python
ム cuanto_carga(10, 5) # tiene 10 litros de agua,
                       # y lo intento cargar con 5 litros más
5 # carga 5 litros, porque no rebalsa
ム cuanto_carga(20, 5)
5
ム cuanto_carga(22, 5)
3
ム cuanto_carga(25, 5)
0
```

> Escribí la función `cuanto_carga`
