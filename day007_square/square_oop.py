print("CÁLCULO DO DOBRO DA ÁREA DO QUADRADO")

class Quadrado:
    def __init__(self, lado, area):
        self.lado = lado
        self.area = area
        
    def dobro_area(self):
        return self.area * 2
        
lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2

quadrado = Quadrado(lado, area)

calculo = quadrado.dobro_area()
    
print(f"O lado possui {lado:.2f}cm, a área possui {area:.2f}cm2 e seu dobro é {calculo:.2f}cm2.")
