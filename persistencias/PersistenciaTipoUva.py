from peewee import SqliteDatabase, Model, TextField, IntegrityError
from persistencias.PersistenciaBase import PersistenciaBase

# Configuración de la base de datos (usar la misma base que en PersistenciaMaridaje)
db = SqliteDatabase('bodegas.db')

# Definir el modelo TipoUva
class TipoUva(Model):
    descripcion = TextField()
    nombre = TextField()

    class Meta:
        database = db

# Crear tabla si no existe
db.connect()
db.create_tables([TipoUva], safe=True)

# Clase de persistencia para TipoUva
class PersistenciaTipoUva(PersistenciaBase):
    def agregar(self, tipo_uva_obj):
        # Verificar si ya existe un tipo de uva con el mismo nombre
        if TipoUva.select().where(TipoUva.nombre == tipo_uva_obj.nombre).exists():
            print("El tipo de uva ya existe en la base de datos.")
            return None

        try:
            # Crear el tipo de uva si no existe
            tipo_uva = TipoUva.create(
                nombre=tipo_uva_obj.nombre,
                descripcion=tipo_uva_obj.descripcion,
            )
            return tipo_uva
        except IntegrityError as e:
            print(f"Error al agregar el tipo de uva: {e}")
            return None

    def obtener_por_id(self, tipo_uva_id):
        try:
            return TipoUva.get(TipoUva.id == tipo_uva_id)
        except TipoUva.DoesNotExist:
            return None

    def obtener_todos(self):
        return list(TipoUva.select())

    def obtener_por_nombre(self, nombre):
        try:
            return TipoUva.get(TipoUva.nombre == nombre)
        except TipoUva.DoesNotExist:
            return None

    def actualizar(self, tipo_uva_id, **campos):
        tipo_uva = self.obtener_por_id(tipo_uva_id)
        if tipo_uva:
            for campo, valor in campos.items():
                if hasattr(tipo_uva, campo):
                    setattr(tipo_uva, campo, valor)
            tipo_uva.save()
            return tipo_uva
        return None

    def eliminar(self, tipo_uva_id):
        tipo_uva = self.obtener_por_id(tipo_uva_id)
        if tipo_uva:
            tipo_uva.delete_instance()
            return True
        return False
