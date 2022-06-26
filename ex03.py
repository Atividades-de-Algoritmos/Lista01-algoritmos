#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 3. Crie um programa que recebe suas três notas (colégio,   
# faculdade) e calcule a média final. calcula a média        

# Entrada de dados

nota1 = int(input("informe a nota 1: ")) # Recebendo um valor inteiro para a nota1
nota2 = int(input("informe a nota 2: ")) # Recebendo um valor inteiro para a nota2
nota3 = int(input("informe a nota 3: ")) # Recebendo um valor inteiro para a nota3
print(nota1 + nota2 + nota3) # Imprimindo o valor da soma de todas as notas

# processamento de dados

media = (nota1 + nota2 + nota3) / 3 # Calculando a média

# Saída de dados

print("a média foi ", media) # Imprimindo a média
print("fim do programa") # Informando ao usuário que o programa terminou
