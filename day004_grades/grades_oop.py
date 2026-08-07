print("MÉDIA DO ALUNO")

class Notas:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    def media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
    
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

calculo = Notas(nota1, nota2, nota3, nota4)

resultado = calculo.media()

print(f"Primeira nota: {nota1:.2f} \nSegunda nota: {nota2:.2f} \nTerceira nota: {nota3:.2f} \nQuarta nota: {nota4:.2f} \nMédia: {resultado:.2f}")
