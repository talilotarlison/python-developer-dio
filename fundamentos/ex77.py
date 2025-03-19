def verificar_pares(numeros:list):
  num_pares = []
  
  for par in numeros:
    if par % 2 == 0:
      num_pares.append(par)
      
  soma_pares(num_pares)      

def soma_pares(num_pares:list):
  soma_num = 0
  for num in num_pares:
      soma_num += num
  
  print(soma_num)

  
verificar_pares(numeros=[1,2,3,4,5])


def verificar_pares2(numeros:list):
  num_pares = 0
  
  for par in numeros:
    if par % 2 == 0:
      num_pares += par
      
  print(num_pares)  

verificar_pares2([1,2,3,4,5])
