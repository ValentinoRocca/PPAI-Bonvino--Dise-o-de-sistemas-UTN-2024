from abc import ABC, abstractmethod

# Clase abstracta para los iteradores de vinos
class InterfazIterator(ABC):
    def __init__(self, vinos):
        self.vinos = vinos
        self.index = None

    @abstractmethod
    def tieneSiguiente(self):
        pass

    @abstractmethod
    def actual(self):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod    
    def primero(self):
        pass

    @abstractmethod
    def cumpleFiltro(self):
        pass