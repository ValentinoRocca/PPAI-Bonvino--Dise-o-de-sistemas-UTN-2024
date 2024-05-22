import tkinter as tk
from Bodega import Bodega
import datetime
import gestor


#def inicializar_interfaz(bodega):

# Crear una instancia de la clase MiClase
#objeto_clase = bodega

fecha = datetime.datetime(2024,1,17)
fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)

bodega = Bodega('aa', 'aa','aa', 'Malbec', 2, fecha )
bodega2 = Bodega('aa', 'aa','aa', 'Don Valetin', 2, fecha2 )
bodega3 = Bodega('aa', 'aa','aa', 'Otro Loco', 2, fecha3 )

arregloBodegasDisp = gestor.buscarBodegasAActualizar(arrayBodega)


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con botón para función de clase")
root.geometry("750x750")
root.configure(bg='brown')

# Crear una etiqueta
label = tk.Label(root, text="BonVino Bodegas")
label.pack(pady=10)  # Empaquetar la etiqueta en la ventana con un poco de padding


def mostrarBodegasActDisponibles(arregloBodegasDisp, etiqueta):

    # Crear una lista de selección (Listbox)
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    listbox.pack(pady=20)

    # Agregar los productos de la bodega al Listbox
    for bodega in arregloBodegasDisp:
        listbox.insert(tk.END, bodega.nombre)

    # Función para mostrar la selección en la etiqueta
    def mostrar_seleccion():
        seleccion = listbox.curselection()
        if seleccion:
            indice_seleccionado = seleccion[0]
            bodega_seleccionada = listbox.get(indice_seleccionado)
            etiqueta_resultado.config(text=bodega_seleccionada)

            


            # si quiero mostrar muchas
            # bodegasSeleccionadas = [listbox.get(i) for i in seleccion]
            # etiqueta_resultado.config(text=", ".join(bodegasSeleccionadas))


    # Botón para confirmar la selección
    btn_confirmar = tk.Button(root, text="Confirmar selección", command=mostrar_seleccion)
    btn_confirmar.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack()

    # Función que se ejecutará al hacer clic en el botón
def acceder_funcion_clase(arregloBodegas, etiqueta_resultado):
    # Llama a la función de la clase
    fechaAct = datetime.datetime.now()
    arregloBodegasDisp = []

    for bodega in arregloBodegas:
        resultado = bodega.estaDisponible(fechaAct)
        if resultado: 
            arregloBodegasDisp.append(bodega)
        else:
            etiqueta_resultado.config(text='FALSO')
    
    mostrarBodegasActDisponibles(arregloBodegasDisp, etiqueta_resultado)

# Crear el botón
boton = tk.Button(root, text="Mostrar Bodegas Disponibles", command=lambda: mostrarBodegasActDisponibles(arregloBodegasDisp, etiqueta_resultado))
boton.pack(pady=50)

# Iniciar el bucle principal de Tkinter
root.mainloop()