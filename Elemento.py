from Fecha import *
from Equipo import *
class Elemento():
    def __init__(self,fecha, inicio, fin, jornada, equipo1, equipo2):
        self.fecha = fecha
        self.inicio = inicio
        self.fin = fin 
        self.jornada = jornada
        self.equipo = equipo1
        self.equipo2 = equipo2

    def dar_todo(self):
        print("------------------------------------------------------------------------------------------")
        self.fecha.dar_todo()

        print("INICIO --> "+str(self.inicio)+", FIN: "+str(self.fin)+", JORNADA: "+str(self.jornada))
        self.equipo.dar_todo()
        self.equipo2.dar_todo()
        