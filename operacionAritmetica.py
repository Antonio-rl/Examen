
valor1=float(input("Digite su primer valor:"))
valor2=float(input("Digite su segundo valor:"))
print("\nLas signos siguiente son +,-,/,*,^")
signo=input("\nDigite el signo de operacion:")

if signo=='+':
  suma=valor1+valor2
  print("La suma es:",suma)
elif signo=='-':
  resta=valor1-valor2
  print("La resta es:",resta)
elif signo=='/':
  division=valor1/valor2
  print("La division es:",division)
elif signo=='*':
  multiplicar=valor1*valor2
  print("La division es:",multiplicar)
elif signo=='^':
  exponente=int(input("Digite el exponente:"))
  potencia1=valor1**exponente
  potencia2=valor2**exponente
  print("La potencia de",valor1," es:",potencia1)
  print("La potencia de",valor2," es:",potencia2)
else:
  print("Se etivoco de operacion.")
