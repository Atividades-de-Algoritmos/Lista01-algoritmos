#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 1. Faça um algoritmo de conversão de uma temperatura em    
# graus Celsius para uma temperatura em Fahrenheit com a     
# a fórmula de conversão f = 9/5 * c + 32                          

# Entrada de dados

celsius = float(input("informe a temperatura em celsius: ")) # Lemos a temperatura em Celsius informada pelo usuário

# Processamento de dados

fahrenheit = 9/5 * celsius + 32 # Calculamos a temperatura em fahrenheit usando a fórmula da conversão de temperatura em Celsius para fahrenheit.

# saída de dados

print(f"A temperatura em fahrenheit é: {fahrenheit}") # Imprimimos a temperatura em fahrenheit
print('fim do programa') # Informamos ao usuário que o programa terminou
