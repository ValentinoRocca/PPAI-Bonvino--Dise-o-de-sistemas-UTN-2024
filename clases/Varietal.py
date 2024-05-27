

class Varietal:
    def __init__(self, descripcion, porcentajeComposicion, tipoUva ):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    def setTipoUva(self, TipoUva):
        self.tipoUva = TipoUva

    def __str__(self):
        return f'|Tipo de Uva: {self.tipoUva} con un {self.porcentajeComposicion} % en el vino |'