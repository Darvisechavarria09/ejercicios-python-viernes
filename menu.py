import math

opcion = 1
while(opcion != 0):
    #pregunte por la opcion
    print("")
    print("")
    print("")
    print("0. Salida")
    print("1: Encuentre si el número es múltiplo de 2")
    print("2: Encuentre la raíz cuadrada del número")
    print("3: Sume 100 al número ingresado")
    print("4: Eleve a la 2 el número ingresado")
    print("****")
    opcion =int(input("Digite una opcion: "));
    if(opcion==1):
        numero=int(input("digite el numero a determinar si es multiplo de 2: "))
        if(numero % 2==0):
            print(f"El numero {numero} SI es multiplo de 2")
        else:
            print(f"El numero {numero} NO es multiplo de 2")

    elif(opcion==2):
        numero=int(input("/RAIZ CUADRADA/ digite el numero a calcular: "))
        raiz=math.sqrt(numero)
        print(f"la raiz de {numero} es {raiz}")
    elif(opcion==3):
        numero=int(input("digite un numero para sumarle 100: "))
        suma=numero+100
        print(f"La suma final es: {suma}")
    elif(opcion==4):
        numero=int(input("digite el numero a elevar: "))
        exponente=2
        potencia=int(math.pow(numero,exponente))
        print(f"El numero {numero} elevado a la 2 es: {potencia}")
    else:
        print("INVALIDO")