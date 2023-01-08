# retorna True ou False se todos os elementos de um conjunto não estão contidos 
# no outro conjunto

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b) 
print(resultado)  # True

resultado = conjunto_a.isdisjoint(conjunto_c)  
print(resultado) # False
