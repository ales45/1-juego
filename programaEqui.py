from equipo import *
from equipo.crearequipo import * #importo archivos de el paquete que uso para hacer las funciones
from equipo.partidos import *
equipos = []
dinero = 50 #lista para gestionar el equipo, y var para gestionar dinero in the game
cantlesiones = 0


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
        equipos[0]["lesiones"] += Numlesiones()
        resultado,puntaje = juego()
        if resultado == 0:
            equipos[0]["wins"] += puntaje
        if resultado == 1:
            equipos[0]["lose"] += puntaje
        if resultado == 2:
            equipos[0]["EMP"] += puntaje
    if menu == 5:
        print(f"hasta luego gracias por jugar tu quipo te esperara en el cielo")
        break