# Conjuntos - é uma coleção de objetos não repetidos.
# Usamos o set ou {} para eliminar objetos duplicados.
# O set e o {} não retorna a ordem dos iteravéis

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) # passando uma tupla (())
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python", "javascript"}
print(linguagens) # {'java', 'python', 'javascript'}
