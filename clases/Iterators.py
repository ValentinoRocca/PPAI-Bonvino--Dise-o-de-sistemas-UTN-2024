from clases.IteratorAbs import InterfazIterator

from clases.Bodega import Bodega
# Implementación para el iterador de vinos desde API
class IteradorVinosBodegaApi(InterfazIterator):
    def __init__(self, vinos_api):
        super().__init__(vinos_api)

    def tieneSiguiente(self):
        return self.index < len(self.vinos)

    def actual(self):
        return self.vinos[self.index]

    def siguiente(self):
        self.index += 1

    def primero(self):
        self.index = 0

    def cumpleFiltro(self):
        pass

# Implementación para el iterador de vinos de la bodega
class IteradorVinosBodega(InterfazIterator):
    def __init__(self, vinos_bodega):
        super().__init__(vinos_bodega)

    def tieneSiguiente(self):
        return self.index < len(self.vinos)

    def actual(self):
        return self.vinos[self.index]

    def siguiente(self):
        self.index += 1

    def primero(self):
        self.index = 0

    def cumpleFiltro(vinoApi, vino):
        return Bodega.sosElMismoVino(vino, vinoApi)
       
        

            
