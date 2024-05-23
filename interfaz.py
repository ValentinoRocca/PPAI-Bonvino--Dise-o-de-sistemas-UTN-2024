import tkinter as tk
from Bodega import Bodega
import datetime
import gestor
import tkinter as tk

class Interfaz:
    def __init__(self, root, label, listbox, etiqueta_resultado):
        self.root = root
        self.label = label
        self.listbox = listbox
        self.etiqueta_resultado = etiqueta_resultado

        self.label.config(text="BonVino Bodegas")
        self.listbox.pack(pady=20)

    def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
        # Limpiar la lista actual antes de agregar nuevas entradas
        self.listbox.delete(0, tk.END)
        self.bodega_seleccionada = None

        # Agregar los productos de la bodega al Listbox
        for tupla in arregloBodegasDisp:
            self.listbox.insert(tk.END, tupla[0])

        # Función para mostrar la selección en la etiqueta
        def tomarSeleccionBodega(arregloBodegasDisp):
            seleccion = self.listbox.curselection()
            if seleccion:
                indice_seleccionado = seleccion[0]
                nombre_bodega_seleccionada = self.listbox.get(indice_seleccionado)
                self.etiqueta_resultado.config(text=nombre_bodega_seleccionada)
                for tupla in arregloBodegasDisp:
                    if (nombre_bodega_seleccionada == tupla[0]):
                        self.bodega_seleccionada = tupla
                        break

        # Botón para confirmar la selección
        btn_confirmar = tk.Button(self.root, text="Confirmar selección", command=lambda:tomarSeleccionBodega(arregloBodegasDisp))
        btn_confirmar.pack(pady=10)

        return self.bodega_seleccionada


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Interfaz con botón para función de clase")
    root.geometry("750x750")
    root.configure(bg='brown')
    

    # Crear los widgets
    label = tk.Label(root, text="BonVino Bodegas")
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    etiqueta_resultado = tk.Label(root, text="")
    etiqueta_resultado.pack()

    # Inicializar la interfaz
    interfaz = Interfaz(root, label, listbox, etiqueta_resultado)

    arregloBodegasDisp = [('Malbec', 'coordenadas'), ('Vino Toro', 'coordenadas'), ('Otro Loco', 'coordenadas')]


    interfaz.mostrarBodegasActDisponibles(arregloBodegasDisp)

    # Mostrar la ventana
    root.mainloop()