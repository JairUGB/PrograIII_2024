'''i=1
while i<=10:
    resultado = 2*i
    print(f"2x{i} = {resultado}")
    i+=1'''

while True:
    numero = int(input("Digite que desea para multiplicar: "))
    i = 1
    while i<=10:
        print(f"{numero} x {i} = {numero*i}")
        i+=1
        op=input("Seleccione una opcion:\n"+ 
                 "1-Pedir otro numero\n"+ 
                 "2-Salir\n")
        
        if (op=="1"):
            continue
        elif(op=="2"):
            break
        else:
            print("Opcion incorrecta")