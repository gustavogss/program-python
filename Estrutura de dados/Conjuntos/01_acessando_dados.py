# Não é possivel acessar os objetos diretamente do Conjunto atraves do indice
# Para isso, é necessário transformar o conjunto em uma lista

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0]) # 1
print(numeros[1]) # 2
print(numeros[2]) # 3
print(numeros[3]) # Erro - porque acabou os objetos da lista
