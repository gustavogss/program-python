texto = input('Digite o texto: ')
VOGAIS = 'AEIOU'
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()