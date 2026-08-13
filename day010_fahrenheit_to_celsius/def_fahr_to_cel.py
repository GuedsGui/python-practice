print("CONVERTENDO CELSIUS PARA FAHRENHEIT")

def celsius():
    celsius = float(input("Temperatura em Celsius: "))
    
    return celsius

def main():
    cel = celsius()
    fahrenheit = (cel * 9/5) + 32
    
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}F°")

if __name__ == "__main__":
    main()
