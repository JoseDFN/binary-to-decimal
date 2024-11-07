def binary_to_decimal(binario):
    """
    Convierte una cadena binaria a decimal.

    >>> binary_to_decimal("1010")
    10
    >>> binary_to_decimal("1111")
    15
    >>> binary_to_decimal("0")
    0
    >>> binary_to_decimal("1021")
    >>> binary_to_decimal("abc")
    """
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "El valor ingresado no es un número binario válido."
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    binario=input("Ingrese un numero binario: ")
    decimal = binary_to_decimal(binario)
    print (f'El numero decimal de {binario} es: {decimal}')
