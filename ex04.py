#
# Crie um programa que receba a altura e o peso do usuário, e
# diga seu IMC (Índice de Massa Corporal), dado pela fórmula:
# IMC = peso / (altura ** 2).

# entrada
peso = int(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

# processamento
imc: float = peso / (altura ** 2)
# ou
# imc = peso / (altura ** 2)
print(f"O IMC é: {imc}")

