# remove - é uma outra forma de remover um objeto da lista. A diferença aqui é 
# que se passa o objeto que se deseja remover, ao invés do indice como acontece
# com o método pop.
# remove apenas uma ocorrência do objeto

linguagens = ["python", "js", "c", "java", "csharp", "c"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp", "c"]
