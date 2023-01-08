lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

l2 = lista.copy()
print(id(l2), id(lista)) # 139756173158016 139756173157312

l2[0]= 3
print(l2)
print(lista)
