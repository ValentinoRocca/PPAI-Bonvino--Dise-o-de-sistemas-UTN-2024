import tkinter as tk
import tkinter as tk
from PIL import ImageTk, Image
from gestor import GestorActualizarVinos
from datetime import * 
class PantallaActualizacionVinos:
    # definicion de elementos que se van a usar en la clase
    def __init__(self, gestor):
        self.root = None
        self.label = None
        self.listbox = None
        self.etiqueta_resultado = None
        self.bodegas_seleccionadas = []
        self.btn_confirmar = None
        self.btn_volver = None
        self.btn_cerrar = None
        self.gestor = gestor


    # funcion que permite cerrar la ventana cuando se necesite
    def cerrar_ventana(self):
        self.btn_conf_click.set(True)
        self.btn_imp_click.set(True)
        self.root.destroy()


    # funcion que incializa todo el proceso de importacion de info nueva para cada bodega
    def opImportarActualizacionVinoBodegas(self):
        if self.listbox is not None:
            self.label.config(text='BonVino Bodegas')
            self.label.pack()
            self.listbox.delete(0, tk.END)
            if self.btn_volver is not None:
                self.btn_volver.pack_forget()
            if self.btn_cerrar is not None:
                print('el cerrar fue creado')
                self.btn_cerrar.pack_forget()    
            if self.btn_confirmar is not None:
                self.btn_confirmar.pack_forget()
                self.etiqueta_resultado.pack_forget()
            self.listbox.pack_forget()
            self.etiqueta_resultado.pack_forget()
            self.root
            self.label.pack(pady=30)
            self.btn_importar = tk.Button(self.root, text='Importar Actualizaciones', command=lambda:self.gestor.nuevaActualizacionVino(self, self.btn_imp_click))
            self.btn_importar.pack()
            self.root.wait_variable(self.btn_imp_click)
            if not self.btn_conf_click.get():
                return False
            else:
                return self.bodegas_seleccionadas
            

    # funcion que permite mostrar las bodegas disponibles para actualizar, dentro de esta tendra un boton que permite tomar la seleccion del usuario
    def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
        if self.listbox is not None:
            self.btn_imp_click.set(True)
            self.listbox.pack()
            self.btn_importar.pack_forget()
            self.label.config(text='Seleccione las bodegas')
            self.label.pack()
            self.listbox.delete(0, tk.END)
            self.etiqueta_resultado.pack_forget()
            # Agregar los productos de la bodega al Listbox
            if arregloBodegasDisp == []:
                self.btn_confirmar.pack_forget()
                self.label.config(text='NO HAY BODEGAS PARA ACTUALIZAR')
                self.label.pack(pady=20)
                self.listbox.pack_forget()
                if self.btn_cerrar is not None:
                    self.btn_cerrar.pack(pady=20)            
                else:
                    self.btn_cerrar = tk.Button(self.root, text="Cerrar", command=lambda: self.cerrar_ventana())
                    self.btn_cerrar.pack(pady=20)
            else:
                for tupla in arregloBodegasDisp:
                    self.listbox.insert(tk.END, tupla[0])
            # Botón para confirmar la selección
                if self.btn_confirmar is None:
                    self.btn_confirmar = tk.Button(self.root, text="Confirmar selección", command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
                else:
                    self.btn_confirmar.config(command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
                self.btn_confirmar.pack(pady=10)
            # Esperar hasta que se haga clic en el botón
            self.root.wait_variable(self.btn_conf_click)
    

    # funcion que permite tomar la seleccion de las bodegas
    def tomarSeleccionBodega(self, arregloBodegasDisp):
        if self.listbox is not None:
            self.btn_conf_click.set(True)
            self.etiqueta_resultado.pack()
            seleccion = self.listbox.curselection()
            self.bodegas_seleccionadas = []
            if seleccion:
                for indice in seleccion:
                    nombre_bodega_seleccionada = self.listbox.get(indice)
                    self.etiqueta_resultado.config(text=nombre_bodega_seleccionada)
                    for tupla in arregloBodegasDisp:
                        if (nombre_bodega_seleccionada == tupla[0]):
                            self.bodegas_seleccionadas.append(tupla)
                            break
                # valida que se selecciono algo, y en ese caso activa la bandera del click
                if (len(self.bodegas_seleccionadas) != 0):
                    for bodega in self.bodegas_seleccionadas:
                        self.btn_conf_click.set(True)
                        self.btn_confirmar.pack_forget()
                        

                        
    # funcion que muestra el resumen de las bodegas que fueron actualizadas
    def mostrarResumenActualizacion(self, arreglobodegaActualizadas):
        if self.listbox is not None:
            self.listbox.delete(0, tk.END) 
            self.etiqueta_resultado.pack_forget()
            self.label.config(text='Bodegas Actualizadas')
            self.label.pack()
            fecha_actual = date.today()
            # valida si no se seleccionaron bodegas
            if arreglobodegaActualizadas == []:
                self.etiqueta_resultado.config(text='NO SE SELECCIONARON BODEGAS', font=(20))
                self.etiqueta_resultado.pack(pady=20)
                self.listbox.pack_forget()
                self.btn_confirmar.pack_forget()
                self.btn_volver = tk.Button(self.root, text='Volver', command=lambda:self.opImportarActualizacionVinoBodegas())
                self.btn_volver.pack()
            else:
                for bodega in arreglobodegaActualizadas:
                    self.listbox.insert(tk.END, (50 * '----------'))
                    self.listbox.insert(tk.END, (f'{bodega.nombre}'))
                    self.listbox.insert(tk.END, (50 * '----------'))
                    for vino in bodega.vinos:
                        if vino.fechaAct == fecha_actual:
                            
                            self.listbox.insert(tk.END, ( f'{vino}'))

            if self.btn_volver is not None:
                self.btn_volver.config(text='Volver', command=lambda:self.opImportarActualizacionVinoBodegas())
                self.btn_volver.pack(pady=20)
            else:
                self.btn_volver = tk.Button(self.root, text='Volver', command=lambda:self.opImportarActualizacionVinoBodegas())
                self.btn_volver.pack(pady=20)

            if self.btn_cerrar is not None:
                self.btn_cerrar.pack()
            else:
                self.btn_cerrar = tk.Button(self.root, text="Cerrar", command=lambda: self.cerrar_ventana())
                self.btn_cerrar.pack()

                
    def cargar_imagen_de_fondo(self, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((750, 750), Image.AFFINE)
        foto = ImageTk.PhotoImage(imagen)
        self.background_label = tk.Label(self.root, image=foto)
        self.background_label.image = foto  # Conserva una referencia
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)   
        

    # funcion que inializa los elementos de la interfaz
    def habilitar_ventana(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Actualizacion de Bodegas")
        self.root.geometry("600x600")
        self.root.configure(bg='brown')
        self.cargar_imagen_de_fondo("img/bonvino.jpg")
        # Crear los widgets
        self.label = tk.Label(self.root, text="BonVino Bodegas", font=("Helvetica", 20), )
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=20, width=60, font=("Helvetica", 12))
        self.etiqueta_resultado = tk.Label(self.root, text="")
        self.btn_conf_click = tk.BooleanVar(value=False)
        self.btn_imp_click = tk.BooleanVar(value=False)

        
""""
import customtkinter as ctk
from PIL import Image
from datetime import date

class PantallaActualizacionVinos:
    def __init__(self, gestor):
        self.root = None
        self.label = None
        self.scroll_frame = None
        self.etiqueta_resultado = None
        self.bodegas_seleccionadas = []
        self.btn_confirmar = None
        self.btn_volver = None
        self.btn_cerrar = None
        self.gestor = gestor

    def cerrar_ventana(self):
        if self.root:
            self.root.destroy()

    def opImportarActualizacionVinoBodegas(self):
        if self.scroll_frame:
            self.label.configure(text='BonVino Bodegas')
            self.scroll_frame.pack_forget()

            for widget in (self.btn_volver, self.btn_cerrar, self.btn_confirmar, self.etiqueta_resultado):
                if widget:
                    widget.pack_forget()

            self.label.pack(pady=30)
            
            # Define el botón `Importar Actualizaciones` con los argumentos necesarios
            self.btn_importar = ctk.CTkButton(
                self.root,
                text='Importar Actualizaciones',
                command=lambda: self.gestor.nuevaActualizacionVino(self, self.btn_importar)
            )
            self.btn_importar.pack()

    def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
        if self.scroll_frame:
            self.scroll_frame.pack()
            self.label.configure(text='Seleccione las bodegas')

            for widget in self.scroll_frame.winfo_children():
                widget.destroy()

            if not arregloBodegasDisp:
                self.label.configure(text='NO HAY BODEGAS PARA ACTUALIZAR')
                if self.btn_cerrar is None:
                    self.btn_cerrar = ctk.CTkButton(self.root, text="Cerrar", command=self.cerrar_ventana)
                self.btn_cerrar.pack(pady=20)
            else:
                for tupla in arregloBodegasDisp:
                    bodega_label = ctk.CTkCheckBox(self.scroll_frame, text=tupla[0], 
                                                command=lambda t=tupla: self.bodegas_seleccionadas.append(t))
                    bodega_label.pack(anchor='w')
                print("entro ak1 bodeg selecc", self.bodegas_seleccionadas)

                if self.btn_confirmar is None:
                    print("entro ak2")
                    self.btn_confirmar = ctk.CTkButton(self.root, text="Confirmar selección", 
                                                    command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))  # Pasa el arreglo correctamente
                self.btn_confirmar.pack(pady=10)

            self.root.wait_variable(self.btn_conf_click)
            print("selec bodegas arreglo funcion", self.bodegas_seleccionadas)

    def actualizarBodegasSeleccionadas(self, tupla):
        
        if tupla in self.bodegas_seleccionadas:
            self.bodegas_seleccionadas.remove(tupla)
        else:
            self.bodegas_seleccionadas.append(tupla)
        
        # Actualiza el estado del botón Confirmar
        if len(self.bodegas_seleccionadas) > 0:
            self.btn_confirmar.configure(state="normal")  # Habilitar el botón de confirmar
        else:
            self.btn_confirmar.configure(state="disabled")  # Deshabilitar el botón de confirmar

    def tomarSeleccionBodega(self, arregloBodegasDisp):
        # Limpiamos la lista de bodegas seleccionadas
        self.bodegas_seleccionadas = []
        
        for checkbox in self.scroll_frame.winfo_children():
            if isinstance(checkbox, ctk.CTkCheckBox):  # Solo procesamos los CTkCheckBox
                if checkbox.get():  # Si el checkbox está seleccionado
                    bodega_seleccionada = checkbox.cget('text')  # El nombre de la bodega es el texto del checkbox
                    
                    # Actualizamos la etiqueta de resultado
                    self.etiqueta_resultado.configure(text=f"Seleccionado: {bodega_seleccionada}")
                    
                    # Buscamos la bodega en el arreglo de bodegas disponibles
                    for tupla in arregloBodegasDisp:
                        if bodega_seleccionada == tupla[0]:  # Si el nombre coincide
                            self.bodegas_seleccionadas.append(tupla)
                            break

        print("selecc bodega arr", self.bodegas_seleccionadas)

        # Si se han seleccionado bodegas, activamos la confirmación
        if len(self.bodegas_seleccionadas) > 0:
            self.btn_conf_click.set(1)  # Cambia el valor de btn_conf_click para activar el botón
        else:
            self.btn_conf_click.set(0)  # Desactiva el botón si no hay bodegas seleccionadas

    def mostrarResumenActualizacion(self, arreglobodegaActualizadas):
        if self.scroll_frame:
            for widget in self.scroll_frame.winfo_children():
                widget.destroy()

            self.label.configure(text='Bodegas Actualizadas')
            fecha_actual = date.today()

            if not arreglobodegaActualizadas:
                self.etiqueta_resultado.configure(text='NO SE SELECCIONARON BODEGAS')
                self.etiqueta_resultado.pack(pady=20)
                if self.btn_volver is None:
                    self.btn_volver = ctk.CTkButton(self.root, text='Volver', command=self.opImportarActualizacionVinoBodegas)
                self.btn_volver.pack(pady=20)
            else:
                for bodega in arreglobodegaActualizadas:
                    header_label = ctk.CTkLabel(self.scroll_frame, text=f'---------- {bodega.nombre} ----------')
                    header_label.pack(anchor='w', pady=5)

                    for vino in bodega.vinos:
                        if vino.fechaAct == fecha_actual:
                            vino_label = ctk.CTkLabel(self.scroll_frame, text=str(vino))
                            vino_label.pack(anchor='w')

                if self.btn_volver is None:
                    self.btn_volver = ctk.CTkButton(self.root, text='Volver', command=self.opImportarActualizacionVinoBodegas)
                self.btn_volver.pack(pady=20)

                if self.btn_cerrar is None:
                    self.btn_cerrar = ctk.CTkButton(self.root, text="Cerrar", command=self.cerrar_ventana)
                self.btn_cerrar.pack()

    def cargar_imagen_de_fondo(self, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        foto = ctk.CTkImage(imagen, size=(750, 750))
        self.background_label = ctk.CTkLabel(self.root, image=foto, text="")
        self.background_label.image = foto
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def habilitar_ventana(self):
        self.root = ctk.CTk()
        self.root.title("Actualización de Bodegas")
        self.root.geometry("600x600")
        self.root.configure(bg='brown')
        self.cargar_imagen_de_fondo("img/bonvino.jpg")

        self.label = ctk.CTkLabel(self.root, text="BonVino Bodegas", font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self.root, width=400, height=400)
        self.scroll_frame.pack(pady=20)

        self.etiqueta_resultado = ctk.CTkLabel(self.root, text="")
        self.etiqueta_resultado.pack()

        self.btn_confirmar = ctk.CTkButton(self.root, text="Confirmar selección", state="disabled", command=self.tomarSeleccionBodega)
        self.btn_conf_click = ctk.IntVar()

        self.opImportarActualizacionVinoBodegas()
        self.root.mainloop()
"""



