print("CONVERSÃO DE GIGABYTES PARA MEGABYTES")

def gb():
    gigabytes = float(input("Gigabytes: "))

    return gigabytes
    
def main():
    giga = gb()
    megabites = giga * 1024

    print(f"{giga}GB contém {megabites:.2f}MB.")
    
if __name__ == "__main__":
    main()
