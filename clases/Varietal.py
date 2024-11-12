from persistencias.PersistenciaVarietal import PersistenciaVarietal

class Varietal:
    def __init__(self, descripcion, porcentajeComposicion, tipoUva, id=None):
        self.id = id
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva  # Debe ser una instancia de TipoUva
        self.persistenciaVarietal = PersistenciaVarietal()

    def setTipoUva(self, tipoUva):
        self.tipoUva = tipoUva

    def persistirVarietal(self):
        varietal = self.persistenciaVarietal.agregar(self)
        if varietal:
            self.id = varietal.id
        else:
            print("Error al persistir el varietal")

    def __str__(self):
        return f'|Tipo de Uva: {self.tipoUva} con un {self.porcentajeComposicion}% en el vino|'
