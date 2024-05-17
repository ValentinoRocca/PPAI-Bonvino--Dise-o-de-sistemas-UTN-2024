import tkinter as tk
from Bodega  import Bodega
import datetime

def inicializar_interfaz(bodega):

    # Crear una instancia de la clase MiClase
    #objeto_clase = bodega
    

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Interfaz con botón para función de clase")
    root.geometry("500x500")
    root.configure(bg='brown')

    # Crear una etiqueta
    label = tk.Label(root, text="BonVino Bodegas")
    label.pack(pady=10)  # Empaquetar la etiqueta en la ventana con un poco de padding

    # Crear una etiqueta para mostrar el resultado
    etiqueta_resultado = tk.Label(root, text="")
    etiqueta_resultado.pack()

     # Función que se ejecutará al hacer clic en el botón
    def acceder_funcion_clase():
        # Llama a la función de la clase
        fechaAct = datetime.datetime.now()
        resultado = bodega.estaDisponible(fechaAct)

        if resultado: 
            etiqueta_resultado.config(text=bodega.nombre)
        else:
            etiqueta_resultado.config(text='FALSO')
    
    # Crear el botón
    boton = tk.Button(root, text="Acceder a función de clase", command=acceder_funcion_clase)
    boton.pack(pady=50)

    # Iniciar el bucle principal de Tkinter
    root.mainloop()