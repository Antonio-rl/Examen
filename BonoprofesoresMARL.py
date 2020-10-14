def BonoprofesoresMARL():
  puntos=int(input("Digite el valor de punto:"))
  salario=float(input("Digite el valor del salario:"))

  if puntos>=50:
    monto=salario*0.1
  if puntos<=100:
    monto=salario*0.1
  if puntos>=101 and puntos<=150:
   monto=salario*0.5
  if puntos>=151:
   monto=salario*0.8
  print("El monto del bono del profesor es:",monto)
BonoprofesoresMARL()