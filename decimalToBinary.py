def decimal_to_binary(decimal):
    """
    Convierte un número decimal a una cadena binaria.

    >>> decimal_to_binary(10)
    '1010'
    >>> decimal_to_binary(15)
    '1111'
    >>> decimal_to_binary(0)
    '0'
    >>> decimal_to_binary(-1)  # Entrada no válida
    'El valor ingresado no es un número decimal válido.'
    """
    try:
        if decimal >= 0:
            return bin(decimal)[2:]  # [2:] elimina el prefijo '0b'
        else:
            return "El valor ingresado no es un número decimal válido."
    except TypeError:
        return "El valor ingresado no es un número decimal válido."
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    decimal = int(input("Ingrese el numero decimal a convertir: "))
    binario = decimal_to_binary(decimal)
    print (f'El numero binario de {decimal} es: {binario}')