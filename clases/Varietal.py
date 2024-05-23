

class Varietal:
    def __init__(self, descripcion, porcentajeComposicion, tipoUva ):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    def setTipoUva(self, TipoUva):
        self.tipoUva = TipoUva