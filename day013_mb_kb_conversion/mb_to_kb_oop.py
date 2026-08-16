print("CONVERSÃO DE GIGABYTES PARA MEGABITES E KILOBYTES")

class Gigabytes:
    def __init__(self, gigabytes):
        self.gigabytes = gigabytes
        
    def converter_gb_mb(self):
        return self.gigabytes * 1024
        
    def converter_mb_kb(self):
        return self.gigabytes * 1024 * 1024
        
gigabytes = float(input("Gigabytes: "))

gigas = Gigabytes(gigabytes)

conversao1 = gigas.converter_gb_mb()
conversao2 = gigas.converter_mb_kb()

print(f"{gigabytes}GB contém: \n{conversao1:.2f}MB. \n{conversao2:.2f}KB.")
