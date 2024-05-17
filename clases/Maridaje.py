class Maridaje:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def sosMaridaje(self, maridajeAPI):
        if (self.nombre == maridajeAPI):
            return True
        else:
            return False