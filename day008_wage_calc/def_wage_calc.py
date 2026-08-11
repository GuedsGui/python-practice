print("CALCULANDO O SALÁRIO")

def valor():
    valor_hora = float(input("Valor recebido por hora: "))
    
    return valor_hora
    
def total():
    total_hora = float(input("Horas trabalhadas no mês: "))
    
    return total_hora
    
def main():
    valor_da_hora, total_da_hora = valor(), total()
    salario = valor_da_hora * total_da_hora
    
    print(f"Seu salario mensal é R$ {salario}")
    
if __name__ == "__main__":
    main()
