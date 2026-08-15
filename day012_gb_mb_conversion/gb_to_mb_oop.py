print("CONVERSÃO DE GIGABYTES PARA MEGABITES")

class Gigabytes:
    def __init__(self, gigabytes):
        self.gigabytes = gigabytes
        
    def converter(self):
        return self.gigabytes * 1024
        
gigabytes = float(input("Gigabytes: "))

gigas = Gigabytes(gigabytes)

conversao = gigas.converter()

print(f"{gigabytes}GB contém {conversao:.2f}MB.")
