class IteradorVinosBodegaApi:
    def __init__(self, vinos_api):
        self.vinos_api = vinos_api
        self.index = 0

    def tieneSiguiente(self):
        return self.index < len(self.vinos_api)

    def actual(self):
            vino = self.vinos_api[self.index]
            return vino
        

    def siguiente(self):
        self.index += 1


class VinoBodegaIterator:
    def __init__(self, vinos_bodega):
        self.vinos_bodega = vinos_bodega
        self.index = 0

    def tieneSiguiente(self):
        return self.index < len(self.vinos_bodega)

    def actual(self):
            vino = self.vinos_bodega[self.index]
            return vino
        

    def siguiente(self):
        self.index += 1

            
