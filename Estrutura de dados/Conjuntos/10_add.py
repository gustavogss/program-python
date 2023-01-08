# add - serve para adicionar um elemento se não for repetido no conjunto

sorteio = {1, 23}

sorteio.add(25)  
print(sorteio) # {1, 23, 25}

sorteio.add(42)  
print(sorteio) # {1, 23, 25, 42}

sorteio.add(25) # 25 vai ignorado porque já tem no conjunto
print(sorteio) # {1, 23, 25, 42}
