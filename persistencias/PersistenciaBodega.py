from peewee import SqliteDatabase, Model, CharField, TextField, DateField, IntegerField
from persistencias.PersistenciaBase import PersistenciaBase

# Configuración de la base de datos
db = SqliteDatabase('bodegas.db')

# Definir el modelo Bodega
class Bodega(Model):
    coordenadas = TextField()
    descripcion = TextField()
    historia = TextField()
    nombre = CharField(max_length=100)
    periodoActualizacion = IntegerField()
    ultimaActualizacion = DateField()

    class Meta:
        database = db

# Crear tabla si no existe
db.connect()
db.create_tables([Bodega], safe=True)

# Clase de persistencia para Bodega
class PersistenciaBodega(PersistenciaBase):
    def agregar(self, bodega_obj):
        # Asegurarse de que bodega_obj es un objeto que contiene los atributos necesarios
        bodega = Bodega.create(
            coordenadas=bodega_obj.coordenadas,
            descripcion=bodega_obj.descripcion,
            historia=bodega_obj.historia,
            nombre=bodega_obj.nombre,
            periodoActualizacion=0,
            ultimaActualizacion=bodega_obj.ultimaActualizacion
        )
        return bodega

    def obtener_por_id(self, bodega_id):
        try:
            return Bodega.get(Bodega.id == bodega_id)
        except Bodega.DoesNotExist:
            return None

    def obtener_todos(self):
        return list(Bodega.select())

    def actualizar(self, bodega_id, **campos):
        # Actualizar solo los campos que han sido proporcionados
        bodega = self.obtener_por_id(bodega_id)
        if bodega:
            for campo, valor in campos.items():
                if hasattr(bodega, campo):
                    setattr(bodega, campo, valor)
            bodega.save()
            return bodega
        return None

    def eliminar(self, bodega_id):
        bodega = self.obtener_por_id(bodega_id)
        if bodega:
            bodega.delete_instance()
            return True
        return False

