#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 1. Faça um algoritmo de conversão de uma temperatura em    
# graus Celsius para uma temperatura em Fahrenheit.          

# entrada de dados

celsius = float(input("informe a temperatura em celsius: ")) # lemos a temperatura em Celsius informada pelo usuário

# processamento

fahrenheit = 9/5 * celsius + 32 # calculamos a temperatura em fahrenheit usando a fórmula da conversão de temperatura em Celsius para fahrenheit.

# saída de dados

print(f"A temperatura em fahrenheit é: {fahrenheit}") # imprimimos a temperatura em fahrenheit
print('fim do programa') # Informamos ao usuário que o programa terminou
