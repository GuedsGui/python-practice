print("Calculando Fahrenheit em Celsius")

def fahrenheit():
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    
    return fahrenheit

def main():
    fahr = fahrenheit()
    celsius = 5 * ((fahr-32) / 9)

    print(f"Temperatura em Celsius: {celsius:.2f}C°")
    
if __name__ == "__main__":
    main()
