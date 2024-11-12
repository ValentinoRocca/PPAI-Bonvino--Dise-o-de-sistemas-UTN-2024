from persistencias.PersistenciaTipoUva import PersistenciaTipoUva

class TipoUva:
    def __init__(self, descripcion, nombre, id=None):
        self.id = id
        self.descripcion = descripcion
        self.nombre = nombre
        self.persistenciaTipoUva = PersistenciaTipoUva()
    
    def sosTipoUva(self, tipoUvaAPI):
        return self.nombre == tipoUvaAPI

    def persistirTipoUva(self):
        tipo_uva = self.persistenciaTipoUva.agregar(self)
        if tipo_uva:
            self.id = tipo_uva.id
        else:
            print("Error al persistir el tipo de uva")
    
    def __str__(self):
        return f'{self.nombre}'
