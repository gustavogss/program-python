# tupla é uma estrutura de dados imutável, já a lista é mutável


frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) # para evitar erros em uma tupla de um único elemento, colocamos uma virgula no final
print(pais)
