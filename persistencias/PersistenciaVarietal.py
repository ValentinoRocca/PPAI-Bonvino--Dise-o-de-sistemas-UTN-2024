# persistencias/PersistenciaVarietal.py

from peewee import SqliteDatabase, Model, TextField, FloatField, ForeignKeyField, IntegrityError
from persistencias.PersistenciaBase import PersistenciaBase
from persistencias.PersistenciaTipoUva import TipoUva  # Importar el modelo TipoUva

# Configuración de la base de datos (usar la misma base que en otros modelos)
db = SqliteDatabase('bodegas.db')

# Definir el modelo Varietal
class Varietal(Model):
    descripcion = TextField()
    porcentajeComposicion = FloatField()
    tipoUva = ForeignKeyField(TipoUva, backref='varietales')

    class Meta:
        database = db

# Crear tabla si no existe
db.connect()
db.create_tables([Varietal], safe=True)

# Clase de persistencia para Varietal
class PersistenciaVarietal(PersistenciaBase):
    def agregar(self, varietal_obj):
        # Verificar si ya existe un varietal similar en la base de datos
        if Varietal.select().where(Varietal.descripcion == varietal_obj.descripcion).exists():
            print("El varietal ya existe en la base de datos.")
            return None

        try:
            # Crear el varietal si no existe
            varietal = Varietal.create(
                descripcion=varietal_obj.descripcion,
                porcentajeComposicion=varietal_obj.porcentajeComposicion,
                tipoUva=varietal_obj.tipoUva.id  # Debe ser una instancia de TipoUva con id
            )
            return varietal
        except IntegrityError as e:
            print(f"Error al agregar el varietal: {e}")
            return None

    def obtener_por_id(self, varietal_id):
        try:
            return Varietal.get(Varietal.id == varietal_id)
        except Varietal.DoesNotExist:
            return None

    def obtener_todos(self):
        return list(Varietal.select())

    def obtener_por_descripcion(self, descripcion):
        try:
            return Varietal.get(Varietal.descripcion == descripcion)
        except Varietal.DoesNotExist:
            return None

    def actualizar(self, varietal_id, **campos):
        varietal = self.obtener_por_id(varietal_id)
        if varietal:
            for campo, valor in campos.items():
                if hasattr(varietal, campo):
                    setattr(varietal, campo, valor)
            varietal.save()
            return varietal
        return None

    def eliminar(self, varietal_id):
        varietal = self.obtener_por_id(varietal_id)
        if varietal:
            varietal.delete_instance()
            return True
        return False
