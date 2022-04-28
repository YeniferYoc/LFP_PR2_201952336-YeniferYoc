from Token import *
from Error_sintatico import *
class Sintactico:
    tipos = Token("lexema", -1, -1, -1)
    preanalisis = tipos.DESCONOCIDO
    posicion = 0
    lista = []
    errorSintactico = False
    lista_err_S = []
    

    def __init__(self, lista, cadena):
        self.cadena = cadena
        self.errorSintactico = False
        self.lista = lista
        tipos = Token("lexema", -1, -1, -1)
        self.lista.append(Token("#", tipos.ULTIMO, 0, 0))
        self.posicion = 0
        self.lista_err_S = []
        self.preanalisis = self.lista[self.posicion].tipo
        self.Inicio()
    
    def Match(self,tipo):
        tipos = Token("lexema", tipo, -1, -1)
        if self.preanalisis != tipo:
            
            print(str(self.lista[self.posicion].getTipo()), "-- Sintactico", " -- Se esperaba "+str(tipos.getTipo()))
            nuevo_err = Error_Sintactico(self.lista[self.posicion].getTipo(),tipos.getTipo(),self.cadena)
            self.lista_err_S.append(nuevo_err)
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
        self.Archivo()
        
    def Goles(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.GOLES)
        self.Match(tipos.LETRAS)
        self.Match(tipos.CADENA)
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
        self.Archivo()

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
        self.Archivo()
        self.A_partir()
        self.Hasta()
    
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
        self.Cuantos
    
    def Adios(self):
        tipos = Token("lexema", -1, -1, -1)
        self.Match(tipos.ADIOS)

    def Archivo(self):
        tipos = Token("lexema", -1, -1, -1)
        if tipos.GUION == self.preanalisis:
            self.Match(tipos.GUION)
            if tipos.F == self.preanalisis:
                self.Match(tipos.F)
                self.Match(tipos.LETRAS)
    
    def A_partir(self):
        tipos = Token("lexema", -1, -1, -1)
        if tipos.GUION == self.preanalisis:
            self.Match(tipos.GUION)
            if tipos.JI == self.preanalisis:
                self.Match(tipos.JI)
                self.Match(tipos.NUMERO)
        
    def Hasta(self):
        tipos = Token("lexema", -1, -1, -1)
        if tipos.GUION == self.preanalisis:
            self.Match(tipos.GUION)
            if tipos.JF == self.preanalisis:
                self.Match(tipos.JF)
                self.Match(tipos.NUMERO)

    def Cuantos(self):
        tipos = Token("lexema", -1, -1, -1)
        if tipos.GUION == self.preanalisis:
            self.Match(tipos.GUION)
            if tipos.N == self.preanalisis:
                self.Match(tipos.N)
                self.Match(tipos.NUMERO)

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
