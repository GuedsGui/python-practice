print("CÁLCULOS COM NÚMEROS INTEIROS E REAIS")

def numeros():
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))
    num3 = float(input("Digite um número real: "))

    return num1, num2, num3
    
def main():
    numero1, numero2, numero3 = numeros()
    
    resultado1 = (2 * numero1) + (numero2 / 2)
    resultado2 = (3 * numero1) + numero3
    resultado3 = numero3 ** 3

    print(f"O produto do dobro do primeiro número com metade do segundo: {resultado1} \nA soma do triplo do primeiro número com o terceiro: {resultado2} \nO terceiro número elevado ao cubo: {resultado3:.2f}")
    
if __name__ == "__main__":
    main()
