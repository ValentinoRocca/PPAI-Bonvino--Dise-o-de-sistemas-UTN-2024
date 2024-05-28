from clases import Bodega
from clases import Enofilo
from clases import Vino
from clases import Varietal
from clases import TipoUva
from clases import Maridaje
from gestor import GestorActualizarVinos
import gestor
from interfaz import Interfaz
from declaracionesLocal import bodegasSistema
from declaracionesLocal import maridajesSistemas
from declaracionesLocal import uvasSistemas

gestor = GestorActualizarVinos()

def main(gestor, arregloBodegasDisp, arregloMaridajes, arregloUvas):
        gestor.cargarDatosAlSistema(arregloBodegasDisp, arregloMaridajes, arregloUvas)
        interfaz = Interfaz(gestor)
        interfaz.habilitar_ventana() 
        interfaz.opImportarActualizacionVinoBodegas()
        interfaz.root.mainloop()


main(gestor, bodegasSistema, maridajesSistemas, uvasSistemas)












