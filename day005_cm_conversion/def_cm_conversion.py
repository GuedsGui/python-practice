print("CONVERSÃO DE METROS-CENTÍMETROS")

def conversao():
    metros = float(input("Metros: "))
    centimetros = metros * 100
    conversao = centimetros
    
    return metros, centimetros, conversao
    
def main():
    metragem, centimetros_convertidos, resultado = conversao()
    print(f"{metragem} metros contém {resultado} centímetros.")
    
if __name__ == "__main__":
    print("Digite a quantidade de metros que quer converter para centímetros.")
    main()
    
