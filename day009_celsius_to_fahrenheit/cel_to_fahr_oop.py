print("Calculando Fahrenheit em Celsius")

class Temperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
        
    def celsius(self):
        return 5 * ((fahrenheit-32) / 9)
        
fahrenheit = float(input("Temperatura em Fahrenheit: "))

temperatura = Temperatura(fahrenheit)

conversao = temperatura.celsius()

print(f"Temperatura em Celsius: {conversao:.2f}C°")
