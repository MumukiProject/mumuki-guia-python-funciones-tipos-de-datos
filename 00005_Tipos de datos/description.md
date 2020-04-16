Como acabamos de ver, en Python existen números, booleanos y strings:

|  Tipo de dato |  Representa             |  Ejemplo |  Operaciones                   |
|---------------|-------------------------|----------|--------------------------------|
|Números        |cantidades               | `4947`   | `+`, `-`, `*`, `%`, `<`, etc   |
|Booleanos      |valores de verdad        | `True`   | `and`, `not`, etc
|Strings        |texto                    | `"hola"` | `str.upper`, `str.startswith`, `len` |


Además, existen operaciones que sirven para todos los _tipos de datos_, por ejemplo:

* `==`: nos dice si dos cosas son iguales
* `!=`: nos dice si dos cosas son diferentes

**Es importante usar las operaciones correctas con los tipos de datos correctos**, por ejemplo, no tiene sentido sumar dos booleanos o hacer operaciones booleanas con los números. **Si usas operaciones que no corresponden, cosas muy raras y malas pueden pasar**. :confounded:

> Probá en la consola las siguientes cosas:
>
> * `5 + 6` (ok, los números se pueden sumar)
> * `5 == 6` (ok, todas las cosas se pueden comparar)
> * `8 > 6` (ok, los números se pueden ordenar)
> * `not True` (ok, los booleanos se pueden _negar_)
> * `False / True` (no está bien, ¡los booleanos no se pueden dividir!)

