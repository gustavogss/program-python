# pop - remove os elementos do conjunto na sequência

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros.pop(4))  # Erro
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
