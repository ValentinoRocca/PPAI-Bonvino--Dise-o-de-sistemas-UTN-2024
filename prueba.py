from persistencias.PersistenciaBodega import PersistenciaBodega
from declaracionesLocal import bodegasSistema

# Instanciar el objeto de persistencia para Bodega
persistencia_bodega = PersistenciaBodega()

# Supongamos que bodegasSistema[0] es un objeto con los atributos necesarios (como 'coordenadas', 'descripcion', etc.)
bodega1 = bodegasSistema[0]

# Agregar una nueva bodega
nueva_bodega = persistencia_bodega.agregar(bodega1)

# Imprimir la nueva bodega agregada (usando los atributos que realmente existen)
print(f"Bodega agregada: {nueva_bodega.nombre}, {nueva_bodega.coordenadas}, {nueva_bodega.descripcion}")

# Obtener todas las bodegas
bodegas = persistencia_bodega.obtener_todos()
for bodega in bodegas:
    print(f"Nombre: {bodega.nombre}, Coordenadas: {bodega.coordenadas}, Descripción: {bodega.descripcion}, "
          f"Periodo de Actualización: {bodega.periodoActualizacion}, Última Actualización: {bodega.ultimaActualizacion}")

