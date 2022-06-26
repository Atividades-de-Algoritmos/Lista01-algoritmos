#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 2. Faça um algoritmo que leia 3 variáveis, do tipo carácter
# A seguir troque o valor das 3 variáveis A, B e C, de forma 
# que A fique com o valor de B, B com o valor de C e C com o 
# valor de A. Mostre os valores finais.

# entrada de dados

A = input("informe um valor para o A: ") # Usamos input() para saber o valor de A
B = input("informe um valor para o B: ") # Usamos input() para saber o valor de B
C = input("informe um valor para o C: ") # Usamos input() para saber o valor de C
B = input("informe um valor para o B: ") # Usamos input() para saber o valor de D

# processamento de dados

X = A # X vai recebe o valor da variável A
A = B # A vai recebe o valor da variável B
B = C # B vai recebe o valor da variável C
C = X # C vai recebe o valor da variável X

# saída de dados

print("o valor de A =", A) # Imprimindo no terminal o valor de A
print("o valor de B =", B) # Imprimindo no terminal o valor de B
print("o valor de C =", C) # Imprimindo no terminal o valor de C

print("fim do programa") # Informamos ao usuário que o programa terminou
