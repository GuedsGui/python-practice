print("CONVERSÃO DE METROS-CENTÍMETROS")

class Metros:
    def __init__(self, metros):
        self.metros = metros
        
    def conversao(self):
        return self.metros * 100
        
print("Digite a quantidade de metros que quer converter para centímetros.")

metros = float(input("Metros: "))

metro = Metros(metros)

resultado = metro.conversao()

print(f"{metros} metros contém {resultado} centímetros.")
