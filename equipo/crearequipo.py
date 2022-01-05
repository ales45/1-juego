from collections import OrderedDict
import random

fin = "no"
def crear():
    while True:
        equipo = sum(random.sample(range(1,9),6))
        equipo2 = sum(random.sample(range(1,9),5))
        equipo += equipo2 #
        Numequipo = 1
        fin = input("\nquieres crear un equipo -->")
        if fin.lower() == "si":
            equipos = OrderedDict()
            NOmbre = input("\ncomo se llama el equipo -->")
            equipos[Numequipo] = NOmbre
            equipos["habilidad"] = equipo
            equipos["wins"] = 0
            equipos["lose"] = 0
            equipos["EMP"] = 0
            equipos["lesiones"] = 0
            return equipos   # retorno de el metodo que uso para añadir el equipo
        if fin.lower == "no":
            break
        else:
            print("opcion no disponible")
    
    
        
    