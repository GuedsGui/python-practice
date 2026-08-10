print("CÁLCULO DO DOBRO DA ÁREA DO QUADRADO")

def lado():
    valor_lado = float(input("Digite o lado do quadrado: "))

    return valor_lado

def area():
    lado_quadrado = lado()
    area_quadrado = lado_quadrado ** 2

    return lado_quadrado, area_quadrado

def main():
    lado_quadrado, area_quadrado = area()
    dobro_area = area_quadrado * 2

    print(f"O lado possui {lado_quadrado:.2f}cm, a área possui {area_quadrado:.2f}cm2 e seu dobro é {dobro_area:.2f}cm2.")

    return lado_quadrado, area_quadrado, dobro_area

if __name__ == "__main__":
    main()
