Ahora miremos a los booleanos con un poco más de detalle:

* Se pueden negar, mediante el operador `!`: `!hay_comida`
* Se puede hacer la conjunción lógica entre dos booleanos (_and_, también conocido en español como _y lógico_), mediante el operador `&&`: `hay_comida && hay_bebida`
* Se puede hacer la disyunción lógica entre dos booleanos (_or_, también conocido en español como _o lógico_), mediante el operador `||`: `una_expresion || otra_expresion`

> Veamos si se entiende; escribí las siguientes funciones:
>
> * `esta_entre`, que tome tres números y diga si el primero es mayor al segundo y menor al tercero.
> * `esta_fuera_de_rango`: que tome tres números y diga si el primero es menor al segundo o mayor al tercero
>
> Ejemplos:
>
> ```python
> ム esta_entre(3, 1, 10)
> True
> ム esta_entre(90, 1, 10)
> False
> ム esta_entre(10, 1, 10)
> False
> ム esta_fuera_de_rango(17, 1, 10)
> True
> ```
>
