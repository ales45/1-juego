from collections import OrderedDict # importo un diccinario ordenado y la el modulo ramdon
import random

fin = "no" #variable para asegurar que se entre a el ciclo y gestinar cuando se cree o no el equipo
def crear():
    while True:
        equipo = sum(random.sample(range(1,9),6))
        equipo2 = sum(random.sample(range(1,9),5))
        equipo += equipo2 #con el metodo ramdon sumo dos listas con valores creados aleatoria mente
        Numequipo = 1
        fin = input("\nquieres crear un equipo -->")
        if fin.lower() == "si" or fin.lower() == "shi":
            equipos = OrderedDict()
            NOmbre = input("\ncomo se llama el equipo -->")
            equipos[Numequipo] = NOmbre
            equipos["habilidad"] = equipo #se le da el valor de el equipo que se creo anterior mente
            equipos["wins"] = 0 
            equipos["lose"] = 0
            equipos["EMP"] = 0
            equipos["lesiones"] = 0 
            return equipos   # retorno de el metodo que uso para añadir el equipo
        if fin.lower == "no": 
            break #se gentiona el fin de el ciclo
        else:
            print("opcion no disponible")
    
    
        
    