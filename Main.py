import tkinter
from tkinter import *
from tkinter.ttk import LabelFrame
from turtle import bgcolor
from Cargar_arch import cargar
from tkinter import Tk, messagebox as mb
from tkinter.simpledialog import *
from os import startfile
#import ventana_analizar
#from  ventana_reportes import *
class Todo():
    
    def __init__(self):

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
        
       
        
        etiqueta = tkinter.Label(self.ventana_principal, width=85, height=33, background="white")
        etiqueta.place(x = 6, y = 5)
        
        boton_limp_en = tkinter.Button(self.ventana_principal, text = "Limpiar Log de entrada", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white" , command= lambda: self.opcion_elegida(1) )
        boton_rep_tok = tkinter.Button(self.ventana_principal, text = "Reporte de tokens", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(2))
        boton_limpia_tok = tkinter.Button(self.ventana_principal, text = "Limpiar log de tokens", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(3))
        boton_usu = tkinter.Button(self.ventana_principal, text = "Manual de usuario", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(4))
        boton_tec = tkinter.Button(self.ventana_principal, text = "Manual Tecnico", font=("Comic Sans MS", 12,"bold"), width=19, height=2, background=  "gray",fg="white",command= lambda: self.opcion_elegida(4))
        
        self.caja_texto = tkinter.Entry(self.ventana_principal, font=("Comic Sans MS", 15,"bold"), width=50)
        self.caja_texto.insert(0, "Hola mundo!")
        self.caja_texto.place(x = 6, y = 525)

        boton_enviar = tkinter.Button(self.ventana_principal, text = "ENVIAR", font=("Comic Sans MS", 12,"bold"), width=19, background=  "green",fg="white",command= lambda: self.opcion_elegida(4))
        boton_enviar.place(x = 625, y = 520)

        boton_limp_en.place(x = 625, y = 20)
        boton_rep_tok.place(x = 625, y = 110)
        boton_limpia_tok.place(x = 625, y = 200)
        boton_usu.place(x = 625, y = 290)
        boton_tec.place(x = 625, y = 380)

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