
salario=float(input("Digite el salario:"))
año=int(input("En cuantos desea el calculo:"))
i=int()
i=1
while i<=año:
  salario=salario+(salario*0.1)
  print("Es salario en el año",i," es de:",salario)
  i = i+1