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


class IteradorVinosBodega:
    def __init__(self, vinos_bodega):
        self.vinos_bodega = vinos_bodega
        self.index = 0

    def tieneSiguiente(self):
        return self.index < len(self.vinos_bodega) or len(self.vinos_bodega) == 0

    def actual(self):
            if len(self.vinos_bodega) == 0:
                 return False
            else:
                vino = self.vinos_bodega[self.index]
                return vino
        
    def siguiente(self):
        if len(self.vinos_bodega) != 0:
            self.index += 1
            
