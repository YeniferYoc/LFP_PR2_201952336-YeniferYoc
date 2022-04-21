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
        self.contenido = ""
        self.lexico_conte = Analizador_Lexico()
        self.general_tokens = []
        self.errores_sintac_general = []
        self.fil = 0

        archi1=open('LaLigaBot-LFP.csv', "r", encoding="utf-8")
        self.contenido=archi1.read()
        archi1.close()
        self.contenido = self.contenido.replace(" ","")
        print(self.contenido)
        self.lexico_conte.analisis(self.contenido)
        self.lexico_conte.Imprimir()

        long_arr = len(self.lexico_conte.tokens_bien)
        print(long_arr)
        self.tipos = Token("lexema", -1, -1, -1)
        self.arreglo_elementos = []
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
                                                                equipo_nuevo = Equipo(nombre1, goles1, False)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, False)
                                                            elif goles1 < goles2:
                                                                equipo_nuevo = Equipo(nombre1, goles1, False)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, True)
                                                            else:
                                                                equipo_nuevo = Equipo(nombre1, goles1, True)
                                                                equipo_nuevo2 = Equipo(nombre2, goles2, False)
                                                            nombre1 =''
                                                            nombre2 = ''
                                                            elemento_nuevo = Elemento(fecha_nueva, inicio, fin,jornada, equipo_nuevo, equipo_nuevo2)
                                                            self.arreglo_elementos.append(elemento_nuevo)
                                                            incrementa = i+12+contador+1+contador2+3
                                                            print(incrementa)
        cont = 0
        for elemento in self.arreglo_elementos:
            elemento.dar_todo()
            cont +=1
        print("")
        print(cont)
                                                            


                                            


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

        canvas = Canvas(self.frame, bd=0, yscrollcommand=yscrollbar.set,width=585, height=500)
        canvas.grid(column=0, row=0, sticky=N+S+E+W)

        yscrollbar.config(command=canvas.yview)


        

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
        
        self.caja_texto = tkinter.Entry(self.ventana_principal, font=("Comic Sans MS", 15,"bold"), width=50)
        self.caja_texto.insert(0, "Hola mundo!")
        self.caja_texto.place(x = 6, y = 525)

        self.boton_enviar = tkinter.Button(self.ventana_principal, text = "ENVIAR", font=("Comic Sans MS", 12,"bold"), width=19, background=  "green",fg="white",command= lambda: self.opcion_elegida(7))
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
            archi1=open('LaLigaBot-LFP.csv', "r", encoding="utf-8")
            self.contenido=archi1.read()
            archi1.close()
            
            print(self.contenido)
            self.lexico_conte.analisis(self.contenido)
            self.lexico_conte.Imprimir()


        if(opcion == 2):
            print("AQUI SE GENERA EL FORMULARIO ")
        
                                      
        if(opcion == 3):
            print("AQUI SE ANALIZA")
                   

        if(opcion == 4):
            print("AQUI REPORTES")
            self.ventana_reportes = tkinter.Toplevel(self.ventana_principal)
            self.ventana_reportes.geometry("500x400")
            self.ventana_reportes.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_reportes, text = "REPORTES", background="light blue",font=("Comic Sans MS", 20,"bold"))
            etiqueta.place(x = 175, y = 5)


            boton_tokens = tkinter.Button(self.ventana_reportes, text = "Reporte de Tokens", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(1))
            boton_errores = tkinter.Button(self.ventana_reportes, text = "Reporte Errores", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(2))
            boton_usuario = tkinter.Button(self.ventana_reportes, text = "Manual de Usuario", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(3))
            boton_tecnico = tkinter.Button(self.ventana_reportes, text = "Manual Tecnico", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(4))
            boton_tokens.place(x = 30, y = 60)
            boton_errores.place(x = 275, y = 60)
            boton_usuario.place(x = 30, y = 250)
            boton_tecnico.place(x = 275, y = 250)

            boton_salir = tkinter.Button(self.ventana_reportes, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white", command=lambda: self.destruir_ventana(self.ventana_reportes))
            boton_salir.place(x = 435, y = 0)
            self.ventana_reportes.mainloop()
        
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
            for token in self.lexico_instruccion.tokens:
                self.general_tokens.append(token)
            #YA QUE EL PROGRAMA DEBE INTENTAR RECUPERARSE DE LOS ERRORES ENTONCES LOS ERRORES LEXICOS NO IMPORTAN
            print("SINTACTICO")
            sintactico = Sintactico(self.lexico_instruccion.tokens_bien)
            
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
            print("ARREGLO GENERAL DE TOKENS ")
            for token in self.general_tokens:
                print("LEXEMA: "+token.getLexema()," TIPO: ",token.getTipo(),' LINEA: ',token.getFila(), ', COLUMNA: ',token.getColumna())
                print("---------------------------------------------------------------------")
            
            


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
                                                                validar_e = equi1.replace(" ","")
                                                                equi2 = str(lista[i+3].lexema_valido)
                                                                vaidar_2 = equi2.replace(" ","")
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
            return 'GOLES'  
        elif lista[0].tipo == self.tipos.TABLA:
            return 'TABLA'
        elif lista[0].tipo == self.tipos.PARTIDOS:
            return 'PARTIDOS'  
        elif lista[0].tipo == self.tipos.TOP:
            return 'TOP'
        elif lista[0].tipo == self.tipos.ADIOS:
            self.caja_texto.configure(state='disabled')
            return 'ADIOS' 
        '''for i in range(len(lista)):
            if self.lexico_conte.tokens_bien[i].tipo == self.tipos.NUMERO:
                pass'''
    def destruir_ventana(self, ventana):
        ventana.destroy()
    
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
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
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


    def opciones_reporte(self, opcion):
        if(opcion == 1):
            print("REPORTE DE TOKENS")
            self.ventana_dialog2 = tkinter.Toplevel(self.ventana_reportes)
            self.ventana_dialog2.geometry("300x150")
            self.ventana_dialog2.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog2, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto2 = tkinter.Entry(self.ventana_dialog2, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto2.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog2, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep)
            boton1.place(x = 120, y = 80) 
            
            
        if(opcion == 2):
            print("REPORTE DE ERRORES")
            self.ventana_dialog23 = tkinter.Toplevel(self.ventana_reportes)
            self.ventana_dialog23.geometry("300x150")
            self.ventana_dialog23.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog23, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto23 = tkinter.Entry(self.ventana_dialog23, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto23.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog23, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep_errores)
            boton1.place(x = 120, y = 80) 
            
        if(opcion == 3):
            print("MANUAL DE USUARIO")
            startfile("[LFPA]_MANUAL_USUARIO_201952336.pdf")

        if(opcion == 4):
            print("MANUAL TECNICO")
            startfile("[LFPA]_MANUAL_TECNICO_201952336.pdf")

    
        

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2  TOP INFERIOR TEMPORADA <1999-2000> -n 3

   app = Todo()

if __name__ == "__main__":
    main()

'''
caja_texto = tkinter.Entry(ventana_nueva, font = "Helvetica 30")
caja_texto.pack()

def saludo (nombre):
    print("holaa"+nombre)

def extraer_texto():
    entrada = caja_texto.get()
    print(entrada)

def extraer_texto_etiqueta():
    entrada = caja_texto.get()
    etiqueta["text"] = entrada 

boton1 = tkinter.Button(ventana_nueva, text= "presiona",width=10, height=5, command = extraer_texto_etiqueta)
boton1.pack()
#boton1 = tkinter.Button(ventana_nueva, text= "presiona", command = lambda:  saludo(" yenifer"))
#boton1.pack()
'''
#ultimo