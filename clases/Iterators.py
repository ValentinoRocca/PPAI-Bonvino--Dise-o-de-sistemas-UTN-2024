from clases.IteratorAbs import InterfazIterator


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
    def __init__(self, vinos_bodega, objeto_bodega):
        super().__init__(vinos_bodega)
        self.bodega = objeto_bodega

    def tieneSiguiente(self):
        return self.index < len(self.vinos)

    def actual(self):
        return self.vinos[self.index]

    def siguiente(self):
        self.index += 1

    def primero(self):
        self.index = 0

    def cumpleFiltro(self, vinoApi, vino):
        return self.bodega.sosElMismoVino(vino, vinoApi)
       
        

            
