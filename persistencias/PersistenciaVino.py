from peewee import SqliteDatabase, Model, CharField, TextField, FloatField, DateField, ForeignKeyField, IntegerField, IntegrityError
from persistencias.PersistenciaBase import PersistenciaBase
from persistencias.PersistenciaBodega import Bodega

# Configuración de la base de datos
db = SqliteDatabase('bodegas.db')

# Definir el modelo Bodega
class Vino(Model):
    nombre = TextField()
    imagenEtiqueta = TextField()
    notaCataVino = TextField()
    precio = FloatField()
    añada = IntegerField()
    bodega = ForeignKeyField(Bodega, backref='vinos', on_delete='CASCADE')  # Clave foránea a Bodega
    fechaAct = DateField()

    class Meta:
        database = db

# Crear tabla si no existe
db.connect()
db.create_tables([Vino], safe=True)

# Clase de persistencia para Vino
class PersistenciaVino(PersistenciaBase):
    def agregar(self, vino_obj, bodega_obj):
        

        vino_existente = Vino.select().where(
            Vino.nombre == vino_obj.nombre,
            Vino.bodega == bodega_obj.id
        ).first()
        if vino_existente:
            print(f"El vino '{vino_obj.nombre}' ya existe en la bodega '{bodega_obj.nombre}'. No se ha agregado.")
            return vino_existente
       
        try:
            # Crear la bodega si no existe
            vino = Vino.create(
                nombre=vino_obj.nombre,
                imagenEtiqueta=vino_obj.imagenEtiqueta,
                notaCataVino=vino_obj.notaCataVino,
                precio=vino_obj.precio,
                añada=vino_obj.añada,
                bodega=bodega_obj.id,
                fechaAct=vino_obj.fechaAct
            )
            return vino
        except IntegrityError as e:
            print(f"Error al agregar el vino: {e}")
            return None

    def obtener_por_id(self, vino_id):
        try:
            return Vino.get(Vino.id == vino_id)
        except Vino.DoesNotExist:
            return None

    def obtener_por_id_bodega(self, bodega_id):
        try:
            # Usar select() para obtener todos los vinos asociados a la bodega
            return list(Vino.select().where(Vino.bodega == bodega_id))
        except Vino.DoesNotExist:
            return []  # Retorna una lista vacía si no hay vinos asociados a la bodega


    def obtener_todos(self):
        return list(Vino.select())

    def actualizar(self, vino_id, **campos):
        # Actualizar solo los campos que han sido proporcionados
        print("entro a actualizar", vino_id)

        vino = self.obtener_por_id(vino_id)

        
        if vino:
            for campo, valor in campos.items():
                if hasattr(vino, campo):
                    setattr(vino, campo, valor)
            vino.save()
            return vino
        return None

    def eliminar(self, vino_id):
        vino = self.obtener_por_id(vino_id)
        if vino:
            vino.delete_instance()
            return True
        return False