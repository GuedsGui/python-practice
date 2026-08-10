print("CALCULANDO A ÁREA DO CÍRCULO")

class Area:
    def __init__(self, raio):
        self.raio = raio
        
    def calculo(self):
        return (self.raio ** 2) * 3.14
        
raio = float(input("Raio: "))
area = (raio ** 2) * 3.14

area_total = Area(raio)

resultado = area_total.calculo()

print(f"O raio tem {raio}cm e sua área é {resultado:.2f} cm².")
