print("Seja bem-vind@, vamos calcular seu IMC?")

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 16:
	print("Abaixo do Peso")
elif imc < 17:
	print("Peso Moderado")
elif imc < 18.5:
	print("Peso Excelente")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")