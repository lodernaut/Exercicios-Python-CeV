altura = float(input("Digite sua altura em (metros): "))
peso = float(input("Digite seu peso em (Kg): "))

imc = peso / (altura **2)
print('=-='*20)
print(f'Seu IMC é: {imc:.1f}'.center(60))
if imc <= 18.5:
    print(f'Abaixo do peso.'.center(60))
elif imc > 18.5 and imc <= 25:
    print(f'Peso ideal.'.center(60))
elif imc > 25 and imc <= 30:
    print(f'Sobrepeso.'.center(60))
elif imc > 30 and imc <= 40:
    print(f'Obesidade.'.center(60))
else:
    print(f'Obesidade mórbida.'.center(60))

print('=-='*20)
