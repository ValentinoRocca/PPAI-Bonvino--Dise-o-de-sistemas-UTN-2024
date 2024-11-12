from persistencias.PersistenciaMaridaje import PersistenciaMaridaje
from persistencias.PersistenciaVinoMaridaje import PersistenciaVinoMaridaje

class Maridaje:
    def __init__(self, descripcion, nombre, id=None):
        self.id = id
        self.descripcion = descripcion
        self.nombre = nombre
        self.persistenciaMaridaje = PersistenciaMaridaje()
        self.persistenciaVinoMaridaje = PersistenciaVinoMaridaje()
    
    def sosMaridaje(self, nombreMaridajeAPI):
        if (self.nombre == nombreMaridajeAPI):
            return True
        else:
            return False
        
    def persistirMaridaje(self):
        maridaje = self.persistenciaMaridaje.agregar(self)
        if maridaje:
            self.id = maridaje.id
        else:
            print("error al persistir")

    def persistirVinoMaridaje(self, vino):
        vinomaridaje = self.persistenciaVinoMaridaje.agregar(self, vino)
        if vinomaridaje:
            print("persistio correctamente vinomaridaje")
        else:
            print("error al persistir vinomaridaje")
            
    def __str__(self):
        return f' |{self.nombre}|'
        