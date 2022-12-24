N = int(input())

while(N > 0):
  
    valores = input().strip().split(" ")

if len(valores) > 1:
    A, B = valores[0], valores[1]

    if (len(A) > 0 and len(B) > 0) and (len(A) <= 1000 and len(B) <= 1000):

      if A[len(A) - len(B):] == B:
        print("encaixa")
      else:
        print("nao encaixa")
      n =- 1 
  