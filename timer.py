class Timer:
    def __init__(self,horas=0,minutos=0,segundos=0):
        if(horas<10):
            self.horas = "0"+str(horas)
        else:
            self.horas = str(horas)
        if(minutos<10):
            self.minutos = "0"+str(minutos)
        else:
            self.minutos = str(minutos)
        if(segundos<10):
            self.segundos = "0"+str(segundos)
        else:
            self.segundos = str(segundos)
        
    def __str__(self):
        return str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos)

    def next_second(self):
        self.segundos = int(self.segundos) +1
        if(self.segundos == 60):
            self.minutos = int(self.minutos) + 1
            if(self.minutos == 60):
                self.horas = int(self.horas) +1
                self.minutos = 0
            if(self.minutos<10):
                self.minutos = "0"+str(self.minutos)
            self.segundos = 0
            if(self.segundos<10):
                self.segundos = "0"+str(self.segundos)
            else:
                self.segundos = str(self.segundos)
        
        

    def previous_second(self):
        self.segundos = int(self.segundos) -1
        if(self.segundos == -1):
            self.minutos = int(self.minutos) - 1
            if(self.minutos == -1):
                self.horas = int(self.horas) -1
                self.minutos = 59
            if(self.minutos<10):
                self.minutos = "0"+str(self.minutos)
            self.segundos = 59
            if(self.segundos<10):
                self.segundos = "0"+str(self.segundos)
            else:
                self.segundos = str(self.segundos)


timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)