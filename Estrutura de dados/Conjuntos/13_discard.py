numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) # irá remover o elemento 1 do conjunto
numeros.discard(45) # o valor 45 vai ser ignorado, porque ele não existe na lista

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
