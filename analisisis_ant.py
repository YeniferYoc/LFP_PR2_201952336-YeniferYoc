        '''self.contenido = ""
        self.lexico_conte = Analizador_Lexico()'''
        '''self.general_tokens = []
        self.errores_sintac_general = []
        self.fil = 0
        self.tipos = Token("lexema", -1, -1, -1)'''

        '''archi1=open('LaLigaBot-LFP.csv', "r", encoding="utf-8")
        self.contenido=archi1.read()
        archi1.close()
        self.contenido = self.contenido.replace(" ","")
        print(self.contenido)
        self.lexico_conte.analisis(self.contenido)
        self.lexico_conte.Imprimir()

        long_arr = len(self.lexico_conte.tokens_bien)
        print(long_arr)'''
        
        '''self.arreglo_elementos = []
        contador = 0
        contador2 = 0
        incrementa = 19

        #ANALIZAR INSTRUCCIONES 
        self.lexico_instruccion = Analizador_Lexico()

        for i in range(0,long_arr,incrementa+contador+contador2):
            if self.lexico_conte.tokens_bien[i].tipo == self.tipos.NUMERO:
                print("ENCONTRE DIA")
                #print(self.lexico_conte.tokens_bien[i].lexema_valido)
                if self.lexico_conte.tokens_bien[i+2].tipo == self.tipos.NUMERO:
                    print("ENCONTRE MES")
                    if self.lexico_conte.tokens_bien[i+4].tipo == self.tipos.NUMERO:
                        print("ENCONTRE AÑO")
                        if self.lexico_conte.tokens_bien[i+6].tipo == self.tipos.NUMERO:
                            print("ENCONTRE INICIO TEMPORADA")
                            if self.lexico_conte.tokens_bien[i+8].tipo == self.tipos.NUMERO:
                                print("ENCONTRE FIN TEMPORADA")
                                if self.lexico_conte.tokens_bien[i+10].tipo == self.tipos.NUMERO:
                                    print("ENCONTRE JORNADA")
                                    if self.lexico_conte.tokens_bien[i+12].tipo == self.tipos.LETRAS:
                                        print("ENCONTRE NOMBRE 1")
                                        nombre1 = ''
                                        contador = 0
                                        for j in range(i+12, long_arr):
                                            if self.lexico_conte.tokens_bien[j].tipo == self.tipos.LETRAS:
                                                nombre1 += self.lexico_conte.tokens_bien[j].lexema_valido
                                                contador += 1
                                            else:
                                                break
                                        if self.lexico_conte.tokens_bien[i+12+contador].tipo == self.tipos.COMA:
                                            print("ENCONTRE COMA")
                                            if self.lexico_conte.tokens_bien[i+12+contador+1].tipo == self.tipos.LETRAS:
                                                print("ENCONTRE NOMBRE 2")
                                                nombre2 = ''
                                                contador2 = 0
                                                for k in range(i+12+contador+1, long_arr):
                                                    if self.lexico_conte.tokens_bien[k].tipo == self.tipos.LETRAS:
                                                        nombre2 += self.lexico_conte.tokens_bien[k].lexema_valido
                                                        contador2 += 1
                                                    else:
                                                        break

                                                if self.lexico_conte.tokens_bien[i+12+contador+1+contador2].tipo == self.tipos.COMA:
                                                    print("ENCONTRE COMA")
                                                    if self.lexico_conte.tokens_bien[i+12+contador+1+contador2+1].tipo == self.tipos.NUMERO:
                                                        print("ENCONTRE GOLES 1")
                                                        if self.lexico_conte.tokens_bien[i+12+contador+1+contador2+3].tipo == self.tipos.NUMERO:
                                                            print("ENCONTRE GOLES 2")
                                                            #CREANDO EL OBJETO FECHA
                                                            fecha_nueva = Fecha(self.lexico_conte.tokens_bien[i].lexema_valido, self.lexico_conte.tokens_bien[i+2].lexema_valido, self.lexico_conte.tokens_bien[i+4].lexema_valido)
                                                            #INICIO Y FIN
                                                            inicio = self.lexico_conte.tokens_bien[i+6].lexema_valido
                                                            fin = self.lexico_conte.tokens_bien[i+8].lexema_valido
                                                            #JORNADA
                                                            jornada = self.lexico_conte.tokens_bien[i+10].lexema_valido
                                                            #OBJETOS EQUIPO
                                                            goles1 = int(self.lexico_conte.tokens_bien[i+12+contador+1+contador2+1].lexema_valido)
                                                            goles2 = int(self.lexico_conte.tokens_bien[i+12+contador+1+contador2+3].lexema_valido)
                                                            if goles1 == goles2:
                                                                equipo_nuevo = Equipo(nombre1, goles1, False,1)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, False,1)
                                                            elif goles1 < goles2:
                                                                equipo_nuevo = Equipo(nombre1, goles1, False,0)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, True,3)
                                                            else:
                                                                equipo_nuevo = Equipo(nombre1, goles1, True,3)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, False,0)
                                                            nombre1 =''
                                                            nombre2 = ''
                                                            elemento_nuevo = Elemento(fecha_nueva, inicio, fin,jornada, equipo_nuevo, equipo_nuevo2)
                                                            self.arreglo_elementos.append(elemento_nuevo)
                                                            incrementa = i+12+contador+1+contador2+3
                                                            print(incrementa)
        '''
        