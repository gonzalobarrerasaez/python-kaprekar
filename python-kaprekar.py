numero = 3425  # Debe ser de 4 digitos
resultado = 0
while numero != 6174:
    numero_str = str(numero).zfill(4)
    ascendente = int(''.join(sorted(numero_str)))
    descendente = int(''.join(sorted(numero_str, reverse=True)))
    numero = descendente - ascendente
print(numero)
