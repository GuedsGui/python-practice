print("CALCULANDO O SALÁRIO")

class Salario:
    def __init__(self, valor_hora, total_hora):
        self.valor_hora = valor_hora
        self.total_hora = total_hora
        
    def salario_mensal(self):
        return self.valor_hora * self.total_hora
        
valor_hora = float(input("Valor recebido por hora: "))
total_hora = float(input("Horas trabalhadas no mês: "))

salario = Salario(valor_hora, total_hora)

salario_mensal = salario.salario_mensal()

print(f"Seu salário mensal é R$ {salario_mensal}.")
