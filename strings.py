NOME = input('Digite um nome: ')
print()
print(NOME.upper())
print(NOME.lower())
print(NOME.title()) # 1 Maisucula e o restante minuscula
print(NOME.strip()) # Remove espaços em branco no inicio e fim
print(NOME.lstrip()) # Remove espaços em branco na esquerda
print(NOME.rstrip()) # Remove espaços em branco a direita
print('$$$' + NOME + '$$') # Concatenando strings
print(NOME.center(10, '$')) # (qtd de caracteres, 'tipo de caracter a ser preenchido')

print("_".join(NOME)) # "tipo de caracter" passando letra a letra, substitui o loop for abaixo

for letra in NOME:
    print (letra, end="_")


