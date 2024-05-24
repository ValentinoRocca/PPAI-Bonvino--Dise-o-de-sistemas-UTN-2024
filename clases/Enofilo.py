class Enofilo: 
    def __init__(self,nombre,apellido,imagenPerfil,usuario):
        self.nombre = nombre,
        self.apellido = apellido,
        self.imagenPerfil = imagenPerfil,
        self.usuario = usuario,
        self.siguiendos = []
    

    def agregar_siguiendo(self,siguiendo):
        self.siguiendos.append(siguiendo)
    
    def estaSuscrito(self, bodega):
        for i in range (self.siguiendos):
            if i == bodega:
             print("El Enófilo ", self.nombre, "está suscrito a la bodega ", bodega)
             return True
            else:
                print("El Enófilo ", self.nombre, " no está suscrito a la bodega ", bodega)
                return False
    
    def getNombre(self):
        print("El nombre del Enófilo es ", self.nombre)
        return self.nombre

    def estaSuscriptoABodega(self, bodega):
        for siguiendo in self.siguiendos:
                if siguiendo.sosDeBodega(bodega):
                    return True
        return False

    def obtenerNombreUsuario(self):
        return self.usuario.getNombre()
