import numbers
from unicodedata import numeric


edad = int(input("digite su edad: "));

if(edad >0 and edad <=14):
    print("Eres un NIÑO")
elif(edad >= 15 and edad <=28):
    print("Eres un JOVEN")
elif(edad >= 28 and edad <=60):
    print("Eres un ADULTO")
elif(edad > 60):
    print("Eres un ADULTO MAYOR")