print("CÁLCULOS COM NÚMEROS INTEIROS E REAIS")

class Numeros:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def calculo1(self):
        return (2 * self.num1) + (self.num2 / 2)
        
    def calculo2(self):
        return (3 * self.num1) + self.num3
    
    def calculo3(self):
        return self.num3 ** 3
        
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

numeros = Numeros(num1, num2, num3)

resultado1 = numeros.calculo1()
resultado2 = numeros.calculo2()
resultado3 = numeros.calculo3()

print(f"O produto do dobro do primeiro número com metade do segundo: {resultado1} \nA soma do triplo do primeiro número com o terceiro: {resultado2} \nO terceiro número elevado ao cubo: {resultado3:.2f}")
