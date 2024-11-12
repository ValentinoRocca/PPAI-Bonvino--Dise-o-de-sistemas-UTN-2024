
"""
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
"""


        

# class PantallaActualizacionVinos:
#     # Definición de elementos que se van a usar en la clase
#     def __init__(self, gestor):
#         self.root = None
#         self.label = None
#         self.listbox = None
#         self.etiqueta_resultado = None
#         self.bodegas_seleccionadas = []
#         self.btn_confirmar = None
#         self.btn_volver = None
#         self.btn_cerrar = None
#         self.gestor = gestor
        

#     # Función que permite cerrar la ventana cuando se necesite
#     def cerrar_ventana(self):
#         self.btn_conf_click.set(True)
#         self.btn_imp_click.set(True)
#         self.root.destroy()

#     # Función que inicializa el proceso de importación de información nueva para cada bodega
#     def opImportarActualizacionVinoBodegas(self):
#         if self.listbox is not None:
#             self.label.config(text='BonVino Bodegas')
#             self.label.pack()
#             self.listbox.delete(0, tk.END)
#             if self.btn_volver is not None:
#                 self.btn_volver.pack_forget()
#             if self.btn_cerrar is not None:
#                 print('El botón cerrar fue creado')
#                 self.btn_cerrar.pack_forget()    
#             if self.btn_confirmar is not None:
#                 self.btn_confirmar.pack_forget()
#                 self.etiqueta_resultado.pack_forget()
#             self.listbox.pack_forget()
#             self.etiqueta_resultado.pack_forget()

#             self.label.pack(pady=30)
#             self.btn_importar = ttk.Button(self.root, text='Importar Actualizaciones', bootstyle=PRIMARY, command=lambda: self.gestor.nuevaActualizacionVino(self, self.btn_imp_click))
#             self.btn_importar.pack()
#             self.root.wait_variable(self.btn_imp_click)

#             if not self.btn_conf_click.get():
#                 return False
#             else:
#                 return self.bodegas_seleccionadas

#     # Función que muestra las bodegas disponibles para actualizar
#     def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
#         if self.listbox is not None:
#             self.btn_imp_click.set(True)
#             self.listbox.pack()
#             self.btn_importar.pack_forget()
#             self.label.config(text='Seleccione las bodegas')
#             self.label.pack()
#             self.listbox.delete(0, tk.END)
#             self.etiqueta_resultado.pack_forget()

#             if arregloBodegasDisp == []:
#                 self.btn_confirmar.pack_forget()
#                 self.label.config(text='NO HAY BODEGAS PARA ACTUALIZAR')
#                 self.label.pack(pady=20)
#                 self.listbox.pack_forget()
#                 if self.btn_cerrar is not None:
#                     self.btn_cerrar.pack(pady=20)            
#                 else:
#                     self.btn_cerrar = ttk.Button(self.root, text="Cerrar", bootstyle=SECONDARY, command=lambda: self.cerrar_ventana())
#                     self.btn_cerrar.pack(pady=20)
#             else:
#                 for tupla in arregloBodegasDisp:
#                     self.listbox.insert(tk.END, tupla[0])

#                 if self.btn_confirmar is None:
#                     self.btn_confirmar = ttk.Button(self.root, text="Confirmar selección", bootstyle=SUCCESS, command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
#                 else:
#                     self.btn_confirmar.config(command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp))
#                 self.btn_confirmar.pack(pady=10)

#             self.root.wait_variable(self.btn_conf_click)

#     # Función que permite tomar la selección de las bodegas
#     def tomarSeleccionBodega(self, arregloBodegasDisp):
#         if self.listbox is not None:
#             self.btn_conf_click.set(True)
#             self.etiqueta_resultado.pack()
#             seleccion = self.listbox.curselection()
#             self.bodegas_seleccionadas = []

#             if seleccion:
#                 for indice in seleccion:
#                     nombre_bodega_seleccionada = self.listbox.get(indice)
#                     self.etiqueta_resultado.config(text=nombre_bodega_seleccionada)
#                     for tupla in arregloBodegasDisp:
#                         if nombre_bodega_seleccionada == tupla[0]:
#                             self.bodegas_seleccionadas.append(tupla)
#                             break

#                 if len(self.bodegas_seleccionadas) != 0:
#                     for bodega in self.bodegas_seleccionadas:
#                         self.btn_conf_click.set(True)
#                         self.btn_confirmar.pack_forget()

#     # Función que muestra el resumen de las bodegas que fueron actualizadas
#     def mostrarResumenActualizacion(self, arreglobodegaActualizadas):
#         if self.listbox is not None:
#             self.listbox.delete(0, tk.END) 
#             self.etiqueta_resultado.pack_forget()
#             self.label.config(text='Bodegas Actualizadas')
#             self.label.pack()
#             fecha_actual = date.today()

#             if arreglobodegaActualizadas == []:
#                 self.etiqueta_resultado.config(text='NO SE SELECCIONARON BODEGAS', font=("Helvetica", 20))
#                 self.etiqueta_resultado.pack(pady=20)
#                 self.listbox.pack_forget()
#                 self.btn_confirmar.pack_forget()
#                 self.btn_volver = ttk.Button(self.root, text='Volver', bootstyle=SECONDARY, command=lambda: self.opImportarActualizacionVinoBodegas())
#                 self.btn_volver.pack()
#             else:
#                 for bodega in arreglobodegaActualizadas:
#                     self.listbox.insert(tk.END, (50 * '----------'))
#                     self.listbox.insert(tk.END, f'{bodega.nombre}')
#                     self.listbox.insert(tk.END, (50 * '----------'))
#                     for vino in bodega.vinos:
#                         if vino.fechaAct == fecha_actual:
#                             self.listbox.insert(tk.END, f'{vino}')

#             if self.btn_volver is not None:
#                 self.btn_volver.config(text='Volver', command=lambda: self.opImportarActualizacionVinoBodegas())
#                 self.btn_volver.pack(pady=20)
#             else:
#                 self.btn_volver = ttk.Button(self.root, text='Volver', bootstyle=SECONDARY, command=lambda: self.opImportarActualizacionVinoBodegas())
#                 self.btn_volver.pack(pady=20)

#             if self.btn_cerrar is not None:
#                 self.btn_cerrar.pack()
#             else:
#                 self.btn_cerrar = ttk.Button(self.root, text="Cerrar", bootstyle=SECONDARY, command=lambda: self.cerrar_ventana())
#                 self.btn_cerrar.pack()


#     # Función que inicializa los elementos de la interfaz
#     def habilitar_ventana(self):
#         # Crear la ventana principal
#         self.root = ttk.Window(themename="superhero")  # Se usa ttkbootstrap para crear la ventana
#         self.root.title("Actualización de Bodegas")
#         self.root.geometry("600x600")
#         self.root.configure(bg="#F9D99B")
#         self.root.attributes("-fullscreen", True)
        
#         # Crear los widgets
#         self.label = ttk.Label(self.root, text="BonVino Bodegas", font=("Helvetica", 20), background="")
#         self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=20, width=60, font=("Helvetica", 12))
#         self.etiqueta_resultado = ttk.Label(self.root, text="")

#         self.btn_conf_click = ttk.BooleanVar(value=False)
#         self.btn_imp_click = ttk.BooleanVar(value=False)




import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from gestor import GestorActualizarVinos
from datetime import date

class PantallaActualizacionVinos:
    def _init_(self, gestor):
        self.root = None
        self.label = None
        self.listbox = None
        self.etiqueta_resultado = None
        self.bodegas_seleccionadas = []
        self.btn_confirmar = None
        self.btn_volver = None
        self.btn_cerrar = None
        self.gestor = gestor

    def cerrar_ventana(self):
        self.btn_conf_click.set(True)
        self.btn_imp_click.set(True)
        self.root.destroy()

    def opImportarActualizacionVinoBodegas(self):
        if self.listbox is not None:
            # Ocultar el Treeview si está visible
            if hasattr(self, 'treeview'):
                self.treeview.pack_forget()  # Ocultar el Treeview
            
            # Configurar el título y la interfaz
            self.label.config(text='BonVino Bodegas')
            self.label.pack(pady=20, fill=tk.X)

            # Ocultar todos los widgets anteriores
            self.listbox.delete(0, tk.END)
            for widget in [self.btn_volver, self.btn_cerrar, self.btn_confirmar, self.etiqueta_resultado, self.listbox]:
                if widget:
                    widget.pack_forget()

            # Mostrar el botón "Importar Actualizaciones" solo en la pantalla inicial
            if not hasattr(self, 'btn_importar'):
                self.btn_importar = tk.Button(
                    self.root,
                    text='Importar Actualizaciones',
                    font=("Helvetica", 12, "bold"),
                    bg="#4CAF50", fg="white",
                    command=lambda: self.gestor.nuevaActualizacionVino(self, self.btn_imp_click)
                )
            self.btn_importar.pack(pady=15)

            # Esperar a que se haga clic en el botón importar
            self.root.wait_variable(self.btn_imp_click)

            # Al confirmar la importación, ocultar el botón "Importar Actualizaciones"
            self.btn_importar.pack_forget()

            return self.bodegas_seleccionadas if self.btn_conf_click.get() else False

    def mostrarBodegasActDisponibles(self, arregloBodegasDisp):
        if self.listbox:
            self.btn_imp_click.set(True)
            self.label.config(text='Seleccione las bodegas')
            self.label.pack(pady=10, fill=tk.X)
            
            # Ocultar el botón "Importar Actualizaciones" si existe
            if hasattr(self, 'btn_importar'):
                self.btn_importar.pack_forget()
            
            self.listbox.delete(0, tk.END)
            self.listbox.pack(pady=5, fill=tk.X)

            if not arregloBodegasDisp:
                self.label.config(text='NO HAY BODEGAS PARA ACTUALIZAR')
                self.btn_cerrar = tk.Button(
                    self.root, 
                    text="Cerrar", 
                    command=self.cerrar_ventana, 
                    font=("Helvetica", 12, "bold"), 
                    bg="#e74c3c", fg="white"
                )
                self.btn_cerrar.pack(pady=20)
            else:
                for tupla in arregloBodegasDisp:
                    self.listbox.insert(tk.END, tupla[0])
                if not self.btn_confirmar:
                    self.btn_confirmar = tk.Button(
                        self.root, 
                        text="Confirmar selección", 
                        font=("Helvetica", 12, "bold"), 
                        bg="#3498db", fg="white",
                        command=lambda: self.tomarSeleccionBodega(arregloBodegasDisp)
                    )
                self.btn_confirmar.pack(pady=10)
            
            # Esperar la confirmación del usuario
            self.root.wait_variable(self.btn_conf_click)

    def tomarSeleccionBodega(self, arregloBodegasDisp):
        if self.listbox:
            self.btn_conf_click.set(True)
            self.etiqueta_resultado.pack(pady=5, fill=tk.X)
            seleccion = self.listbox.curselection()
            self.bodegas_seleccionadas = [arregloBodegasDisp[i] for i in seleccion if i < len(arregloBodegasDisp)]
            if self.bodegas_seleccionadas:
                self.btn_confirmar.pack_forget()

    def mostrarResumenActualizacion(self, arreglobodegaActualizadas):
        if self.listbox:
            self.listbox.pack_forget()  # Ocultamos el listbox
            self.etiqueta_resultado.pack_forget()
            self.label.config(text='Bodegas Actualizadas')
            self.label.pack(pady=10, fill=tk.X)
            
            # Configurar Treeview con las columnas correctas para los datos de Vino
            if not hasattr(self, 'treeview'):
                self.treeview = ttk.Treeview(
                    self.root,
                    columns=("Bodega", "Nombre Vino", "Nota de Cata", "Añada", "Precio", "Varietales", "Maridajes", "Fecha de Actualización"),
                    show='headings'
                )
                self.treeview.heading("Bodega", text="Bodega")
                self.treeview.heading("Nombre Vino", text="Nombre Vino")
                self.treeview.heading("Nota de Cata", text="Nota de Cata")
                self.treeview.heading("Añada", text="Añada")
                self.treeview.heading("Precio", text="Precio")
                self.treeview.heading("Varietales", text="Varietales")
                self.treeview.heading("Maridajes", text="Maridajes")
                self.treeview.heading("Fecha de Actualización", text="Fecha de Actualización")

                # Configurar tamaños de columnas y alineación
                self.treeview.column("Bodega", width=200, anchor='w')
                self.treeview.column("Nombre Vino", width=200, anchor='w')
                self.treeview.column("Nota de Cata", width=150, anchor='w')
                self.treeview.column("Añada", width=80, anchor='center')
                self.treeview.column("Precio", width=100, anchor='center')
                self.treeview.column("Varietales", width=150, anchor='w')
                self.treeview.column("Maridajes", width=150, anchor='w')
                self.treeview.column("Fecha de Actualización", width=150, anchor='center')
            
            # Limpiar Treeview antes de agregar nuevos datos
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            if not arreglobodegaActualizadas:
                self.etiqueta_resultado.config(text='NO SE SELECCIONARON BODEGAS', font=("Helvetica", 14))
                self.etiqueta_resultado.pack(pady=20, fill=tk.X)
            else:
                for bodega in arreglobodegaActualizadas:
                    # Insertar una fila para el nombre de la bodega
                    self.treeview.insert("", "end", values=(f'--- {bodega.nombre} ---', "", "", "", "", "", ""), tags=('bodega',))

                    # Agregar filas para cada vino de la bodega actualizado hoy
                    for vino in bodega.vinos:
                        if vino.fechaAct == date.today():
                            self.treeview.insert(
                                "",
                                "end",
                                values=(
                                    "",  # Columna Bodega en blanco para vinos
                                    vino.nombre,  # Nombre del vino
                                    vino.notaCataVino,  # Nota de cata del vino
                                    vino.añada,  # Añada del vino
                                    f"${vino.precio:.2f}",  # Precio del vino
                                    vino.varietales,  # Varietales del vino
                                    vino.maridajes,  # Maridajes del vino
                                    vino.fechaAct.strftime("%d/%m/%Y")  # Fecha de actualización
                                ),
                                tags=('vino',)
                            )

                    # Insertar una fila divisoria más larga después de cada bodega
                    self.treeview.insert("", "end", values=("-------------------------------------------------------------", "", "", "", "", "", ""), tags=('divider',))
                
            # Configurar los estilos de las filas
            self.treeview.tag_configure('bodega', background="#f0f0f0", font=("Helvetica", 12, "bold"))
            self.treeview.tag_configure('vino', background="#ffffff", font=("Helvetica", 12))
            self.treeview.tag_configure('divider', background="#f0f0f0", font=("Helvetica", 12, "italic"))
            
            self.treeview.pack(pady=5, fill=tk.BOTH, expand=True)

            # Botones Volver y Cerrar
            if not self.btn_volver:
                self.btn_volver = tk.Button(
                    self.root, 
                    text='Volver', 
                    command=self.opImportarActualizacionVinoBodegas, 
                    font=("Helvetica", 12, "bold"), 
                    bg="#3498db", fg="white"
                )
            self.btn_volver.pack(pady=10)

            if not self.btn_cerrar:
                self.btn_cerrar = tk.Button(
                    self.root, 
                    text="Cerrar", 
                    command=self.cerrar_ventana, 
                    font=("Helvetica", 12, "bold"), 
                    bg="#e74c3c", fg="white"
                )
            self.btn_cerrar.pack(pady=10)

            
    def cargar_imagen_de_fondo(self, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)
        self.background_label = tk.Label(self.root, image=foto)
        self.background_label.image = foto
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def habilitar_ventana(self):
        self.root = tk.Tk()
        self.root.title("Actualización de Bodegas")
        self.root.geometry("800x600")
        self.root.state('zoomed')
        self.root.configure(bg='#f5f5f5')
        self.cargar_imagen_de_fondo("./img/bonvino.jpg")

        self.label = tk.Label(self.root, text="BonVino Bodegas", font=("Helvetica", 24, "bold"), bg='#f5f5f5', fg='#333333')
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=20, width=60, font=("Helvetica", 12))
        self.etiqueta_resultado = tk.Label(self.root, text="", bg='#f5f5f5', fg='#333333')
        self.btn_conf_click = tk.BooleanVar(value=False)
        self.btn_imp_click = tk.BooleanVar(value=False)

        self.label.pack(pady=20, fill=tk.X)