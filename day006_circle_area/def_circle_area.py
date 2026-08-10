print("CALCULANDO A ÁREA DO CÍRCULO")

def raio():
    raio = float(input("Raio: "))
    return raio
    
def area():
    raio1 = raio()
    area = (raio1 ** 2) * 3.14
    
    return raio1, area
    
def main():
    raio1, area_total = area()
    print(f"O raio tem {raio1}cm e sua area {area_total:.2f}cm².")
    
if __name__ == "__main__":
    main()
