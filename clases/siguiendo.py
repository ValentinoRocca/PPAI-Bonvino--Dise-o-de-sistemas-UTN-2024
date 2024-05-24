class Siguiendo:
    def __init__(self, fechaFin, fechaInicio, bodega):
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.bodega = bodega


    def sosDeBodega(self, bodegaAPreguntar):
        if bodegaAPreguntar.nombre == self.bodega.nombre:
            return True

