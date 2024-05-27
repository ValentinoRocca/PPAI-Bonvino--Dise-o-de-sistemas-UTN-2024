class Maridaje:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def sosMaridaje(self, nombreMaridajeAPI):
        if (self.nombre == nombreMaridajeAPI):
            return True
        else:
            return False
    
    def __str__(self):
        return f' |{self.nombre}|'
        