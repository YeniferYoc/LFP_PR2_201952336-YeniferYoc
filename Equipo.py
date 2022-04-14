from sys import float_repr_style


class Equipo():
    def __init__(self,nombre, goles , ganador):
        self.nombre = nombre
        self.goles = goles
        self.ganador = ganador 

    def dar_todo(self):
        print("NOMBRE "+self.nombre+", goles: "+str(self.goles)+", ganador: "+str(self.ganador))