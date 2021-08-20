![Tec de Monterrey](../../images/logotecmty.png)
# Distancia entre dos puntos
Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    #Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
    #Los mensajes para recibir las 4 entradas deben ser **"x1=    y1=     x2=   y2=   ** respectivamente "
    #El mensaje para la salida debe ser **"distancia= **"

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema

Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.

**Entradas**

El programa solicita el punto inicial (x1, y1) y el final (x2, y2). Todos enteros y en ese orden.

**Salida** 

El valor de la distancia (numero flotante) que existe entre los dos puntos. Despliega el resultado con la palabra distancia (todo en minúsculas) y un = y el número formateado a 2 decimales (sin espacios entre caracteres y números). Por ejemplo: distancia= 9.90

## Ejemplos de ejecución

Ejemplo 1 

```plaintext
x1= 2
y1= -4
x2= 5
y2= 3
distancia= 7.62
```

Ejemplo 2 

```plaintext
x1= 5
y1= 10
x2= -3
y2= -4
distancia= 16.12
```
**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
