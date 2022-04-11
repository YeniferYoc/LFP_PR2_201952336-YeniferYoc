from Token import Token

class Analizador_Lexico():
    lexema = ''
    tokens= []
    tokens_bien = []
    tokens_errorres= []
    estado = 1
    fila = 1
    columna = 1
    generar = False

    def analisis(self,entrada):
        self.estado = 1
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 1
        self.error = True
        tipos = Token("lexema", -1, -1, -1)
        #print(entrada)

        entrada = entrada + '#'
        #print(entrada)
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            #print("["+actual+"]")
            #print(str(self.estado)+"estasdo")
            
            if self.estado == 1:
                #print("entro"+str(i))
                if actual.isalpha():
                    #print(actual)
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 5
                    self.columna += 1
                    continue
                elif actual == '-':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.GUION)
                    continue
                elif actual == '>':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.MAYOR_QUE)
                    continue
                elif actual == '<':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.MENOR_QUE)
                    continue
                elif actual == '/':
                    self.columna += 1
                    self.lexema += actual
                    self.AgregarToken(tipos.DIAGONAL)
                    continue
                elif actual == ',':
                    self.columna +=1
                    self.lexema += actual
                    self.AgregarToken(tipos.COMA)
                    continue
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                    #continue
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                    continue
                elif actual =='\r':
                    self.estado = 1
                    continue
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                    continue
                elif actual == '#' and i ==longitud - 1:
                    print('EL ANALIZADOR LEXICO HA TERMINADO')
                    continue
                else:
                    self.lexema += actual
                    self.columna += 1
                    self.AgregarToken(tipos.DESCONOCIDO)
                    
                    self.error = False
                    print("ERROR")
                    continue
                
            
            #MANEJRAR LETRAS
            elif self.estado == 4:
                #print("entro")
                #print(actual)
                if actual.isalpha():
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    if self.RESERVADA():
                        self.AgregarToken(tipos.PALABRA_RESERVADA)
                        if actual == '<':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.DOS_PUNTOS)
                            #continue
                        elif actual == ' ':
                            self.columna +=1
                            self.estado = 1
                            #continue
                        elif actual == '\n':
                            self.fila += 1
                            self.estado = 1
                            self.columna = 1
                            
                        elif actual =='\r':
                            self.estado = 1
                            
                        elif actual == '\t':
                            self.columna += 5
                            self.estado = 1
                            continue
                        #print(i)
                        continue
                    else:
                        print(i)
                        print("["+actual+"]")
                        self.AgregarToken(tipos.DESCONOCIDO)  
                        if actual == '\n':
                            self.fila += 1
                            self.estado = 1
                            self.columna = 1
                            continue
                        elif actual == '>':
                            self.columna +=1
                            self.lexema += actual
                            self.AgregarToken(tipos.MAYOR_QUE)
                            continue
                        elif actual == '<':
                            self.columna += 1
                            self.lexema += actual
                            self.AgregarToken(tipos.MENOR_QUE)
                            continue
                        elif actual == ',':
                            self.columna +=1
                            self.lexema += actual
                            self.AgregarToken(tipos.COMA)
                            continue
                        else:
                            self.lexema += actual
                            self.AgregarToken(tipos.DESCONOCIDO)
                            self.columna += 1
                            self.error = False
                            print("ERROR")
                            continue
                        i -= 1
                        print(i)
                        continue
            
            #ESTADO PARA MANEJAR NUMEROS
            elif self.estado == 3:
                if actual.isdigit():
                    self.estado = 3    
                    self.columna += 1
                    self.lexema += actual
                    continue

                else:
                    if actual == '-':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.GUION)
                            continue
                    elif actual == '<':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.MENOR_QUE)
                            continue
                    elif actual == '>':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.MAYOR_QUE)
                            continue
                    elif actual == '/':
                            self.lexema += actual
                            self.columna += 1
                            self.AgregarToken(tipos.DIAGONAL)
                            continue
                    else:
                        self.lexema = actual
                        self.columna += 1
                        self.AgregarToken(tipos.DESCONOCIDO)
                    continue 
                     
            #ESTADO DE CADENAS
            elif self.estado == 5:
                if actual != '"':
                    self.estado = 5
                    self.columna +=1
                    self.lexema += actual
                    continue
                elif actual == '"':
                     
                    self.AgregarToken(tipos.CADENA)
                    self.columna +=1
                    if actual == '\n':
                            self.fila += 1
                            self.estado = 1
                            self.columna += 1
                            continue
                    elif actual == ' ':
                            self.estado = 1
                            self.columna += 1
                            continue
                    elif actual == '\t':
                            self.estado = 1
                            self.columna += 5
                            continue
                    continue
            


    def AgregarToken(self,tipo):
        nuevo_token = Token(self.lexema, tipo, self.fila, self.columna)
        tipos = Token("lexema", -1, -1, -1)
        if nuevo_token.tipo != tipos.DESCONOCIDO:
            self.tokens_bien.append(nuevo_token)
        else:
            self.tokens_errorres.append(nuevo_token)
        self.tokens.append(nuevo_token)
        self.lexema = ""
        self.estado = 1
        
    def RESERVADA(self):
        entrada = self.lexema.upper() #convertir todo a minuscula
        si_es = False
        palabras_reservadas = ["RESULTADO","VS","TEMPORADA","JORNADA","GOLES", "LOCAL", "VISITANTE", "TOTAL", "TABLA","PARTIDOS", "TOP","SUPERIOR", "INFERIOR", "ADIOS", "f", "ji","jf"]
        
        if entrada in palabras_reservadas:
            si_es = True
        
        return si_es

    def Imprimir(self):
        print("---------------------------------------------LISTA DE TOKENS ---------------------------------------------")
        #print("entro imprimir")
        tipos = Token("lexema", -1, -1, -1)
        contador = 0
        #print(len(self.tokens))
        for token in self.tokens:
            #print(contador)
            if token.tipo != tipos.DESCONOCIDO:
                #print(contador)
                print("LEXEMA: "+token.getLexema()," TIPO: ",token.getTipo(),' LINEA: ',token.getFila(), ', COLUMNA: ',token.getColumna())
                print("---------------------------------------------------------------------")
    
    def ImprimirErrores(self):
        print("--------------------------------------------- LISTA DE ERRORES ---------------------------------------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.DESCONOCIDO:
                #self.tokens_errorres.append(x)
                print("LEXEMA: "+x.getLexema()," ENCONTRADO EN: LINEA: ",x.getFila(), ', COLUMNA: ',x.getColumna(),'--> Error Lexico')
                print("---------------------------------------------------------------------")

#ultimo