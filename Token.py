class Token():
    lexema_valido = ''
    tipo = 0
    fila = 0
    columna = 0

    PALABRA_RESERVADA = 1
    NUMERO = 2
    DIAGONAL = 3
    COMA = 4
    GUION = 5
    DESCONOCIDO = 6
    LETRAS = 7
    CADENA = 8
    MAYOR_QUE = 9
    MENOR_QUE = 10
    ULTIMO = 11
    RESULTADO = 12
    VS = 13
    TEMPORADA = 14
    JORNADA = 15
    F = 16
    GOLES = 17
    '''LOCAL = 18
    VISITANTE = 19
    TOTAL = 20'''
    TABLA = 21
    PARTIDOS = 22
    JI = 23
    JF = 24
    TOP = 25
    '''SUPERIOR = 26
    INFERIOR = 27'''
    N = 28
    ADIOS = 29

    def __init__(self,lexema,tipo,fila,columna):
        self.lexema_valido = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema_valido

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
#ultimo
    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA_RESERVADA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.DIAGONAL:
            return 'DIAGONAL'
        elif self.tipo == self.COMA:
            return 'COMA'
        elif self.tipo == self.GUION:
            return 'GUION'
        elif self.tipo == self.NUMERO:
            return "NUMERO"
        elif self.tipo == self.LETRAS:
            return "LETRAS"
        elif self.tipo == self.DESCONOCIDO:
            return "DESCONOCIDO"
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.MAYOR_QUE:
            return 'MAYOR QUE'
        elif self.tipo == self.MENOR_QUE:
            return "MENOR QUE"
        elif self.tipo == self.ULTIMO:
            return "ULTIMO"
        elif self.tipo == self.RESULTADO:
            return 'RESULTADO'
        elif self.tipo == self.VS:
            return 'VS'
        elif self.tipo == self.TEMPORADA:
            return 'TEMPORADA'
        elif self.tipo == self.JORNADA:
            return 'JORNADA'
        elif self.tipo == self.F:
            return "F"
        elif self.tipo == self.GOLES:
            return "GOLES"
        elif self.tipo == self.LOCAL:
            return "LOCAL"
        elif self.tipo == self.VISITANTE:
            return 'VISITANTE'
        elif self.tipo == self.TOTAL:
            return 'TOTAL'
        elif self.tipo == self.MENOR_QUE:
            return "TABLA"
        elif self.tipo == self.ULTIMO:
            return "PARTIDOS"
        elif self.tipo == self.JI:
            return 'JI'
        elif self.tipo == self.JF:
            return 'JF'
        elif self.tipo == self.TOP:
            return 'TOP'
        elif self.tipo == self.SUPERIOR:
            return 'SUPERIOR'
        elif self.tipo == self.INFERIOR:
            return "INFERIOR"
        elif self.tipo == self.N:
            return "N"
        elif self.tipo == self.ADIOS:
            return "ADIOS"