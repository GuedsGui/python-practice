print("CÁLCULOS COM NÚMEROS INTEIROS E REAIS")

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

resultado1 = (2 * num1) + (num2 / 2)
resultado2 = (3 * num1) + num3
resultado3 = num3 ** 3

print(f"O produto do dobro do primeiro número com metade do segundo: {resultado1} \nA soma do triplo do primeiro número com o terceiro: {resultado2} \nO terceiro número elevado ao cubo: {resultado3:.2f}")
