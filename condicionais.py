saldo = 2000.00
saque = float(input('Informe o valor para saque: '))

if(saque > saldo):
    print('Saldo insuficiente para saque')
elif (saque == saldo):
    print('Quer sacar todo o saldo da conta?') 
else:
    print('Pode sacar')