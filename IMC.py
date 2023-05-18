peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2

if imc < 18.5:
    print("Abaixo do Peso. Seu IMC é {:.2f}".format(imc))
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal. Seu IMC é {:.2f}".format(imc))
elif imc >= 25 and imc <= 30:
    print("Sobrepeso. Seu IMC atual é {:.2f}".format(imc))
elif imc >= 30 and imc <= 40:
    print("Obesidade. Seu IMC atual é {:.2f}".format(imc))
elif imc >= 41:
    print("Obesidade mórbida. Seu IMC atual é {:.2f}".format(imc))
    