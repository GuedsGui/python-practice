print("CONVERTENDO CELSIUS PARA FAHRENHEIT")

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
        
celsius = float(input("Temperatura em Celsius: "))

temperatura = Temperatura(celsius)

conversao = temperatura.fahrenheit()

print(f"Temperatura em Fahrenhei: {conversao:.2f}F°")
