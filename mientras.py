import math

#declaro el bucle/ciclo/iteracion/repeticion/la vuelta/loop

#variable controladora
opcion = 1
while(opcion != 0):
    #pregunte por la opcion
    print("empanadas el machetico")
    print("****")
    print("0. digita 0 para salir")
    print("1. digita 1 para calcular cuadrada de un #")
    print("2. digite 2 para calcular la potencia de un #")
    print("****")
    opcion =int(input("Digite una opcion: ")) ;
    if(opcion==1):
        numero=int(input("/RAIZ CUADRADA/ digite el numero a calcular: "))
        raiz=float(math.sqrt(numero))
        print(f"la raiz de {numero} es {raiz}")
    elif(opcion==2):
        numero=int(input("/POTENCIA/ digite el numero a calcular: "))
        exponente=int(input("digite el exponente: "))
        potencia=int(math.pow(numero,exponente))
        print(f"la potencia de {numero} es {potencia}")
    else:
        print("INVALIDO")
