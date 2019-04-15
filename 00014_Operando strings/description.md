¿Y qué podemos hacer con los strings, además de compararlos? ¡Varias cosas! Por ejemplo, podemos preguntarles cuál es su cantidad de letras:

```python
ム len("biblioteca")
10
ム len("babel")
5
```

O también podemos _concatenarlos_, es decir, obtener **uno nuevo** que junta dos strings:

```python
ム "aa" + "bb"
"aabb"
ム "sus anaqueles " + "registran todas las combinaciones"
"sus anaqueles registran todas las combinaciones"
```

O podemos preguntarles si uno comienza con otro:

```python
ム str.startwith("una página", "una")
True
ム str.startwith("la biblioteca", "todos los fuegos")
False
```

> Veamos si queda claro: escribí una función `longitud_nombre_completo`, que tome un nombre y un apellido, y devuelva su longitud total, contando un espacio extra para separar a ambos:
>
>```python
> ム longitud_nombre_completo("Cosme", "Fulanito")
>14
>```
