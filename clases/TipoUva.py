class TipoUva:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def sosTipoUva(self, tipoUvaAPI):
        if (self.nombre == tipoUvaAPI):
            return True
        else:
            return False
