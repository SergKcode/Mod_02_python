class Termometro()
#como se construye

    def __init__ (self)
        self.unidadM= "C"
        self.temperatura= 0
        
#como se imprime        
 
    def __str__(self):
        return return "{} º {}". format (self. temperatura, self.unidadM)
#getter y setter  
    
    def unidadMedida(self, uniM=None)
        if uniM == None:
            return self.__unidadM
        else:
            if uniM== "F" or uniM== "C":
                self.__unidadM= uniM
                
    def temp(self,temperatura=None):
        if temperatura==None:
            return self.__temperatura
        else:
            self._temperatura= temperatura
            
#funcionalidad           
            
   def conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{} º F". format (temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{} º C". format ((temperatura -32) * 5/9)
        else:
            return "unidad incorrecta"            
            
    
    def mide(self,uniM=None)
        if uniM==None or uniM==self.unidadM:
            return self._str_()
        else:
            return self. conversor (self.temperatura, uniM)