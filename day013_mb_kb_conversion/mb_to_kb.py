print("CONVERSÃO DE GIGABYTES PARA MEGABYTES e KILOBYTES")

gigabytes = float(input("Gigabytes: "))
megabites = gigabytes * 1024
kilobytes = megabites * 1024

print(f"{gigabytes}GB contém: \n{megabites:.2f}MB. \n{kilobytes:.2f}KB.")
