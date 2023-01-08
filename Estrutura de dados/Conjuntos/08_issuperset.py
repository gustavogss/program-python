# retorna como resposta True ou False, se todos os elementos não pertencem a um conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  
print(resultado) # False

resultado = conjunto_b.issuperset(conjunto_a)  
print(resultado) # True
