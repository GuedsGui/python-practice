print("CONVERSÃO DE GIGABYTES PARA MEGABYTES")

def gb():
    gigabytes = float(input("Gigabytes: "))

    return gigabytes
    
def mb(gigabytes):
    megabytes = gigabytes * 1024
    
    return megabytes
    
def main():
    giga = gb()
    mega = mb(giga)
    kilobytes = mega * 1024

    print(f"{giga}GB contém: \n{mega:.2f}MB. \n{kilobytes:.2f}KB.")
    
if __name__ == "__main__":
    main()
