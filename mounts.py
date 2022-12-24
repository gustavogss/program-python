month = int(input("Digite o numero do mẽs: "))

month_dict = {
  1: 'january' , 
  2: 'february' , 
  3: 'march', 
  4: 'april',
  5: 'may',
  6: 'june', 
  7: 'july', 
  8: 'august', 
  9: 'setember',
  10: 'october',
  11: 'november', 
  12: 'december'
  }
  
print(month_dict[month].title())