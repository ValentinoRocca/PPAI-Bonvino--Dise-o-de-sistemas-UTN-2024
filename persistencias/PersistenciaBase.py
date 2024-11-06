# persistencia_base.py
from abc import ABC, abstractmethod
from peewee import Model

class PersistenciaBase(ABC):
    """Clase base abstracta para operaciones CRUD de persistencia."""
    
    @abstractmethod
    def agregar(self, **kwargs):
        """Agregar un nuevo registro en la base de datos."""
        pass

    @abstractmethod
    def obtener_por_id(self, obj_id):
        """Obtener un registro por su ID."""
        pass

    @abstractmethod
    def obtener_todos(self):
        """Obtener todos los registros."""
        pass

    @abstractmethod
    def actualizar(self, obj_id, **kwargs):
        """Actualizar un registro existente."""
        pass

    @abstractmethod
    def eliminar(self, obj_id):
        """Eliminar un registro por su ID."""
        pass
