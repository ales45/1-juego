from equipo import *
from equipo.crearequipo import * #importo archivos de el paquete que uso para hacer las funciones
from equipo.partidos import *
equipos = []
dinero = 50 #lista para gestionar el equipo, y var para gestionar dinero in the game
cantlesiones = 0
equipo = 0
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
=se a creado el equipo {equipos[0][1]}=
============================

===================
=dinero - {dinero}=
===================

=equipo - {equipos[0][1]}=
='habilidad' - {equipos[0]["habilidad"]}=
=wins - {equipos[0]["wins"]}=
=loses - {equipos[0]["lose"]}=
=EMP - {equipos[0]["EMP"]}=
=lesiones - {equipos[0]["lesiones"]}=


""")
    if menu == 2:
        print(f"""
=equipo - {equipos[0][1]}=
='habilidad' - {equipos[0]["habilidad"]}=
=wins - {equipos[0]["wins"]}=
=loses - {equipos[0]["lose"]}=
=EMP - {equipos[0]["EMP"]}=
=lesiones - {equipos[0]["lesiones"]}=
""")
    if menu == 3:
        equipos[0]["lesiones"] += Numlesiones() #guardo en el dict de la lista las lesiones
        #modifico las lesiones
        resultado,puntaje = juego() #llamo el metodo juego que me retorna 2 valores para modificar las estadisticas
        if resultado == 0: #en estas cadenas de sentencias if modifico las estadisticas de resultado de los partidos
            equipos[0]["wins"] += puntaje
            # if Numvictorias == 0:
            #     dinero += 10
            # else:
            dinero += Numvictorias * 10 #forma en la que se añade dinero por victoria, este se multiplica si las victorias son seguidas
        elif resultado == 1:
            equipos[0]["lose"] += puntaje
        elif resultado == 2:
            equipos[0]["EMP"] += puntaje
    if menu == 4:
        pass
    if menu == 5:
        print(f"hasta luego gracias por jugar tu quipo te esperara en el cielo")
        break
    else:
        print("la opcion no esta disponible")