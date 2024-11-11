from clases.InterfazBodega import InterfazBodega
from gestor import GestorActualizarVinos
from interfaz import PantallaPrincipal
from declaracionesLocal import bodegasSistema
from declaracionesLocal import maridajesSistema
from declaracionesLocal import uvasSistemas


interfazApi = InterfazBodega()
gestor = GestorActualizarVinos(interfazApi)

def main(gestor, arregloBodegasDisp, arregloMaridajes, arregloUvas):
        gestor.cargarDatosAlSistema(arregloBodegasDisp, arregloMaridajes, arregloUvas)
        interfaz = PantallaPrincipal(gestor)
        interfaz.habilitar_ventana() 
        interfaz.opImportarActualizacionVinoBodegas()
        interfaz.root.mainloop()


main(gestor, bodegasSistema, maridajesSistema, uvasSistemas)












