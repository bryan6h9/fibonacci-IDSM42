def fibonacci(n):
    """
    Calcula el término n de la sucesión de Fibonacci.

    Parámetros:
        n (int): Posición de la sucesión.

    Retorna:
        int: Valor de Fibonacci en la posición n.

    Excepciones:
        TypeError: Si n no es un número entero.
        ValueError: Si n es negativo.
    """

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero")

    if n < 0:
        raise ValueError("El número no puede ser negativo")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci(10))
