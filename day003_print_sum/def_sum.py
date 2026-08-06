print("IMPRIMINDO A SOMA DE DOIS NÚMEROS")

def soma():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    
    soma = num1 + num2
    
    return num1, num2, soma

def main():
    numero1, numero2, somar_numeros = soma()
    print(f"Resultado da soma: {numero1} + {numero2} = {somar_numeros}")
    
if __name__ == "__main__":
    main()
