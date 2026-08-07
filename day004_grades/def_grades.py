print("MÉDIA DO ALUNO")

def notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    
    media = (nota1 + nota2 + nota3 + nota4) / 4 
    
    return nota1, nota2, nota3, nota4, media

def main():
    nt1, nt2, nt3, nt4, md = notas()
    
    print(f"Primeira nota: {nt1:.2f} \nSegunda nota: {nt2:.2f} \nTerceira nota: {nt3:.2f} \nQuarta nota: {nt4:.2f} \nMédia: {md:.2f}")
    
if __name__ == "__main__":
    main()
    
