if __name__ == '__main__':
	salario = float()
	ano = int()
	x = int()
	print("Digite el salario:")
	salario = float(input())
	print("A cuantos años deseas realizar el calculo:")
	ano = int(input())
	x = 1
	while x<=ano:
		salario = salario+(salario*0.1)
		print("El salario en el año ",x," es de:",salario)
		x = x+1