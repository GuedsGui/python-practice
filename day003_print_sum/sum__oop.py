print("IMPRIMINDO A SOMA DE DOIS NÚMEROS")

class Soma:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculo(self):
        return self.num1 + self.num2
    
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

somar = Soma(num1, num2)

resultado = somar.calculo()

print(f"Resultado da soma: {num1} + {num2} = {resultado}")
