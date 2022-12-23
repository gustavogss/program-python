tamanho = int(input('Digite o tamanho do range: '))
for numero in range(tamanho): #range(tamanho_da_sequencia)
    if numero % 2 == 0:
        continue
    print(numero, end=" ")