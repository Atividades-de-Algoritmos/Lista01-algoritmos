#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 4. Crie um programa que receba a altura e o peso do usuário,
# e diga seu IMC (Índice de Massa Corporal), dado pela fórmula:
# IMC = peso / (altura ** 2).

# entrada de dados

peso = int(input("Digite o peso: ")) # Recebendo o valor inteiro do peso
altura = float(input("Digite a altura: ")) # Recebendo o valor flutuante da altura

# Processamento de dados

imc = peso / (altura ** 2) # Calculando o IMC
# imc = peso / (altura * altura) - Possível alternativa

# Saída de dados

print(f"O IMC é: {imc}") # Imprimindo o valor do IMC
print("fim do programa") # Informando ao usuário que o programa terminou