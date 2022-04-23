from sys import float_repr_style


class Equipo():
    def __init__(self,nombre, goles , ganador, puntos):
        self.nombre = nombre
        self.goles = goles
        self.ganador = ganador 
        self.puntos = puntos

    def dar_todo(self):
        print("NOMBRE "+self.nombre+", goles: "+str(self.goles)+", ganador: "+str(self.ganador))