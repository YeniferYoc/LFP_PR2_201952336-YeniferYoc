class Error_Sintactico():
    def __init__(self,hay, habia):
        self.hay = hay
        self.habia = habia 

    def dar_todo(self):
        print(str(self.hay), "-- Sintactico", " -- Se esperaba "+str(self.habia))