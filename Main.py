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
#import ventana_analizar
#from  ventana_reportes import *
class Todo():
    
    def __init__(self):
        self.contenido = ""
        self.lexico_conte = Analizador_Lexico()
        self.general_tokens = []

        '''archi1=open('LaLigaBot-LFP.csv', "r", encoding="utf-8")
        self.contenido=archi1.read()
        archi1.close()
        self.contenido = self.contenido.replace(" ","")
        print(self.contenido)
        self.lexico_conte.analisis(self.contenido)
        self.lexico_conte.Imprimir()

        long_arr = len(self.lexico_conte.tokens_bien)
        print(long_arr)
        self.tipos = Token("lexema", -1, -1, -1)
        arreglo_elementos = []
        contador = 0
        contador2 = 0
        incrementa = 19

        #ANALIZAR INSTRUCCIONES 
        self.lexico_instruccion = Analizador_Lexico()

        for i in range(0,long_arr,incrementa+contador+contador2):
            print("entro al for")
            print(i)
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
                                                            arreglo_elementos.append(elemento_nuevo)
                                                            incrementa = i+12+contador+1+contador2+3
                                                            print(incrementa)
        cont = 0
        for elemento in arreglo_elementos:
            elemento.dar_todo()
            cont +=1
        print("")
        print(cont)'''
                                                            


                                            


        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("La Liga Bot")
        self.ventana_principal.geometry("850x575")
        self.ventana_principal.configure(bg="cyan")

       

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
        self.frame = Frame(self.ventana_principal, borderwidth=2, relief=SUNKEN, background="light gray")
        self.frame.grid(column=0, row=0, sticky=N+S+E+W)


        yscrollbar = Scrollbar(self.frame)
        yscrollbar.grid(column=1, row=0, sticky=N+S)

        canvas = Canvas(self.frame, bd=0, yscrollcommand=yscrollbar.set)
        canvas.grid(column=0, row=0, sticky=N+S+E+W)

        yscrollbar.config(command=canvas.yview)

        self.frame = Frame(canvas, borderwidth=2, relief=SUNKEN, background="light gray")
        canvas.create_window(4, 4, window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", _on_frame_configure)

        
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
            '''entrada = ''
            
            self.lexico_instruccion.tokens = []
            self.lexico_instruccion.tokens_bien = []
            self.lexico_instruccion.tokens_errorres = []
            entrada = self.caja_texto.get()
            self.caja_texto.delete(0, tkinter.END)'''
            

            for i in range(30):
                label = ttk.Label(self.frame, text="This is a label "+str(i))
                label.grid(column=1, row=i, sticky=W)

                text = ttk.Entry(self.frame, textvariable="text")
                text.grid(column=2, row=i, sticky=W)

            '''etiqueta = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta.place(x=400, y =10)
            etiqueta2 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta2.place(x=400, y =60)
            etiqueta3 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta3.place(x=400, y =110)
            etiqueta4 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta4.place(x=400, y =160)
            etiqueta5 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta5.place(x=400, y =210)
            etiqueta26 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta26.place(x=400, y =260)
            etiqueta37 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta37.place(x=400, y =310)
            etiqueta48 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta48.place(x=400, y =360)
            etiqueta59 = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            etiqueta59.place(x=400, y =410)
            nombre = tkinter.Label(self.mycanvas, text = "hla", background="gray",font=("Comic Sans MS", 15,"bold"))
            nombre.place(x=400, y =460)'''
            '''self.mycanvas.create_rectangle(175,10, 500,65, outline="black", fill = "green")
            self.mycanvas.create_text(160,10,text = "hola", fill = "white",font=("Comic Sans MS", 15,"bold"))

            self.mycanvas.create_rectangle(175,10, 500,65, outline="black", fill = "green")
            self.mycanvas.create_text(160,10,text = "hola", fill = "white",font=("Comic Sans MS", 15,"bold"))'''


            
            '''self.lexico_instruccion.analisis(entrada)
            self.lexico_instruccion.Imprimir()
            #LLENAMOS EL ARREGLO GENERAL 
            self.general_tokens = self.lexico_instruccion.tokens
            for token in self.general_tokens:
                tipos = Token("lexema", -1, -1, -1)
                print("LEXEMA: "+token.getLexema()," TIPO: ",token.getTipo(),' LINEA: ',token.getFila(), ', COLUMNA: ',token.getColumna())
                print("---------------------------------------------------------------------")
    '''






            
  
    
    
    def destruir_ventana(self, ventana):
        ventana.destroy()

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

    
        

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
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