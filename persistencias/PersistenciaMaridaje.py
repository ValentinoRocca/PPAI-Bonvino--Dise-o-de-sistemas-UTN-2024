from peewee import SqliteDatabase, Model, CharField, TextField, DateField, IntegerField, IntegrityError
from persistencias.PersistenciaBase import PersistenciaBase

# Configuración de la base de datos
db = SqliteDatabase('bodegas.db')

# Definir el modelo Maridaje
class Maridaje(Model):
    descripcion = TextField()
    nombre = TextField()

    class Meta:
        database = db

# Crear tabla si no existe
db.connect()
db.create_tables([Maridaje], safe=True)

# Clase de persistencia para Maridaje
class PersistenciaMaridaje(PersistenciaBase):
    def agregar(self, maridaje_obj):
        # Verificar si ya existe una bodega con el mismo nombre
        if Maridaje.select().where(Maridaje.nombre == maridaje_obj.nombre).exists():
            print("El maridaje ya existe en la base de datos.")
            return None

        try:
            # Crear la bodega si no existe
            maridaje = Maridaje.create(
                nombre=maridaje_obj.nombre,
                descripcion=maridaje_obj.descripcion,
                
            )
            return maridaje
        except IntegrityError as e:
            print(f"Error al agregar el maridaje: {e}")
            return None

    def obtener_por_id(self, maridaje_id):
        try:
            return Maridaje.get(Maridaje.id == maridaje_id)
        except Maridaje.DoesNotExist:
            return None

    def obtener_todos(self):
        return list(Maridaje.select())
    
    def obtener_por_nombre(self, nombre):
        try:
            return Maridaje.get(Maridaje.nombre == nombre)
        except Maridaje.DoesNotExist:
            return None

    def actualizar(self, maridaje_id, **campos):
        # Actualizar solo los campos que han sido proporcionados
        maridaje = self.obtener_por_id(maridaje_id)
        if maridaje:
            for campo, valor in campos.items():
                if hasattr(maridaje, campo):
                    setattr(maridaje, campo, valor)
            maridaje.save()
            return maridaje
        return None

    def eliminar(self, maridaje_id):
        maridaje = self.obtener_por_id(maridaje_id)
        if maridaje:
            maridaje.delete_instance()
            return True
        return False
