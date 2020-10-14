def vacunaCovid19MARL():
  edad=int(input("Digite la edad:"))
  print("Seleccione el sexo:")
  print("   1.Hombre")
  print("   2.Mujer")
  sexo=int(input("Digite el numero:"))

  if edad>70:
    print("C")
  if sexo==2 and edad>=16 and edad<70:
    print("B")
  if (sexo==1 and edad>=16 and edad<70) or edad<16:
    print("A")
vacunaCovid19MARL()