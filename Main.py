from gc import disable
import tkinter
from tkinter import *
from tkinter.ttk import LabelFrame
from turtle import bgcolor
from Cargar_arch import cargar
from tkinter import Tk, messagebox as mb
from tkinter.simpledialog import *
from os import startfile
from Elemento import Elemento
from Token import *
from Lexico_csv import Analizador_Lexico
from Elemento import *
from Fecha import *
from tkinter import ttk
import tkinter as tk
from Equipo import *
from Error_sintatico import *
from Sintactico import Sintactico
#import ventana_analizar
#from  ventana_reportes import *
class Todo():
    
    def __init__(self):
        self.general_tokens_bien = []
        self.general_tokens_err = []
        self.errores_sintac_general = []
        self.fil = 0
        self.tipos = Token("lexema", -1, -1, -1)
        self.lexico_instruccion = Analizador_Lexico()
        self.arreglo_elementos = []#LaLigaBot-LFP
        nombre_archivo_csv = "original.csv"
        with open(nombre_archivo_csv, "r", encoding='utf-8') as archivo:
            
            next(archivo, None)
            for linea in archivo:
                linea = linea.replace("-",",")
                
                lista = linea.split(",")
                
                fecha = str(lista[0])
                inicio = int(lista[1])
                fina = int(lista[2])
                jornada = int(lista[3])
                equipo1 = str(lista[4])
                equipo2 = str(lista[5])
                goles1 = int(lista[6])
                goles2 = int(lista[7])
                
                if goles1 == goles2:
                    equipo_nuevo = Equipo(equipo1, goles1, False,1)
                    equipo_nuevo2 = Equipo(equipo2, goles2, False,1)
                elif goles1 < goles2:
                    equipo_nuevo = Equipo(equipo1, goles1, False,0)
                    equipo_nuevo2 = Equipo(equipo2, goles2, True,3)
                else:
                    equipo_nuevo = Equipo(equipo1, goles1, True,3)
                    equipo_nuevo2 = Equipo(equipo2, goles2, False,0)
                
                
                elemento_nuevo = Elemento(fecha, inicio, fina,jornada, equipo_nuevo, equipo_nuevo2)
                self.arreglo_elementos.append(elemento_nuevo)
        archivo.close()
        '''cont = 0
        for elemento in self.arreglo_elementos:
            elemento.dar_todo()
            cont +=1
        print("")
        print(cont)'''
                                                            
        #INTERFAZ GRAFICA
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("La Liga Bot")
        self.ventana_principal.geometry("850x575")
        self.ventana_principal.configure(bg="cyan")
        self.ventana_principal.resizable(False, False)

       

        '''panel = LabelFrame(self.ventana_principal)

        mycanvas = Canvas(panel)
        mycanvas.pack(side = LEFT)

        yscrollbar = tkinter.Scrollbar(panel, orient = "vertical", command = mycanvas.yview)
        yscrollbar.pack(side = RIGHT, fill = "y")

        myFrame = Frame(mycanvas)
        myFrame.pack()
        
        self.entrada_w = tkinter.Entry(myFrame, font=("Comic Sans MS", 15,"bold"))
        self.entrada_w.pack()
        
        panel.pack(fill = "both", expand="yes", padx=10, pady= 10)
        panel.configure(bg = "white")'''
        
       
        
        '''etiqueta = tkinter.Label(self.ventana_principal, width=85, height=33, background="white")
        etiqueta.place(x = 6, y = 5)'''
        '''panel = LabelFrame(self.ventana_principal)
        panel.place(x = 0, y = 0)
        panel.pack(fill = 'both', side=LEFT)
        
        panel.configure(bg = "cyan")'''
        '''self.canvas1=tk.Canvas(self.ventana_principal, width=600, height=500, background="cyan")
        self.canvas1.pack(expand="no")
        
        self.canvas1.place(x = 6,y =5)

        self.mycanvas =tk.Canvas(self.canvas1, width=600, height=500, background="white")
        self.mycanvas.place(x = 0, y = 0)
        self.mycanvas.pack(side = LEFT)

        yscrollbar = tkinter.Scrollbar(self.canvas1, orient = "vertical", command = self.mycanvas.yview)
        yscrollbar.pack(side = RIGHT, fill = "y")'''

        #self.mycanvas.configure(yscrollcommand=yscrollbar.set)

        def _on_frame_configure(self, event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
        self.frame = Frame(self.ventana_principal, borderwidth=2, relief=SUNKEN, background="white")
        self.frame.grid(column=0, row=0, sticky=N+S+E+W)


        yscrollbar = Scrollbar(self.frame)
        yscrollbar.grid(column=1, row=0, sticky=N+S)

        hscrollbar = Scrollbar(self.frame, orient=HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky=E+W)

        canvas = Canvas(self.frame, bd=0, yscrollcommand=yscrollbar.set,xscrollcommand=hscrollbar.set,width=585, height=500)
        canvas.grid(column=0, row=0, sticky=N+S+E+W)

        yscrollbar.config(command=canvas.yview)
        hscrollbar.config(command=canvas.xview)


        

        self.frame = Frame(canvas, borderwidth=2, relief=SUNKEN, background="white",width=585, height=500)
        canvas.create_window(4, 4, window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", _on_frame_configure)


        label_entrada = ttk.Label(self.frame, text="Bienvenido a la Liga Bot, Ingrese un comando", background="light gray",font=("Comic Sans MS", 15,"bold"))
        label_entrada.grid(column=1, row=self.fil, sticky=W)
        self.fil += 1
        
        '''self.mycanvas=tk.Canvas(self.ventana_principal, width=600, height=500, background="white")
        self.mycanvas.place(x = 6,y =5)'''

        '''yscrollbar = tkinter.Scrollbar(self.ventana_principal, orient = "vertical", command = self.canvas1.yview)
        yscrollbar.place(x = 0, y = 0)
        yscrollbar.pack(side = RIGHT, fill = "y")'''
        
        boton_err = tkinter.Button(self.ventana_principal, text = "Reporte de errores", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white" , command= lambda: self.opcion_elegida(1) )
        boton_limp_log_err = tkinter.Button(self.ventana_principal, text = "Limpiar Log de errores", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(2))
        boton_rep_tok = tkinter.Button(self.ventana_principal, text = "Reporte de tokens", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(3))
        boton_limpia_tok = tkinter.Button(self.ventana_principal, text = "Limpiar log de tokens", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(4))
        boton_usu = tkinter.Button(self.ventana_principal, text = "Manual de usuario", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(5))
        boton_tec = tkinter.Button(self.ventana_principal, text = "Manual Tecnico", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(6))
        
        etiqueta = tkinter.Label(self.ventana_principal, text = " ", background="white",font=("Comic Sans MS", 14,"bold"),width=10)
        etiqueta.place(x = 0, y = 525)

        self.caja_texto = tkinter.Entry(self.ventana_principal, font=("Comic Sans MS", 15,"bold"), width=50)
        self.caja_texto.insert(0, "Hola mundo!")
        self.caja_texto.place(x = 6, y = 525)
        

        self.boton_enviar = tkinter.Button(self.ventana_principal, text = "<ENVIAR>", font=("Comic Sans MS", 12,"bold"), width=19, background=  "green",fg="white",command= lambda: self.opcion_elegida(7))
        self.boton_enviar.place(x = 625, y = 520)

        boton_err.place(x = 625, y = 5)
        boton_limp_log_err.place(x = 625, y = 85)
        boton_rep_tok.place(x = 625, y = 165)
        boton_limpia_tok.place(x = 625, y = 245)
        boton_usu.place(x = 625, y = 325)
        boton_tec.place(x = 625, y = 405)

        '''boton_salir = tkinter.Button(self.ventana_principal, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white", command=lambda: self.destruir_ventana(self.ventana_principal))
        boton_salir.place(x = 745, y = 0)'''
        
        self.ventana_principal.mainloop()

    def opcion_elegida(self,opcion):
        
        if(opcion == 1):
            #SI SELECCIONAN OTRO ARCHIVO, SE LIMPIAN LOS CAMPOS
            print("REPORTE DE ERRORES SINTACTICOS Y LEXICOS")
            self.ventana_dialog23 = tkinter.Toplevel(self.ventana_principal)
            self.ventana_dialog23.geometry("300x150")
            self.ventana_dialog23.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog23, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto23 = tkinter.Entry(self.ventana_dialog23, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto23.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog23, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep_errores)
            boton1.place(x = 120, y = 80) 
            


        if(opcion == 2):
            print("LIMPIAR LOG DE ERRORES")
            self.general_tokens_err = []
            self.errores_sintac_general = []
            print(len(self.general_tokens_err))
            print(len(self.errores_sintac_general))
            mb.showerror("ERROR", "LOG DE ERRORES LIMPIO ")

        
                                      
        if(opcion == 3):
            print("REPORTE DE TOKENS")
            self.ventana_dialog2 = tkinter.Toplevel(self.ventana_principal)
            self.ventana_dialog2.geometry("300x150")
            self.ventana_dialog2.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog2, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto2 = tkinter.Entry(self.ventana_dialog2, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto2.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog2, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep)
            boton1.place(x = 120, y = 80) 
                   

        if(opcion == 4):
            print("LIMPIAR LOG DE TOKENS")
            self.general_tokens_bien = []
            mb.showerror("ERROR", "LOG DE TOKENS LIMPIO ")
            print(len(self.general_tokens_bien))
            
        
        if(opcion == 5):
            print("MANUAL DE USUARIO")
        
        if(opcion == 6):
            print("MANUAL TECNICO")
        
        if opcion == 7:
            #LOS DATOS DEBEN REESTABLECERSE CADA VEZ QUE SE PRESIONE ENVIAR
            entrada = ''
            
            self.lexico_instruccion.tokens = []
            self.lexico_instruccion.tokens_bien = []
            self.lexico_instruccion.tokens_errorres = []
            entrada = self.caja_texto.get()
            self.caja_texto.delete(0, tkinter.END)
            
            label_usu = ttk.Label(self.frame, text=entrada, background="light green",font=("Comic Sans MS", 15,"bold"))
            label_usu.grid(column=1, row=self.fil, sticky=W, pady=10)
            self.fil += 1

            #QEU SE ANALICE LA INSTRUCCON INTRODUCIDA        
            self.lexico_instruccion.analisis(entrada)
            self.lexico_instruccion.Imprimir()
            #LLENAMOS EL ARREGLO GENERAL
            for token in self.lexico_instruccion.tokens_bien:
                self.general_tokens_bien.append(token)
            for token in self.lexico_instruccion.tokens_errorres:
                self.general_tokens_err.append(token)
            #YA QUE EL PROGRAMA DEBE INTENTAR RECUPERARSE DE LOS ERRORES ENTONCES LOS ERRORES LEXICOS NO IMPORTAN
            print("SINTACTICO")
            sintactico = Sintactico(self.lexico_instruccion.tokens_bien,entrada)
            
            for erro in sintactico.lista_err_S:
                erro.dar_todo()
                print("---------------------------------------------------------------------")
                self.errores_sintac_general.append(erro)
            if sintactico.errorSintactico == True:
                label_res = ttk.Label(self.frame, text="LO SENTIMOS, ERROR SINTACTICO DETECTADO", background="light gray",font=("Comic Sans MS", 15,"bold"))
                label_res.grid(column=1, row=self.fil, sticky=E, pady=10)
                self.fil += 1
            else:#SINO HAY ERRORES SINTACTICOS ENTONCES QE SE EJECUTE LA INSTRUCCION  
                respuesta = self.Ejecutar_instruccion(self.lexico_instruccion.tokens_bien, self.arreglo_elementos)
                print(respuesta)
                label_res = ttk.Label(self.frame, text=respuesta, background="light gray",font=("Comic Sans MS", 15,"bold"))
                label_res.grid(column=1, row=self.fil, sticky=E, pady=10)
                
                self.fil += 1

                if respuesta == 'ADIOS':
                    self.destruir_ventana(self.ventana_principal)

                
            '''print("ARREGLO GENERAL DE TOKENS ")
            for token in self.general_tokens:
                print("LEXEMA: "+token.getLexema()," TIPO: ",token.getTipo(),' LINEA: ',token.getFila(), ', COLUMNA: ',token.getColumna())
                print("---------------------------------------------------------------------")'''
            

    def Ejecutar_instruccion(self, lista, elementos_arr):
        #VALIDAMOS A CASO DEBE IR 
        respuesta = ''
        
        if lista[0].tipo == self.tipos.RESULTADO:
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.RESULTADO:
                    if lista[i+1].tipo == self.tipos.CADENA:
                        if lista[i+2].tipo == self.tipos.VS:
                            if lista[i+3].tipo == self.tipos.CADENA:
                                if lista[i+4].tipo == self.tipos.TEMPORADA:
                                    if lista[i+5].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+6].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+6].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+7].tipo == self.tipos.GUION:
                                                    if lista[i+8].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+8].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+9].tipo == self.tipos.MAYOR_QUE:
                                                                print("llego")#RESULTADO "AD Almería" VS "Español" TEMPORADA <1979 - 1980>
                                                                ini = int(lista[i+6].lexema_valido)
                                                                print(ini)
                                                                
                                                                finn = int(lista[i+8].lexema_valido)
                                                                print(finn)
                                                                equi1 = str(lista[i+1].lexema_valido)
                                                                validar_e = equi1
                                                                equi2 = str(lista[i+3].lexema_valido)
                                                                vaidar_2 = equi2
                                                                si_hay_equipos = False
                                                                si_hay_temp = False
                                                                for elemento in elementos_arr:
                                                                    print(str(elemento.inicio)+"iii")
                                                                    print(str(elemento.fin)+'fin')
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        if validar_e.upper() == elemento.equipo.nombre.upper():
                                                                            if vaidar_2.upper() == elemento.equipo2.nombre.upper():
                                                                                si_hay_equipos = True
                                                                                goles1 = elemento.equipo.goles
                                                                                goles2 = elemento.equipo2.goles
                                                                                respuesta = 'El resultado de este partido fue: '+ str(equi1)+' '+str(goles1)+' - ' + str(equi2)+' '+str(goles2)
                                                                            
                                                                        elif validar_e.upper() == elemento.equipo2.nombre.upper():
                                                                            if vaidar_2.upper() == elemento.equipo.nombre.upper():
                                                                                si_hay_equipos = True
                                                                                goles1 = elemento.equipo.goles
                                                                                goles2 = elemento.equipo2.goles
                                                                                respuesta = 'El resultado de este partido fue: '+ str(equi1)+' '+str(goles2)+' - ' + str(equi2)+' '+str(goles1)
                                                                if si_hay_temp == True:
                                                                    if si_hay_equipos == True:
                                                                        pass
                                                                    else:
                                                                        respuesta = 'ESTOS EQUIPOS NO SE ENFRENTARON EN ESTA TEMPORADA'
                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta
        
        elif lista[0].tipo == self.tipos.JORNADA:
            arreglo_partidos = []
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.JORNADA:
                    if lista[i+1].tipo == self.tipos.NUMERO:
                        digitos = int(lista[i+1].lexema_valido)
                        #SE VALIDA QUE EL NUEMRO TENGA 2 DIGITOS 
                        if digitos > 100: 
                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+'LA JORNADA DEBE TENER 2 DIGITOS MAXIMO'
                        else:
                                if lista[i+2].tipo == self.tipos.TEMPORADA:
                                    if lista[i+3].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+4].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+4].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+5].tipo == self.tipos.GUION:
                                                    if lista[i+6].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+6].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+7].tipo == self.tipos.MAYOR_QUE:
                                                                nombre_archivo = ''
                                                                if lista[i+8].tipo != None:
                                                                    print("si debe haber archivo")
                                                                    if lista[i+8].tipo == self.tipos.GUION:
                                                                        if lista[i+9].tipo == self.tipos.F:
                                                                            if lista[i+10].tipo == self.tipos.LETRAS:
                                                                                nombre_archivo = str(lista[i+10].lexema_valido)
                                                                                
                                                                else:
                                                                    nombre_archivo = 'jornada'
                                                                print("llego")#RESULTADO "AD Almería" VS "Español" TEMPORADA <1979 - 1980>
                                                                jornad = int(lista[i+1].lexema_valido)
                                                                ini = int(lista[i+4].lexema_valido)
                                                                print(ini)
                                                                
                                                                finn = int(lista[i+6].lexema_valido)
                                                                print(finn)
                                                                si_hay_jorn = False
                                                                si_hay_temp = False
                                                                for elemento in elementos_arr:
                                                                    '''print(str(elemento.inicio)+"iii")
                                                                    print(str(elemento.fin)+'fin')'''
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    jor = int(elemento.jornada)

                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        if jornad == jor:
                                                                                si_hay_jorn = True
                                                                                arreglo_partidos.append(elemento)
                                                                respuesta = 'Generando los resultados jornada '+ str(jornad)+' temporada '+str(ini)+' - ' + str(finn)
                                                                            
                                                                        
                                                                if si_hay_temp == True:
                                                                    if si_hay_jorn == True:
                                                                        self.generar_partidos_jor(arreglo_partidos,nombre_archivo,jornad)
                                                                    else:
                                                                        respuesta = 'ESTA JORNADA NO EXISTE EN ESTA TEMPORADA'
                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta
 
        elif lista[0].tipo == self.tipos.GOLES:
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.GOLES:
                    if lista[i+1].tipo == self.tipos.LETRAS:
                        if lista[i+2].tipo == self.tipos.CADENA:
                                if lista[i+3].tipo == self.tipos.TEMPORADA:
                                    if lista[i+4].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+5].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+5].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+6].tipo == self.tipos.GUION:
                                                    if lista[i+7].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+7].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+8].tipo == self.tipos.MAYOR_QUE:
                                                                print("llego")# GOLES TOTAL "Valencia" TEMPORADA <1998-1999>
                                                                ini = int(lista[i+5].lexema_valido)
                                                                print(ini)
                                                                
                                                                finn = int(lista[i+7].lexema_valido)
                                                                print(finn)
                                                                equipo_ = str(lista[i+2].lexema_valido)
                                                                validar_e = equipo_
                                                                si_hay_equipo = False
                                                                goles_eq = 0
                                                                condicion = str(lista[i+1].lexema_valido)
                                                                si_hay_temp = False
                                                                for elemento in elementos_arr:
                                                                    print(str(elemento.inicio)+"iii")
                                                                    print(str(elemento.fin)+'fin')
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        if condicion.upper() == 'VISITANTE':# GOLES VISITANTE "Barcelona" TEMPORADA <1979-1980>
                                                                            if validar_e.upper() == elemento.equipo2.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                goles_eq += elemento.equipo2.goles
                                                                
                                                                        elif condicion.upper() == 'LOCAL':
                                                                            if validar_e.upper() == elemento.equipo.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                goles_eq += elemento.equipo.goles

                                                                        elif condicion.upper() == 'TOTAL':
                                                                            if validar_e.upper() == elemento.equipo.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                goles_eq += elemento.equipo.goles
                                                                                
                                                                            elif validar_e.upper() == elemento.equipo2.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                goles_eq += elemento.equipo2.goles
                                                                        
                                                                if si_hay_temp == True:
                                                                    if si_hay_equipo == True:
                                                                       respuesta = 'Los goles anotados por '+str(equipo_)+' en condición '+str(condicion)+' en la temporada '+str(ini)+'-'+str(finn)+' fueron '+str(goles_eq)
                                                                    else:
                                                                        respuesta = 'EQUIPO NO ENCONTRADO'
                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta
         
        elif lista[0].tipo == self.tipos.TABLA:
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.TABLA:
                                if lista[i+1].tipo == self.tipos.TEMPORADA:
                                    if lista[i+2].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+3].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+3].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+4].tipo == self.tipos.GUION:
                                                    if lista[i+5].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+5].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+6].tipo == self.tipos.MAYOR_QUE:
                                                                nombre_archivo = ''
                                                                if lista[i+7].tipo != None:
                                                                    print("si debe haber archivo")
                                                                    if lista[i+7].tipo == self.tipos.GUION:
                                                                        if lista[i+8].tipo == self.tipos.F:
                                                                            if lista[i+9].tipo == self.tipos.LETRAS:
                                                                                nombre_archivo = str(lista[i+9].lexema_valido)
                                                                                
                                                                else:
                                                                    nombre_archivo = 'temporada'

                                                                print("llego")#RESULTADO "AD Almería" VS "Español" TEMPORADA <1979 - 1980>
                                                                ini = int(lista[i+3].lexema_valido)
                                                                print(ini)
                                                                
                                                                finn = int(lista[i+5].lexema_valido)
                                                                print(finn)
                                                                
                                                                si_hay_temp = False
                                                                arreglo_equipos_temp = []
                                                                arreglo_equipos = []
                                                                print("long arreglo equipos temp "+str(len(arreglo_equipos_temp)))
                                                                print("long arreglo equipos "+str(len(arreglo_equipos)))
                                                                for elemento in elementos_arr:
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        arreglo_equipos.append(elemento)
                                                                if si_hay_temp == True:
                                                                    print("ENTRO AL IF ")
                                                                    arreglo_equipos_temp.append(arreglo_equipos[0].equipo)
                                                                    arreglo_equipos_temp.append(arreglo_equipos[0].equipo2)

                                                                    for e in range(1, len(arreglo_equipos)):
                                                                                
                                                                                equipo1_t = arreglo_equipos[e].equipo.nombre.upper()
                                                                                equipo2_t = arreglo_equipos[e].equipo2.nombre.upper()
                                                                                print(equipo1_t)
                                                                                print(equipo2_t)
                                                                                bandera_encontre = False
                                                                                bandera_encontre_2 = False
                                                                            
                                                                                for k in range(len(arreglo_equipos_temp)):
                                                                                    if arreglo_equipos_temp[k].nombre.upper() == equipo1_t:
                                                                                        agreg = int(arreglo_equipos[e].equipo.puntos)
                                                                                        bandera_encontre = True
                                                                                        print(agreg)
                                                                                        arreglo_equipos_temp[k].puntos += agreg
                                                                                
                                                                                    if arreglo_equipos_temp[k].nombre.upper() == equipo2_t:
                                                                                        bandera_encontre_2 = True
                                                                                        agreg2 = int(arreglo_equipos[e].equipo2.puntos)
                                                                                        print(agreg2)
                                                                                        arreglo_equipos_temp[k].puntos += agreg2

                                                                                if bandera_encontre == False:
                                                                                    print("agregoss")
                                                                                    arreglo_equipos_temp.append(arreglo_equipos[e].equipo)
                                                                                if bandera_encontre_2 == False:
                                                                                    print("agregoss2")
                                                                                    arreglo_equipos_temp.append(arreglo_equipos[e].equipo2)


                                                                            
                                                                    print("SALIO DEL FOR")
                                                                    print(len(arreglo_equipos_temp))  
                                                                    for m in arreglo_equipos_temp:
                                                                        print(m.nombre)
                                                                        print(m.puntos)  
                                                                            
                                                                        
                                                                

                                                                        
                                                                if si_hay_temp == True:
                                                                    respuesta = 'Generando archivo de clasificación de temporada '+str(ini)+'-'+str(finn)
                                                                    ordenado = self.ordenar_puntos(arreglo_equipos_temp)
                                                                    for inff in ordenado:
                                                                        print(inff.nombre+"*"+str(inff.puntos))
                                                                    self.generar_Puntos_temp(ordenado, nombre_archivo, ini, finn)

                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta
        
        elif lista[0].tipo == self.tipos.PARTIDOS:
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.PARTIDOS:
                    if lista[i+1].tipo == self.tipos.CADENA:
                                if lista[i+2].tipo == self.tipos.TEMPORADA:
                                    if lista[i+3].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+4].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+4].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+5].tipo == self.tipos.GUION:
                                                    if lista[i+6].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+6].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+7].tipo == self.tipos.MAYOR_QUE:
                                                                nombre_ar = 'partidos'
                                                                b_desde = False
                                                                b_hasta = False
                                                                jornada_desde = 0
                                                                jornada_hasta = 0


                                                                if lista[i+8].tipo != None:
                                                                    print("si debe haber archivo")
                                                                    for f in range(len(lista)):
                                                                        if lista[f].tipo == self.tipos.F:
                                                                            if lista[f+1].tipo == self.tipos.LETRAS:
                                                                                nombre_ar = str(lista[f+1].lexema_valido)
                                                                        if lista[f].tipo == self.tipos.JI:
                                                                            if lista[f+1].tipo == self.tipos.NUMERO:
                                                                                jornada_desde = int(lista[f+1].lexema_valido)
                                                                                b_desde = True
                                                                        if lista[f].tipo == self.tipos.JF:
                                                                            if lista[f+1].tipo == self.tipos.NUMERO:
                                                                                b_hasta = True
                                                                                jornada_hasta = int(lista[f+1].lexema_valido)

                                                                print("llego")#RESULTADO "AD Almería" VS "Español" TEMPORADA <1979 - 1980>
                                                                ini = int(lista[i+4].lexema_valido)
                                                                print(ini)
                                                                
                                                                finn = int(lista[i+6].lexema_valido)
                                                                print(finn)
                                                                equi1 = str(lista[i+1].lexema_valido)
                                                                validar_e = equi1
                                                                si_hay_equipo = False
                                                                si_hay_temp = False
                                                                arreglo_temp_jor = []
                                                                arreglo_partidos_equipo = []
                                                                for elemento in elementos_arr:
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        jornada = int(elemento.jornada)
                                                                        if b_desde == False and b_hasta == False:
                                                                            #QUE LOS AGREGUE TODOSS
                                                                            arreglo_temp_jor.append(elemento)
                                                                        elif b_desde == True and b_hasta == True:
                                                                            if jornada >= jornada_desde and jornada <= jornada_hasta:
                                                                                arreglo_temp_jor.append(elemento)
                                                                            #entre
                                                                        elif b_desde == True and b_hasta == False:
                                                                            if jornada >= jornada_desde:
                                                                                arreglo_temp_jor.append(elemento)
                                                                            #SOLO LOS DE PRINCIPIO
                                                                        elif b_desde == False and b_hasta == True:
                                                                            if jornada <= jornada_hasta:
                                                                                arreglo_temp_jor.append(elemento)
                                                                                 #LOS ULTIMOS 
                                                                                 # PARTIDOS "Español" TEMPORADA <1979-1980> -f reporteEspanol -ji 2 -jf 3

                                                                print("SALIO FOR ELEMENTOS")
                                                                for elem in arreglo_temp_jor:
                                                                        if validar_e.upper() == elem.equipo.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                arreglo_partidos_equipo.append(elem)
                                                                        elif validar_e.upper() == elem.equipo2.nombre.upper():
                                                                                si_hay_equipo = True
                                                                                arreglo_partidos_equipo.append(elem)
                                                                if si_hay_temp == True:
                                                                    if si_hay_equipo == True:
                                                                        self.generar_partidos_equipo(arreglo_partidos_equipo, nombre_ar, equi1)
                                                                        respuesta = 'Generando archivo de resultados de temporada'+str(ini)+'-'+str(finn)+' del equipo '+equi1
                                                                    else:
                                                                        respuesta = 'ESTE EQUIPO NO ESTA EN ESTA TEMPORADA'
                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta  
        
        elif lista[0].tipo == self.tipos.TOP:
            for i in range(len(lista)):
                if lista[i].tipo == self.tipos.TOP:
                    if lista[i+1].tipo == self.tipos.LETRAS:
                                if lista[i+2].tipo == self.tipos.TEMPORADA:
                                    if lista[i+3].tipo == self.tipos.MENOR_QUE:
                                        if lista[i+4].tipo == self.tipos.NUMERO:
                                            digitos = int(lista[i+4].lexema_valido)
                                            #SE VALIDA QUE EL NUEMRO TENGA 4 DIGITOS 
                                            if digitos < 1000: 
                                                respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                            else:
                                                if lista[i+5].tipo == self.tipos.GUION:
                                                    if lista[i+6].tipo == self.tipos.NUMERO:
                                                        digitos = int(lista[i+6].lexema_valido)
                                                        if digitos < 1000: 
                                                            respuesta = 'HA OCURRIDO UN ERROR ->>'+ str(digitos)+' EL AÑO NO PUEDE TENER MENOS DE 4 DIGITOS'
                                                        else:
                                                            if lista[i+7].tipo == self.tipos.MAYOR_QUE:
                                                                cuantos = 5

                                                                if lista[i+8].tipo != None:
                                                                    print("si debe haber archivo")
                                                                    if lista[i+8].tipo == self.tipos.GUION:
                                                                        if lista[i+9].tipo == self.tipos.N:
                                                                            if lista[i+10].tipo == self.tipos.NUMERO:
                                                                                cuantos = int(lista[i+10].lexema_valido)
                                                                
                                                                print("llego")#RESULTADO "AD Almería" VS "Español" TEMPORADA <1979 - 1980>
                                                                ini = int(lista[i+4].lexema_valido)
                                                                finn = int(lista[i+6].lexema_valido)
                                                                
                                                                
                                                                si_hay_temp = False
                                                                arreglo_top_temp = []
                                                                arreglo_top = []
                                                                print("long arreglo equipos temp top "+str(len(arreglo_top_temp)))
                                                                print("long arreglo equipos top"+str(len(arreglo_top)))
                                                                for elemento in elementos_arr:
                                                                    inicio_t = int(elemento.inicio)
                                                                    final_t = int(elemento.fin)
                                                                    if ini == inicio_t and finn == final_t:
                                                                        print("ENCONTRO TEMP")
                                                                        si_hay_temp = True
                                                                        arreglo_top_temp.append(elemento)
                                                                
                                                                if si_hay_temp == True:
                                                                    print("ENTRO AL IF ")
                                                                    arreglo_top.append(arreglo_top_temp[0].equipo)
                                                                    arreglo_top.append(arreglo_top_temp[0].equipo2)

                                                                    for e in range(1, len(arreglo_top_temp)):
                                                                                
                                                                                equipo1_t = arreglo_top_temp[e].equipo.nombre.upper()
                                                                                equipo2_t = arreglo_top_temp[e].equipo2.nombre.upper()
                                                            
                                                                                bandera_encontre = False
                                                                                bandera_encontre_2 = False
                                                                            
                                                                                for k in range(len(arreglo_top)):
                                                                                    if arreglo_top[k].nombre.upper() == equipo1_t:
                                                                                        agreg = int(arreglo_top_temp[e].equipo.puntos)
                                                                                        bandera_encontre = True
                                                                    
                                                                                        arreglo_top[k].puntos += agreg
                                                                                
                                                                                    if arreglo_top[k].nombre.upper() == equipo2_t:
                                                                                        bandera_encontre_2 = True
                                                                                        agreg2 = int(arreglo_top_temp[e].equipo2.puntos)
                                                                                        arreglo_top[k].puntos += agreg2

                                                                                if bandera_encontre == False:
                                                                                    print("agregoss")
                                                                                    arreglo_top.append(arreglo_top_temp[e].equipo)
                                                                                if bandera_encontre_2 == False:
                                                                                    print("agregoss2")
                                                                                    arreglo_top.append(arreglo_top_temp[e].equipo2)


                                                                
                                                                if si_hay_temp == True:
                                                                    
                                                                    ent = str(lista[i+1].lexema_valido)
                                                                    if ent == 'SUPERIOR':
                                                                        ordenado = self.ordenar_puntos(arreglo_top)
                                                                        respuesta = 'El top superior de la temporada'+str(ini)+'-'+str(finn)+' fue:\n'
                                                                        for cu in range(cuantos):
                                                                            
                                                                            respuesta += '\t'+str(cu)+'.'+str(ordenado[cu].nombre)+'\n'
                                                                            
                                                                        
                                                                    else:
                                                                        ordenado = self.ordenar_puntos_inf(arreglo_top)
                                                                        respuesta = 'El top inferior de la temporada'+str(ini)+'-'+str(finn)+' fue:\n'
                                                                        for inf in ordenado:
                                                                            print(inf.nombre+str(inf.puntos))
                                                                        for cu in range(cuantos):
                                                                            
                                                                            respuesta += '\t'+str(cu)+'.'+str(ordenado[cu].nombre)+'\n'
                                                                        
                                                                    
                                                                else: 
                                                                    respuesta = 'ESTA TEMPORADA NO EXISTE'                
            return respuesta
        
        elif lista[0].tipo == self.tipos.ADIOS:
            self.caja_texto.configure(state='disabled')
            return 'ADIOS'

        else: 
            return 'INSTRUCCION NO VALIDA' 
        
    def destruir_ventana(self, ventana):
        ventana.destroy()

    def ordenar_puntos(self, lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].puntos > lista[j].puntos):
                    aux=lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
        return lista
    
    def ordenar_puntos_inf(self, lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].puntos < lista[j].puntos):
                    aux=lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
        return lista
    
    def generar_partidos_jor(self, elementos, nombre, jornada):
        nombre = nombre + ".html"
        file = open(nombre, "w")
        file.write("<HTML>")
        file.write("<HEAD><TITLE>PARTIDOS DE LA JORNADA "+str(jornada)+"</TITLE>")
        file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
        file.write("</head>")
        file.write("<body>")
        file.write("<CENTER><H1><b>----------------------- PARTIDOS DE LA JORNADA &nbsp &nbsp"+str(jornada)+" -----------------------</b></H1>")
        file.write("</CENTER>")
        file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
        file.write("<form action=\"\"> ")
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
        file.write("<br>")
        file.write("<div  id = \"main-container\" >")
        file.write("<b>")
        file.write("<table>")
        file.write("<thead>")
        file.write("<tr>")
        file.write("<th> FECHA   </th><th>EQUIPO 1</th><th>GOLES</th><th>EQUIPO 2</th><th>GOLES</th>")
        file.write("</tr>")
        file.write("</thead>")#JORNADA 1 TEMPORADA <1979-1980>
                
        for elemento in elementos:
                    file.write("<tr><font size = 12 color = \"white\" >")
                    file.write("<td> "+str(elemento.fecha.dar_todo())+"</td><td>"+str(elemento.equipo.nombre)+"</td><td>"+str(elemento.equipo.goles)+"</td><td>"+str(elemento.equipo2.nombre)+"</td><td>"+str(elemento.equipo2.goles)+"</td>")
                    file.write("<font size = 12></tr>")
                
        file.write("</b>")
        file.write("</table>")
        file.write("</div>")
        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL REPORTE CON EXITO")
        print("")   

    def generar_Puntos_temp(self, elementos, nombre, inicio, finall):
        nombre = nombre + ".html"
        file = open(nombre, "w")
        file.write("<HTML>")
        file.write("<HEAD><TITLE>TEMPORADA "+str(inicio)+"-"+str(finall)+"</TITLE>")
        file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
        file.write("</head>")
        file.write("<body>")
        file.write("<CENTER><H1><b>------------------- PARTIDOS DE LA TEMPORADA &nbsp"+str(inicio)+"-"+str(finall)+" ------------------</b></H1>")
        file.write("</CENTER>")
        file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
        file.write("<form action=\"\"> ")
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
        file.write("<br>")
        file.write("<div  id = \"main-container\" >")
        file.write("<b>")
        file.write("<table>")
        file.write("<thead>")
        file.write("<tr>")
        file.write("<th> EQUIPO   </th><th>PUNTOS OBTENIDOS</th>")
        file.write("</tr>")
        file.write("</thead>")#JORNADA 1 TEMPORADA <1979-1980>
                
        for elemento in elementos:
                    file.write("<tr><font size = 12 color = \"white\" >")
                    file.write("<td>"+str(elemento.nombre)+"</td><td>"+"&nbsp &nbsp &nbsp"+str(elemento.puntos)+"</td>")
                    file.write("<font size = 12></tr>")
                
        file.write("</b>")
        file.write("</table>")
        file.write("</div>")
        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL ARCHIVO CON EXITO")
        print("")   

    def generar_partidos_equipo(self, elementos, nombre, nom_e):
        nombre = nombre + ".html"
        file = open(nombre, "w")
        file.write("<HTML>")
        file.write("<HEAD><TITLE>PARTIDOS "+str(nom_e)+"</TITLE>")
        file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
        file.write("</head>")
        file.write("<body>")
        file.write("<CENTER><H1><b>----------------------- PARTIDOS DEL EQUIPO &nbsp &nbsp"+str(nom_e)+" -----------------------</b></H1>")
        file.write("</CENTER>")
        file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
        file.write("<form action=\"\"> ")
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
        file.write("<br>")
        file.write("<div  id = \"main-container\" >")
        file.write("<b>")
        file.write("<table>")
        file.write("<thead>")
        file.write("<tr>")
        file.write("<th> FECHA   </th><th>JORNADA</th><th>EQUIPO 1</th><th>GOLES</th><th>EQUIPO 2</th><th>GOLES</th>")
        file.write("</tr>")
        file.write("</thead>")#JORNADA 1 TEMPORADA <1979-1980>
                
        for elemento in elementos:
                    file.write("<tr><font size = 12 color = \"white\" >")
                    file.write("<td> "+str(elemento.fecha.dar_todo())+"</td><td>"+str(elemento.jornada)+"</td><td>"+str(elemento.equipo.nombre)+"</td><td>"+str(elemento.equipo.goles)+"</td><td>"+str(elemento.equipo2.nombre)+"</td><td>"+str(elemento.equipo2.goles)+"</td>")
                    file.write("<font size = 12></tr>")
                
        file.write("</b>")
        file.write("</table>")
        file.write("</div>")
        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL REPORTE CON EXITO")
        print("")   

    def extraer_nom_rep (self):
        nombre_rep = self.caja_texto2.get()
        self.caja_texto2.delete(0, tkinter.END)
        self.ventana_dialog2.destroy()
        tokens_rep = self.general_tokens_bien
        sintac = []
        self.reporte_tokens(nombre_rep, tokens_rep, "TOKENS", sintac)
    
    def extraer_nom_rep_errores (self):
        nombre_rep_e = self.caja_texto23.get()
        self.caja_texto23.delete(0, tkinter.END)
        self.ventana_dialog23.destroy()
        tokens_rep_e = self.general_tokens_err
        sint = self.errores_sintac_general
        self.reporte_tokens(nombre_rep_e, tokens_rep_e, "ERRORES",sint)
    
    def reporte_tokens(self, nombre, tokens, titulo, sintacticos):
        nombre = nombre + ".html"
        file = open(nombre, "w")
        file.write("<HTML>")
        file.write("<HEAD><TITLE>REPORTE TOKENS</TITLE>")
        file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
        file.write("</head>")
        file.write("<body>")
        file.write("<CENTER><H1><b>------------------------------- REPORTE DE &nbsp &nbsp"+titulo+" -------------------------------</b></H1>")
        file.write("</CENTER>")
        file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
        file.write("<form action=\"\"> ")
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
        file.write("<br>")
        file.write("<div  id = \"main-container\" >")
        file.write("<b>")
        file.write("<table>")
        file.write("<thead>")
        file.write("<tr>")
        file.write("<th> TOKEN   </th><th>LEXEMA</th><th>FILA</th><th>COLUMNA</th>")
        file.write("</tr>")
        file.write("</thead>")
                
        for token in tokens:
                    file.write("<tr><font size = 12 color = \"white\" >")
                    file.write("<td> "+str(token.getTipo())+"</td><td>"+str(token.lexema_valido)+"</td><td>"+str(token.fila)+"</td><td>"+str(token.columna)+"</td>")
                    file.write("<font size = 12></tr>")
                
        file.write("</b>")
        file.write("</table>")
        file.write("</div>")
        if len(sintacticos) == 0:
            pass
        else:
            file.write("<br>")
            file.write("<div  id = \"main-container\" >")
            file.write("<b>")
            file.write("<table>")
            file.write("<thead>")
            file.write("<tr>")
            file.write("<th> CADENA INTRODUCIDA </th><th>TOKEN ENCONTRADO</th><th>TOKEN ESPERADO</th>")
            file.write("</tr>")
            file.write("</thead>")
                    
            for sintactico in sintacticos:
                        file.write("<tr><font size = 12 color = \"white\" >")
                        file.write("<td> "+str(sintactico.cadena)+"</td><td>"+str(sintactico.hay)+"</td><td>"+str(sintactico.habia)+"</td>")
                        file.write("<font size = 12></tr>")
                    
            file.write("</b>")
            file.write("</table>")
            file.write("</div>")
        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL REPORTE CON EXITO")
        print("")   
  
    
        

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3

   app = Todo()

if __name__ == "__main__":
    main()

