class Fecha():
    def __init__(self,dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def dar_todo(self):
        print(str(self.dia)+" / "+str(self.mes)+" / "+str(self.año))
        