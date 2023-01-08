# sort - ordena a lista alfabeticamente
# lambda - é uma função anônima que executa um argumento 

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  
print(linguagens) # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ordena a lista alfabeticamente e faz o espelhamento dela 
print(linguagens) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ordena as linguagens pelos tamanhos das palavras 
print(linguagens) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ordena pelo tamanho das palavras e depois espelha a lista
print(linguagens) # ["python", "csharp", "java", "js", "c"]
