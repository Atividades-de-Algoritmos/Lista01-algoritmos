#
# Faça um algoritmo que leia 3 variáveis, do tipo caracter.
# A seguir troque o valor das 3 variáveis A, B e C, de forma
# que A fique com o valor de B, B com o valor de C e C com o valor de A.
# Mostre os valores finais.

# entrada
A = input("informe um valor para o A: ")
B = input("informe um valor para o B: ")
C = input("informe um valor para o C: ")

# processamento
X = A # X recebe o valor de A
A = B # A recebe o valor de B
B = C # B recebe o valor de C
C = X # C recebe o valor de X

# saida
print("o valor de A =", A)
print("o valor de B =", B)
print("o valor de C =", C)