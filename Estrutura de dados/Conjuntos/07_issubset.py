# retorna como resposta True ou False, se todos os elementos pertencem a um conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  
print(resultado) # True

resultado = conjunto_b.issubset(conjunto_a)  
print(resultado) # False
