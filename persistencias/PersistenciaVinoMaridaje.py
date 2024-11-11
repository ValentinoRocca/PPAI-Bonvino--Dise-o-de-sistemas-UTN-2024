from peewee import SqliteDatabase, Model, ForeignKeyField, IntegrityError
from persistencias.PersistenciaVino import Vino
from persistencias.PersistenciaMaridaje import Maridaje  # Suponiendo que ya tienes un modelo Maridaje

# Definir el modelo VinoMaridaje
class VinoMaridaje(Model):
    vino = ForeignKeyField(Vino, backref='maridajes')  # Relación con el modelo Vino
    maridaje = ForeignKeyField(Maridaje, backref='vinos')  # Relación con el modelo Maridaje

    class Meta:
        database = db  # Conexión a la base de datos
        indexes = ((('vino', 'maridaje'), True),)  # Asegura que no se repitan las combinaciones de vino y maridaje

# Crear la tabla si no existe
db.connect()
db.create_tables([VinoMaridaje], safe=True)


class PersistenciaVinoMaridaje(PersistenciaBase):
    def agregar(self, vino_obj, maridaje_obj):
        try:
            # Crear la relación entre vino y maridaje
            vino_maridaje = VinoMaridaje.create(
                vino=vino_obj.id,
                maridaje=maridaje_obj.id
            )
            return vino_maridaje
        except IntegrityError as e:
            print(f"Error al agregar la relación vino-maridaje: {e}")
            return None

    def obtener_por_id(self, vino_maridaje_id):
        try:
            return VinoMaridaje.get(VinoMaridaje.id == vino_maridaje_id)
        except VinoMaridaje.DoesNotExist:
            return None

    def obtener_todos(self):
        return list(VinoMaridaje.select())

    def eliminar(self, vino_obj, maridaje_obj):
        try:
            # Eliminar la relación entre un vino y un maridaje
            vino_maridaje = VinoMaridaje.get(
                (VinoMaridaje.vino == vino_obj.id) & (VinoMaridaje.maridaje == maridaje_obj.id)
            )
            vino_maridaje.delete_instance()
            return True
        except VinoMaridaje.DoesNotExist:
            print("La relación vino-maridaje no existe")
            return False
