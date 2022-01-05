from equipo import *
from equipo.crearequipo import * #importo archivos de el paquete que uso para hacer las funciones
equipos = []
dinero = 50 #lista para gestionar el equipo, y var para gestionar dinero in the game


while True: # while true con el que voy a correr el juego
    menu  = int(input("""
--------------------
-1 crear equipo-----     
-2 ver equipos------
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
    