NOME = input('Digite seu nome: ')
IDADE = int(input('Digite sua idade: '))
PROFISSAO = input('Digite sua profissão: ')
STACK = input('Digite a stack que você trabalha: ')

print()

print(NOME.upper())
print(NOME.lower())
print(NOME.title()) # 1 Maisucula e o restante minuscula
print(NOME.strip()) # Remove espaços em branco no inicio e fim
print(NOME.lstrip()) # Remove espaços em branco na esquerda
print(NOME.rstrip()) # Remove espaços em branco a direita
print('$$$' + NOME + '$$') # Concatenando strings
print(NOME.center(10, '$')) # (qtd de caracteres, 'tipo de caracter a ser preenchido')

print("_".join(NOME)) # "tipo de caracter" passando letra a letra, substitui o loop for abaixo

for letra in NOME:
    print (letra, end="_")

# Interpolação de strings (A desvantagens é que as variáveis tem que ser informadas em sequência)

# %s - para substituir strings
# %d - para substituir números 
# %f - para substituir números de ponto flutuante 
print()

print('Olá, meu nome é %s tenho %d anos de idade, e trabalho como %s %s.' %(NOME, IDADE, PROFISSAO, STACK))

# Com o método format temos diversas formas de trabalhar usando {}
# sem informar a posição, mas passando a sequência exata das variáveis
# informando as posições {3}
# substituindo as variáveis pelos seus nomes
# por meio de dicionarios .format(**pessoa)

print('Olá, meu nome é {} tenho {} anos de idade, e trabalho como {} {}.' .format(NOME, IDADE, PROFISSAO, STACK))
print('Olá, meu nome é {1} tenho {2} anos de idade, e trabalho como {3} {0}.' .format(STACK, NOME, IDADE, PROFISSAO))
print('Olá, meu nome é {nome} tenho {idade} anos de idade, e trabalho como {profissao} {stack}.' .format(nome=NOME, idade=IDADE, profissao=PROFISSAO, stack=STACK))

pessoa = {"nome":"Gustavo", "idade":47, "profissao":"Programador", "stack":"Python"}
print('Olá, meu nome é {nome} tenho {idade} anos de idade, e trabalho como {profissao} {stack}.' .format(**pessoa))

# Manipulando string com o f (É a forma mais atual de utilizarmos)
print(f'Olá, meu nome é {NOME} tenho {IDADE} anos de idade, e trabalho como {PROFISSAO} {STACK}.')
print()
PI = 3.14159
print(f'O valor de PI é: {PI:.2f}') #Coloca duas casas após o ponto 3.14
print(f'O valor de PI é: {PI:10.2f}') #Coloca um espaço em branco de dez caracteres antes do ponto

print()
# Fatiamento de Strings
print(NOME[0]) # Pega a primeira letra na posição 0
print(NOME[-1]) # Pega a última letra da string
print(NOME[:5]) # Pega do inicio até o caracter 5
print(NOME[3:]) # Pega a partir da posição 3 ao final da string
print(NOME[3:6]) # Pega um pedaço da string da posição 3 a 6
print(NOME[3:8:2]) # Pega um pedaço da string da posição 3 a 8 contando de 2 em 2
print(NOME[:]) # Retorna a cópia da string
print(NOME[::-1]) # Retorna a string espelhada e invertida
print()

# Strings de múltiplas linhas ou triplas f'''. Respeita a quebra de linhas, espaços e formatação do texto
mensagem = f'''
Meu nome é {NOME}.
Tenho {IDADE} idade.
    Sou {PROFISSAO}.
E trabalho com {STACK}
'''
print(mensagem)

print()

print(
    f'''
    ============== MENU ================\n  
    1 - Depositar
    2 - Sacar
    0 - Sair\n
    =====================================
    
        Obrigado por usar nosso sistema!
    '''
)

# \n pula uma linha




 
 