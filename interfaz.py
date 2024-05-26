import tkinter as tk
import tkinter as tk
from PIL import ImageTk, Image
from gestor import GestorActualizarVinos
import datetime

class Interfaz:
    def __init__(self):
        self.root = None
        self.label = None
        self.listbox = None
        self.etiqueta_resultado = None
        self.bodegas_seleccionadas = []
        self.btn_confirmar = None
        

    def cerrar_ventana(self):
        self.root.destroy()

    

    def opImportarActBodegas(self, arregloBodegasDisp):
        
        self.gestor = GestorActualizarVinos()
    
        if self.listbox is not None:
            self.label.pack(pady=30)

            self.btn_importar = tk.Button(self.root, text='Importar Actualizaciones', command=lambda:self.gestor.nuevaActualizacionVino(self, arregloBodegasDisp, self.btn_imp_click))
            self.btn_importar.pack()

            self.root.wait_variable(self.btn_imp_click)

            if not self.btn_conf_click.get():
                return False
            else:
                return self.bodegas_seleccionadas


    def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
        if self.listbox is not None:

            self.btn_imp_click.set(True)
            self.listbox.pack()
            self.btn_importar.pack_forget()

            self.label.config(text='Selecciones las bodegas')
            self.label.pack()
            # Limpiar la lista actual antes de agregar nuevas entradas
            self.listbox.delete(0, tk.END)
            self.mostrarTupla = tk.Label(self.root)

            self.etiqueta_resultado.pack_forget()

            # Agregar los productos de la bodega al Listbox
            if arregloBodegasDisp == []:
                self.listbox.insert(tk.END, 'NO HAY BODEGAS A ACTUALIZAR')  
                boton_cerrar = tk.Button(self.root, text="Cerrar", command=lambda: self.cerrar_ventana())
                boton_cerrar.pack(pady=20)
            
            else:
                for tupla in arregloBodegasDisp:
                    self.listbox.insert(tk.END, tupla[0])

            # Botón para confirmar la selección
                if self.btn_confirmar is None:
                    self.btn_confirmar = tk.Button(self.root, text="Confirmar selección", command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
                else:
                    self.btn_confirmar.config(command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
                
                self.btn_confirmar.pack(pady=10)

            #self.load_image("img/bonvino.jpg")

            # Esperar hasta que se haga clic en el botón
            self.root.wait_variable(self.btn_conf_click)

            # Devolver la bodega seleccionada o False si no se hizo clic en el botón
            
            
            


            # Función para mostrar la selección en la etiqueta
    def tomarSeleccionBodega(self, arregloBodegasDisp):

        self.btn_conf_click.set(True)
        self.etiqueta_resultado.pack()
        seleccion = self.listbox.curselection()

        print('entro a tomar seleccion')
        if seleccion:
            for indice in seleccion:
                #indice_seleccion = seleccion[0]
                nombre_bodega_seleccionada = self.listbox.get(indice)
                self.etiqueta_resultado.config(text=nombre_bodega_seleccionada)

                for tupla in arregloBodegasDisp:
                    if (nombre_bodega_seleccionada == tupla[0]):
                        self.bodegas_seleccionadas.append(tupla)
                        break


            if (len(self.bodegas_seleccionadas) != 0):
                for bodega in self.bodegas_seleccionadas:
                    self.mostrarTupla.config(text=f'{bodega[0]}, {bodega[1]}')
                    self.mostrarTupla.pack(pady=20)
                    self.btn_conf_click.set(True)
                    self.btn_confirmar.pack_forget()

            print('entro aca', self.bodegas_seleccionadas)

            

    
    def mostrarResumenActualizacion(self, arreglobodegaActualizadas):
        if self.listbox is not None:
            self.listbox.delete(0, tk.END) 

            hoy = datetime.datetime.now()
            
            if arreglobodegaActualizadas == []:
                self.listbox.insert(tk.END, ('NO SE SELECCIONO NINGUNA BODEGA'))
            
            else:
                for bodega in arreglobodegaActualizadas:
                    for vino in bodega.vinos:
                        if vino.fechaAct == hoy:
                            self.listbox.insert(tk.END, (f'{bodega.nombre}', f'{vino}'))

    
    
    
    '''
    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((1000, 300), Image.AFFINE)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack(pady=10)
        self.image_label(x=0, y=0, relwidth=1, relheight=1)
    '''

    def cargar_imagen_de_fondo(self, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((750, 750), Image.AFFINE)
        foto = ImageTk.PhotoImage(imagen)
        self.background_label = tk.Label(self.root, image=foto)
        self.background_label.image = foto  # Conserva una referencia
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
    def iniciar_interfaz(self):
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