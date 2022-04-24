class Error_Sintactico():
    def __init__(self,hay, habia, cadena):
        self.hay = hay
        self.cadena = cadena
        self.habia = habia 

    def dar_todo(self):
        print("EN LA ENTRADA: "+str(self.cadena)+str(self.hay), "-- Sintactico", " -- Se esperaba "+str(self.habia))