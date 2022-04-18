from Token import *

class Sintactico:
    tipos = Token("lexema", -1, -1, -1)
    preanalisis = tipos.DESCONOCIDO
    posicion = 0
    lista = []
    errorSintactico = False

    def __init__(self, lista):
        self.errorSintactico = False
        self.lista = lista
        tipos = Token("lexema", -1, -1, -1)
        self.lista.append(Token("#", tipos.ULTIMO, 0, 0))
        self.posicion = 0
        self.preanalisis = self.lista[self.posicion].tipo
        self.Inicio()
    

    def Match(self,tipo):
        tipos = Token("lexema", -1, -1, -1)
        if self.preanalisis != tipo:
            print(str(self.lista[self.posicion].tipo), "-- Sintactico", " -- Se esperaba "+str(tipo))
            self.errorSintactico = True
        
        if self.preanalisis != tipos.ULTIMO:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        
        if self.preanalisis == tipos.ULTIMO:
            print('Se finalizado el analisis sintactico')

    
    def Inicio(self):
        print("*** INICIO DEL ANALISIS SINTACTICO")
        tipos = Token("lexema", -1, -1, -1)
        if tipos.RESULTADO == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif tipos.JORNADA == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif tipos.GOLES == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif tipos.TABLA == self.preanalisis:
            self.Tabla()
            self.Repetir()
        elif tipos.PARTIDOS == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif tipos.TOP == self.preanalisis:
            self.Top()
            self.Repetir()
        elif tipos.ADIOS == self.preanalisis:
            self.Adios()
            self.Repetir()


    def Resultado(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.RESULTADO)
        self.Match(tipos.CADENA)
        self.Match(tipos.VS)
        self.Match(tipos.CADENA)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)

    def Jornada(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.JORNADA)
        self.Match(tipos.NUMERO)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)
        self.Match(tipos.GUION)
        self.Match(tipos.F)
        self.Match(tipos.LETRAS)
    
    def Goles(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.GOLES)
        self.Match(tipos.LETRAS)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)

    def Tabla(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.TABLA)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)
        self.Match(tipos.GUION)
        self.Match(tipos.F)
        self.Match(tipos.LETRAS)

    def Partidos(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.PARTIDOS)
        self.Match(tipos.CADENA)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)
        self.Match(tipos.GUION)
        self.Match(tipos.F)
        self.Match(tipos.LETRAS)
        self.Match(tipos.GUION)
        self.Match(tipos.JI)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.JF)
        self.Match(tipos.NUMERO)
    
    def Top(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.TOP)
        self.Match(tipos.LETRAS)
        self.Match(tipos.TEMPORADA)
        self.Match(tipos.MENOR_QUE)
        self.Match(tipos.NUMERO)
        self.Match(tipos.GUION)
        self.Match(tipos.NUMERO)
        self.Match(tipos.MAYOR_QUE)
        self.Match(tipos.GUION)
        self.Match(tipos.N)
        self.Match(tipos.NUMERO)
    
    def Adios(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.ADIOS)
    


    '''def Ancho(self):
        self.Match(TypeToken.ANCHO.name)
        self.Match(TypeToken.IGUAL.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.PUNTO_Y_COMA.name)

    def Celdas(self):
        self.Match(TypeToken.CELDAS.name)
        self.Match(TypeToken.IGUAL.name)
        self.Match(TypeToken.LLAVE_IZQUIERDA.name)
        self.Bloque_Celdas()
        self.Match(TypeToken.LLAVE_DERECHA.name)
        self.Match(TypeToken.PUNTO_Y_COMA.name)

    def Bloque_Celdas(self):
        if TypeToken.CORCHETE_IZQUIERDA.name == self.preanalisis:
            self.Cuerpo_Celda()
            self.Bloque_Celdas()
    
    def Cuerpo_Celda(self):
        self.Match(TypeToken.CORCHETE_IZQUIERDA.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.COMA.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.COMA.name)
        print("Estamos en cuerpo celda")
        self.Boleano()
        self.Match(TypeToken.COMA.name)
        self.Match(TypeToken.COLOR.name)
        self.Match(TypeToken.CORCHETE_DERECHA.name)
    
    def Boleano(self):
        self.Match(TypeToken.BOOLEANO.name)'''

    def Repetir(self):
        tipos = Token("lexema", -1, -1, -1)
        if tipos.RESULTADO == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif tipos.JORNADA == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif tipos.GOLES == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif tipos.TABLA == self.preanalisis:
            self.Tabla()
            self.Repetir()
        elif tipos.PARTIDOS == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif tipos.TOP == self.preanalisis:
            self.Top()
            self.Repetir()
        elif tipos.ADIOS == self.preanalisis:
            self.Adios()
            self.Repetir()
