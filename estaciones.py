#ejemplo estaciones

mes = input("digite un mes del año: ");

print(f"el mes digitado fue: {mes}");

if(mes == "diciembre" or mes=="enero" or mes=="febrero" or mes=="marzo"):
    print("Estamos en Invierno")
elif(mes =="junio" or mes=="julio" or mes=="agosto"):
    print("Estamos en Verano")
elif(mes =="abril" or mes=="mayo"):
    print("Estamos en Primavera")
elif(mes == "septiembre" or mes=="octubre" or mes=="noviembre"):
    print("Estamos en Otoño")
elif(mes != "diciembre" or "enero" or "febrero" or "marzo" or "junio" or "julio" or "agosto" or "abril" or "mayo" or "septiembre" or "octubre" or "noviembre"):
    print("Error digitando el mes del año")