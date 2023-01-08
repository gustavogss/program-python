# Dicionário - é um conjunto não ordenado de pares chave:valor

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa) # {'nome': 'Guilherme', 'idade': 28}

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa) # {'nome': 'Guilherme', 'idade': 28}

pessoa["telefone"] = "3333-1234" # adicionando um novo elemento ao dicionário
print(pessoa) # {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}
