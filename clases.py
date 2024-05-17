class Bodega:
    def __init__(self, coordenadaUbicacion, descripcion,historia,nombre,periodoActualizacion):
        self.coordenadas = coordenadaUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoAct= periodoActualizacion

    

class Enofilo: 
    def __init__(self,nombre,apellido,imagenPerfil):
        self.nombre = nombre,
        self.apellido = apellido,
        self.imagenPerfil = imagenPerfil,
    
    def estaSuscrito():
        pass
    def obtenerNombreUsuario(self, nombre):
        return self.nombre

    
class Maridaje:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def sosMaridaje():
        pass
    def maridaConVino():
        pass


class TipoUva:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre
    
    def sosTipoUva():
        pass


class Usuario:
    def __init__(self,nombre,mail,password):
        self.nombre= nombre
        self.mail = mail,
        self.password = password,
    
    def getNombre():
        pass
    
    def setMail(self, nuevoMail):
        self.mail = nuevoMail


class Varietal:
    def __init__(self, descripcion, porcentajeComposicion, tipoUva ):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva
    def new():
        pass

    def conocerTipoUva():
        pass

        
    
    

class Siguiendo:
    def __init__(self, fechaFin, fechaInicio, bodega):
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.bodega = bodega




class Reseña: 
    def __init__(self,comentario,fechaReseña,puntaje,esPremium):
        self.comentario = comentario
        self.fechaReseña = fechaReseña
        self.puntaje = puntaje
        self.esPremium = esPremium


class Certificacion: 
    def __init__(self,adjuntoURL,descripcion,fechafin,fechaInicio, InstitucionOtorgante, nombre):
        self.adjuntoURL= adjuntoURL        
        self.fechaInicio = fechaInicio
        self.descripcion = descripcion
        self.fechafin = fechafin
        self.InstitucionOtorgante = InstitucionOtorgante
        self.nombre = nombre


class Sommelier: 
    def __init__(self,fechaValidacion,nombre,notaPresentacion):
        self.fechaValidacion = fechaValidacion
        self.nombre = nombre
        self.notaPresentacion = notaPresentacion


class CobroPremium: 
    def __init__(self,esAnual,fechaPago,monto, nroOperacionMercadoPago):
        self.esAnual = esAnual
        self.fechaPago = fechaPago
        self.monto = monto
        self.nroOperacionMercadoPago = nroOperacionMercadoPago

