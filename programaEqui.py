from cgi import print_arguments
from equipo import *
from equipo.crearequipo import * #importo archivos de el paquete que uso para hacer las funciones
from equipo.partidos import *
equipos = []
dinero = 50 #lista para gestionar el equipo, y var para gestionar dinero in the game
cantlesiones = 0
equipo = 0 #variable que voy a usar para gestionar los otros equipos
Numvictorias = 1

while True: # while true con el que voy a correr el juego
    menu  = int(input("""
--------------------
-1 crear equipo-----     
-2 ver equipo-------
-3 enfrentamientos--
-4 curar jugadores--
-5 salir------------
--------------------


que quieres hacer --> """))
    #sentencias condicionales con base en el menu
    if menu == 1:  
        equipos.append(crear()) #agrego a la lista el metodo de el paquete
        print(f"""
============================
=se a creado el equipo {equipos[equipo][1]}=
============================

===================
=dinero - {dinero}=
===================

=equipo - {equipos[equipo][1]}=
='habilidad' - {equipos[equipo]["habilidad"]}=
=wins - {equipos[equipo]["wins"]}=
=loses - {equipos[equipo]["lose"]}=
=EMP - {equipos[equipo]["EMP"]}=
=lesiones - {equipos[equipo]["lesiones"]}=


""")
    elif menu == 2:
        print(f"""
=equipo - {equipos[equipo][1]}=
='habilidad' - {equipos[equipo]["habilidad"]}=
=wins - {equipos[equipo]["wins"]}=
=loses - {equipos[equipo]["lose"]}=
=EMP - {equipos[equipo]["EMP"]}=
=lesiones - {equipos[equipo]["lesiones"]}=
""")
    elif menu == 3:
        equipos[equipo]["lesiones"] += Numlesiones() #guardo en el dict de la lista las lesiones
        #modifico las lesiones
        resultado,puntaje = juego() #llamo el metodo juego que me retorna 2 valores para modificar las estadisticas
        if resultado == 0: #en estas cadenas de sentencias if modifico las estadisticas de resultado de los partidos
            equipos[equipo]["wins"] += puntaje
            # if Numvictorias == 0:
            #     dinero += 10
            # else:
            dinero += Numvictorias * 10 #forma en la que se añade dinero por victoria, este se multiplica si las victorias son seguidas
        elif resultado == 1:
            equipos[equipo]["lose"] += puntaje
        elif resultado == 2:
            equipos[equipo]["EMP"] += puntaje
    elif menu == 4: #opcion para curar jugadores
        if equipos[equipo]["lesiones"] == 0: # esto es por si no tiene lesiones el prb
            print("tu equipo no tiene lesiones no puedes curar nada")
        if equipos[equipo]["lesiones"] > 0: # pa cuando tiene lesiones
            curarse = input("quieres curar a tus jugadores: ") 
            print(f"curar a cada jugador cuesta 10 :3 y tienes {dinero}")

            if curarse.lower() == "si" and dinero > 0: #cumpruebo si quiere curar a los jugadores y si tenfo plata para eso
                print("tienes {} lesionados y {}".format(equipos[equipo]["lesiones"],dinero)) 
                Numdejugadores = int(input("cuantos jugadores quieres curar? -->")) #esta variable la uso pa saber cuantos jugadores quiere curar
                equipos[equipo]["lesiones"] -= Numdejugadores #quito las lesiones del dict
                dinero -= Numdejugadores * 10 # resto el dinero por curar lesiones
            #if equipos[equipo]["lesiones"] == 0:
                print("has curado a {} jugadores y has utilizado {} de dinero, tienes {} jugadores lesionados y {} de dinero".format(Numdejugadores,Numdejugadores * 10,equipos[equipo]["lesiones"],dinero))

            elif curarse.lower() == "si" and dinero == 0: #este condicional lo uso para el caso en que no tenga dinero
                print("tienes {} jugadores lesionados pero no tienes dinero, no puedo ayudarte bay".format(equipos[equipo]["lesiones"]))
    elif menu == 5:
        print(f"hasta luego gracias por jugar tu quipo te esperara en el cielo")
        break
    else:
        print("la opcion no esta disponible")