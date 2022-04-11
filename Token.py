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