opcion = 1
suma=0
while(opcion < 0):

    print("Digita un numero negativo para salir del programa")
    opcion = int(input("Digite una opcion: "));
    if(opcion > 0):
        
        suma=suma+opcion
        print(f"sumando: {suma}")
    else:
        print("salimos del programa")