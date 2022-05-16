import math

print ("Hello World")
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print ("A soma é", a+b)
print ("A diferença é", a-b)
print ("O produto é", a*b)
if(b == 0):
  print("Não é possível dividir por zero!")
else:
  print ("A divisão é", a/b)
print ("O expoente é", math.pow(a,b))



