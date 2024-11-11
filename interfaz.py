

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




#----------------------------------- cambios chas ----------------------

"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from gestor import GestorActualizarVinos
from datetime import *

class PantallaPrincipal:
    def __init__(self, gestor):
        self.gestor = gestor
        self.root = ttk.Window(themename="superhero")
        self.root.title("Sistema BonVino")
        self.root.geometry("800x600")
        self.root.eval('tk::PlaceWindow . center')  # Centrar ventana

        # Cargar la imagen de fondo solo una vez
        self.imagen_fondo = Image.open("./img/foto_vino_prueba.jpg")
        self.imagen_fondo = self.imagen_fondo.resize((800, 600), Image.Resampling.LANCZOS)
        self.img_tk_fondo = ImageTk.PhotoImage(self.imagen_fondo)

        # Etiqueta para la imagen de fondo (visible solo en inicio)
        self.label_fondo = ttk.Label(self.root, image=self.img_tk_fondo)
        self.label_fondo.place(relwidth=1, relheight=1)

        
        # Contenedor para el contenido inicial
        self.contenedor_inicio = ttk.Frame(self.root, relief="solid")
        self.contenedor_inicio.place(relwidth=1, relheight=1)

        # Botón para abrir la ventana de bodegas
        self.btn_visualizar_bodegas = ttk.Button(
            self.contenedor_inicio, text="Visualizar Bodegas", bootstyle="primary", command=self.mostrar_bodegas
        )
        self.btn_visualizar_bodegas.place(relx=0.5, rely=0.5, anchor="center")  # Centrado en la ventana

        self.root.mainloop()

    def mostrar_bodegas(self):
        # Ocultar la imagen de fondo al cambiar de vista
        self.label_fondo.place_forget()

        # Limpiar el contenedor de inicio para mostrar la lista de bodegas
        for widget in self.contenedor_inicio.winfo_children():
            widget.destroy()

        # Lista de bodegas con selección múltiple
        self.listbox_bodegas = tk.Listbox(
            self.contenedor_inicio, font=("Helvetica", 12, "italic"), width=40, height=40, selectmode=tk.MULTIPLE, 
            bg="#f7f7f7", fg="#333333", selectbackground="#4CAF50", selectforeground="#FFFFFF"
        )
        self.listbox_bodegas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(20, 10))

        # Scrollbar para el listbox
        scrollbar_bodegas = ttk.Scrollbar(self.contenedor_inicio, orient=tk.VERTICAL, command=self.listbox_bodegas.yview)
        self.listbox_bodegas.config(yscrollcommand=scrollbar_bodegas.set)
        scrollbar_bodegas.pack(side=tk.LEFT, fill=tk.Y, pady=(20, 10))

        # Frame para los botones en la parte inferior
        btn_frame = ttk.Frame(self.contenedor_inicio)
        btn_frame.pack(pady=20, anchor='s')  # Fijar el frame en la parte inferior

        # Botón de importar actualizaciones
        self.btn_importar = ttk.Button(
            btn_frame, text="Importar Actualizaciones", bootstyle="success", command=self.importar_actualizaciones
        )
        self.btn_importar.grid(row=0, column=0, padx=5)
        
        # Botón de volver
        self.btn_volver_inicio = ttk.Button(
            btn_frame, text="Volver al inicio", bootstyle="secondary", command=self.volver_inicio
        )
        self.btn_volver_inicio.grid(row=0, column=1, padx=5)

        # Mostrar bodegas en el listbox
        bodegas_disponibles = self.gestor.buscarBodegasAActualizar()
        self.mostrar_bodegas_disponibles(bodegas_disponibles)

        # Habilitar el botón importar solo si hay selección
        self.listbox_bodegas.bind("<<ListboxSelect>>", self.habilitar_boton_importar)

    def mostrar_bodegas_disponibles(self, bodegas):
        self.listbox_bodegas.delete(0, tk.END)
        for bodega in bodegas:
            self.listbox_bodegas.insert(tk.END, bodega[0])

    def habilitar_boton_importar(self, event):
        if self.listbox_bodegas.curselection():
            self.btn_importar["state"] = tk.NORMAL
        else:
            self.btn_importar["state"] = tk.DISABLED

    def importar_actualizaciones(self):
        selecciones = self.listbox_bodegas.curselection()
        if not selecciones:
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos una bodega a actualizar")
            return
        
        bodegas_seleccionadas = [self.listbox_bodegas.get(i) for i in selecciones]
        self.mostrar_ventana_vinos(bodegas_seleccionadas)

    def mostrar_ventana_vinos(self, bodegas_seleccionadas):
        # Limpiar el contenedor de inicio sin eliminar el fondo
        for widget in self.contenedor_inicio.winfo_children():
            widget.destroy()

        frame_vinos = ttk.Frame(self.contenedor_inicio)
        frame_vinos.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
        frame_vinos.pack_propagate(False)  # Evitar que cambie el tamaño del frame

        # Scrollbar para el frame de vinos en caso de que haya demasiados vinos
        canvas_vinos = tk.Canvas(frame_vinos)
        canvas_vinos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_vinos = ttk.Scrollbar(frame_vinos, orient=tk.VERTICAL, command=canvas_vinos.yview)
        scrollbar_vinos.pack(side=tk.RIGHT, fill=tk.Y)

        canvas_vinos.configure(yscrollcommand=scrollbar_vinos.set)
        canvas_vinos.bind("<Configure>", lambda e: canvas_vinos.configure(scrollregion=canvas_vinos.bbox("all")))

        vinos_frame_in_canvas = ttk.Frame(canvas_vinos)
        canvas_vinos.create_window((0, 0), window=vinos_frame_in_canvas, anchor="nw")

        for bodega_nombre in bodegas_seleccionadas:
            bodega = next((b for b in self.gestor.arregloBodegasSistema if b.nombre == bodega_nombre), None)
            if bodega is None:
                continue

            # Título de cada bodega
            titulo_bodega = ttk.Label(vinos_frame_in_canvas, text=f"{bodega.nombre}", font=("Helvetica", 14, "bold"), foreground="#4CAF50")
            titulo_bodega.pack(pady=(10, 5))

            # Lista de vinos importados
            listbox_vinos = tk.Listbox(vinos_frame_in_canvas, font=("Helvetica", 12), width=207, height=10)
            listbox_vinos.pack(fill=tk.BOTH, padx=(10, 0), pady=(5, 10))

            vinos_importados = self.gestor.obtener_vinos_de_bodega(bodega)
            if not vinos_importados:
                listbox_vinos.insert(tk.END, "NO HAY VINOS A ACTUALIZAR")
            else:
                for vino in vinos_importados:
                    listbox_vinos.insert(tk.END, vino)

        # Botón "Volver a bodegas" en la vista de vinos
        btn_volver_bodegas = ttk.Button(self.contenedor_inicio, text="Volver a bodegas", bootstyle="secondary", command=self.mostrar_bodegas)
        btn_volver_bodegas.pack(side=tk.BOTTOM, pady=10)  # Siempre al final del contenedor, visible

    def volver_inicio(self):
        #Vuelve a la pantalla principal de inicio sin reiniciar el objeto
        # Limpiar widgets del contenedor de inicio y volver a mostrar la imagen de fondo
        for widget in self.contenedor_inicio.winfo_children():
            widget.destroy()

        self.label_fondo.place(relwidth=1, relheight=1)  # Volver a mostrar la imagen de fondo

        # Reutilizar el contenedor para el botón inicial
        self.btn_visualizar_bodegas = ttk.Button(
            self.contenedor_inicio, text="Visualizar Bodegas", bootstyle="primary", command=self.mostrar_bodegas
        )
        self.btn_visualizar_bodegas.place(relx=0.5, rely=0.5, anchor="center")  # Centrado
"""