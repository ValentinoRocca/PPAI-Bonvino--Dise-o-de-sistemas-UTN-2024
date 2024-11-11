from clases.Bodega import *
from datetime import date
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *



#DEFINICION TIPOS DE UVA

uva1 = TipoUva("Uva tinta de origen francés, adaptada perfectamente en Argentina.", "Malbec")
uva2 = TipoUva("Uva tinta de origen francés, conocida por sus taninos fuertes.", "Cabernet Sauvignon")
uva3 = TipoUva("Uva blanca de origen francés, popular en todo el mundo.", "Chardonnay")
uva4 = TipoUva("Uva tinta de origen francés, conocida por su suavidad y elegancia.", "Merlot")
uva5 = TipoUva("Uva tinta originaria del valle del Ródano, en Francia.", "Syrah")
uva6 = TipoUva("Uva tinta de origen francés, famosa por su delicadeza.", "Pinot Noir")
uva7 = TipoUva("Uva blanca de origen francés, conocida por su frescura y acidez.", "Sauvignon Blanc")
uva8 = TipoUva("Uva blanca considerada la uva insignia de Argentina.", "Torrontés")
uva9 = TipoUva("Uva tinta de origen español, conocida por su versatilidad.", "Tempranillo")
uva10 = TipoUva("Uva tinta de origen italiano, ampliamente cultivada en Argentina.", "Bonarda")

uvasSistemas = [uva1,uva2,uva3,uva4,uva5,uva6,uva7,uva8,uva9,uva10]

# Definición de maridajes
maridaje1 = Maridaje("Excelente combinación con carnes rojas asadas.", "Carne Asada")
maridaje2 = Maridaje("Perfecto con platos de caza y guisos.", "Caza")
maridaje3 = Maridaje("Ideal para acompañar pastas con salsas de tomate.", "Pasta con Salsa de Tomate")
maridaje4 = Maridaje("Combina muy bien con quesos duros.", "Queso Duro")
maridaje5 = Maridaje("Marida con ensaladas frescas y pescados.", "Ensalada y Pescado")
maridaje6 = Maridaje("Perfecto para mariscos y platos ligeros.", "Mariscos")
maridaje7 = Maridaje("Ideal para acompañar postres dulces.", "Postres")
maridaje8 = Maridaje("Excelente con comidas picantes.", "Comida Picante")
maridaje9 = Maridaje("Combina bien con aves y cordero.", "Aves y Cordero")
maridaje10 = Maridaje("Perfecto para acompañar sushi.", "Sushi")
maridaje11 = Maridaje("Ideal con hamburguesas gourmet.", "Hamburguesa Gourmet")
maridaje12 = Maridaje("Combina bien con platos vegetarianos.", "Platos Vegetarianos")
maridaje13 = Maridaje("Excelente con risottos.", "Risotto")
maridaje14 = Maridaje("Marida con platos mediterráneos.", "Platos Mediterráneos")
maridaje15 = Maridaje("Perfecto para pizzas artesanales.", "Pizza")
maridaje16 = Maridaje("Ideal con frutos secos y quesos suaves.", "Frutos Secos y Queso Suave")


##BodegasDelASistema

#BODEGA 1 "CATENA ZAPATA"
bodega1 = Bodega(
    coordenadaUbicacion=(-32.89084, -68.845),
    descripcion="Una de las bodegas más prestigiosas de Argentina, conocida por sus Malbecs de alta gama.",
    historia="Fundada en 1902 por Nicola Catena, es una de las bodegas más antiguas de Mendoza.",
    nombre="Bodega Catena Zapata",
    periodoActualizacion=6,  # En meses
    ultimaActualizacion=date(2024, 1, 1)
)

#VINOS DE BODEGA 1
# Vinos para Bodega Catena Zapata
vino1_catena = Vino("Catena Alta Malbec", "catena_alta_malbec.jpg", "Notas de ciruela, higos y un toque de especias.", 1500, 2018, date(2024, 1, 1))
vino2_catena = Vino("Catena Zapata Adrianna Vineyard", "catena_adrianna_vineyard.jpg", "Aromas de violetas y frutos negros con un final largo.", 3500, 2016, date(2024, 1, 1))
vino3_catena = Vino("Catena Chardonnay", "catena_chardonnay.jpg", "Fresco, con notas cítricas y un toque de vainilla.", 1200, 2019, date(2024, 1, 1))
vino4_catena = Vino("Catena Malbec", "catena_malbec.jpg", "Frutal y especiado con taninos suaves.", 25000, 2020, date(2024, 1, 1))

#VARIETALES VINO CATENA ZAPATA
vino1_catena.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1)) #hechoenApi
vino2_catena.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1)) #hechoenApi
vino2_catena.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2)) #hechoenApi
vino3_catena.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3)) #hechoenApi
vino4_catena.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))

#MARIDAJES BODEGA 1
vino1_catena.agregarMaridaje(maridaje1)
vino1_catena.agregarMaridaje(maridaje4)
vino2_catena.agregarMaridaje(maridaje2)
vino2_catena.agregarMaridaje(maridaje9)
vino3_catena.agregarMaridaje(maridaje5)
vino3_catena.agregarMaridaje(maridaje6)
vino4_catena.agregarMaridaje(maridaje1)
vino4_catena.agregarMaridaje(maridaje8)


# Agregando vinos a la bodega
bodega1.agregar_vino(vino1_catena)
bodega1.agregar_vino(vino2_catena)
bodega1.agregar_vino(vino3_catena)
bodega1.agregar_vino(vino4_catena)

#vinos API Bodega catena
vinoAPI1_catena = ["Catena Alta Malbec", "catena_alta_malbec.jpg", "Notas de ciruela higos y un toque de especias.",9999999,1800,["Carne Asada"], [["Vino 100% Malbec", 100, "Malbec"]],date(2024, 3, 25)]
vinoAPI2_catena = ["Catena Zapata Adrianna Vineyard", "catena_adrianna_vineyard.jpg", "Aromas de violetas y frutos negros con un final largo.", 3500, 2016,["Caza","Mariscos"], [["Blend de Malbec y Cabernet Sauvignon", 80, "Malbec"],["Blend de Malbec y Cabernet Sauvignon", 20, "Cabernet Sauvignon"]], date(2024, 4, 25)]
vinoAPI3_catena = ["Catena Chardonnay", "catena_chardonnay.jpg", "Fresco, con notas cítricas y un toque de vainilla.", 1200, 2019,["Ensalada y Pescado", "Mariscos","Carne Asada"], [["Vino 100% Chardonnay", 100, "Chardonnay"]], date(2024, 4, 25)]
vinoAPI4_catena = ["Catena Malbec", "catena_malbec.jpg", "Frutal y especiado con taninos suaves.", 1100, 2020, ["Comida Picante"],[["Vino 100% Malbec", 100, "Malbec"]],date(2024, 4, 25)]
vinosApiCatena = [vinoAPI1_catena,vinoAPI2_catena,vinoAPI3_catena,vinoAPI4_catena]

bodega1.agregarVinosApi(vinosApiCatena) 
#---------------------------------------------------------bodega 2--------------------------------------#
bodega2 = Bodega(
    coordenadaUbicacion=(-32.9312, -68.7885),
    descripcion="Bodega con una larga tradición en la elaboración de vinos de calidad, ubicada en Luján de Cuyo.",
    historia="Desde su fundación en 1895, ha sido pionera en la viticultura argentina.",
    nombre="Bodega Norton",
    periodoActualizacion=2,
    ultimaActualizacion=date(2024, 2, 1)
)
#vinos bodega 2 norton
# Vinos para Bodega Norton
vino1_norton = Vino("Norton Malbec", "norton_malbec.jpg", "Aromas de frutas rojas maduras y especias.", 800, 2020, date(2024, 2, 1))
vino2_norton = Vino("Norton Reserva Cabernet Sauvignon", "norton_reserva_cabernet.jpg", "Complejo con notas de pimiento y frutos negros.", 950, 2018, date(2024, 2, 1))
vino3_norton = Vino("Norton Chardonnay", "norton_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 700, 2019, date(2024, 2, 1))
vino4_norton = Vino("Norton Reserva Malbec", "norton_reserva_malbec.jpg", "Intenso y frutal con taninos suaves.", 1000, 2017, date(2024, 2, 1))

#varietales norton
vino1_norton.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_norton.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_norton.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_norton.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 90, uva1))
vino4_norton.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 10, uva2))

#maridajes norton
vino1_norton.agregarMaridaje(maridaje1)
vino1_norton.agregarMaridaje(maridaje11)
vino2_norton.agregarMaridaje(maridaje2)
vino2_norton.agregarMaridaje(maridaje14)
vino3_norton.agregarMaridaje(maridaje5)
vino3_norton.agregarMaridaje(maridaje15)
vino4_norton.agregarMaridaje(maridaje1)
vino4_norton.agregarMaridaje(maridaje9)

#agregarVinos
#bodega2.agregar_vino(vino1_norton)
#bodega2.agregar_vino(vino2_norton)
#bodega2.agregar_vino(vino3_norton)
#bodega2.agregar_vino(vino4_norton)

#API
vinoAPI1_norton = ["Norton Malbec", "norton_malbec.jpg", "Aromas de frutas rojas maduras y especias traidas de freldjord.", 800, 2020,["Carne Asada","Hamburguesa Gourmet"],[["Vino 100% Malbec", 100, "Malbec"]], date(2024, 2, 1)]
vinoAPI2_norton = ["Norton Reserva Cabernet Sauvignon", "norton_reserva_cabernet.jpg", "Complejo con notas de pimiento y frutos negros.", 950, 2018,["Caza","Platos Mediterráneos"], [["Vino 100% Cabernet Sauvignon", 100, "Cabernet Sauvignon"]], date(2024, 2, 1)]
vinoAPI3_norton = ["Norton Chardonnay", "norton_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 700, 2019,["Ensalada y Pescado","Pizza"],[["Vino 100% Chardonnay", 100, "Chardonnay"]], date(2024, 2, 1)]
vinoAPI4_norton = ["Norton Reserva Malbec", "norton_reserva_malbec.jpg", "Intenso y frutal con taninos suaves.", 1000, 2017,["Carne Asada","Aves y Cordero"], [["Blend de Malbec y Cabernet Sauvignon", 90, "Malbec"],["Blend de Malbec y Cabernet Sauvignon", 10, "Cabernet Sauvignon"]],date(2024, 2, 1)]
vinoAPI5_norton = ["Norton Uncle Grandpa", "norton_reserva_cn.jpg", "Frescura alimonada con sason conquistador.", 2600, 2014,["Pizza"], [["Blend de Malbec y Cabernet Sauvignon", 50, "Malbec"],["Blend de Malbec y Cabernet Sauvignon", 50, "Cabernet Sauvignon"]],date(2024, 4, 3)]
vinoAPI6_norton = ["Norton KFPanda", "norton_reserva_poo.jpg", "Notas de dumplings con arroz y fideos chinos.", 3560, 2012,["Aves y Cordero", "Ensalada y Pescado" ], [["Vino 100% Bonarda", 100, "Bonarda"]],date(2024, 4, 3)]

vinosApiNorton = [vinoAPI1_norton,vinoAPI2_norton,vinoAPI3_norton,vinoAPI4_norton,vinoAPI5_norton, vinoAPI6_norton]

bodega2.agregarVinosApi(vinosApiNorton)

#------------------------------------BODEGA 3----------------------#
bodega3 = Bodega(
    coordenadaUbicacion=(-33.0068, -68.8628),
    descripcion="Reconocida por sus vinos Malbec y Cabernet Sauvignon de alta calidad.",
    historia="Con una historia que data de 1884, esta bodega ha sido un pilar en la industria del vino argentino.",
    nombre="Bodega Trapiche",
    periodoActualizacion=3,
    ultimaActualizacion=date(2024, 1, 15)
)

# Vinos para Bodega Trapiche
vino1_trapiche = Vino("Trapiche Malbec", "trapiche_malbec.jpg", "Notas de frutas rojas y negras con un toque de especias.", 850, 2019, date(2024, 1, 15))
vino2_trapiche = Vino("Trapiche Reserva Cabernet Sauvignon", "trapiche_reserva_cabernet.jpg", "Aromas de frutos negros y especias.", 900, 2018, date(2024, 1, 15))
vino3_trapiche = Vino("Trapiche Chardonnay", "trapiche_chardonnay.jpg", "Fresco con notas cítricas y tropicales.", 750, 2020, date(2024, 1, 15))
vino4_trapiche = Vino("Trapiche Broquel Malbec", "trapiche_broquel_malbec.jpg", "Intenso con notas de ciruela y chocolate.", 950, 2017, date(2024, 1, 15))

#varietales
vino1_trapiche.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_trapiche.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_trapiche.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_trapiche.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 70, uva1))
vino4_trapiche.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 30, uva2))

#maridaje
vino1_trapiche.agregarMaridaje(maridaje1)
vino1_trapiche.agregarMaridaje(maridaje3)
vino2_trapiche.agregarMaridaje(maridaje2)
vino3_trapiche.agregarMaridaje(maridaje5)
vino3_trapiche.agregarMaridaje(maridaje6)
vino4_trapiche.agregarMaridaje(maridaje1)
vino4_trapiche.agregarMaridaje(maridaje4)

#agregarVinos

bodega3.agregar_vino(vino1_trapiche)
bodega3.agregar_vino(vino2_trapiche)
bodega3.agregar_vino(vino3_trapiche)
bodega3.agregar_vino(vino4_trapiche)

#api
vinoAPI1_trapiche = ["Trapiche Malbec", "trapiche_malbec.jpg", "Notas de frutas rojas y negras con un toque de especias.", 1850, 2019, ["Carne Asada","Pasta con Salsa de Tomate"],[["Vino 100% Malbec", 100, "Malbec"]],date(2024, 2, 3)]
vinoAPI2_trapiche = ["Trapiche Reserva Cabernet Sauvignon", "trapiche_reserva_cabernet.jpg", "Aromas de frutos negros y especias.", 900, 2018,["Caza"],[["Vino 100% Chardonnay", 100, "Chardonnay"]], date(2024, 3, 15)]
vinoAPI3_trapiche = ["Trapiche Chardonnay", "trapiche_chardonnay.jpg", "Fresco con notas cítricas y tropicales.", 2750, 2020, ["Ensalada y Pescado","Mariscos"],[["Vino 100% Cabernet Sauvignon", 100, "Cabernet Sauvignon"]],date(2024, 2, 28)]
vinoAPI4_trapiche = ["Trapiche Broquel Malbec", "trapiche_broquel_malbec.jpg", "Intenso con notas de ciruela y chocolate.", 15000, 2017,["Carne Asada"] ,[["Blend de Malbec y Cabernet Sauvignon", 70, "Malbec"], ["Blend de Malbec y Cabernet Sauvignon", 30, "Cabernet Sauvignon"]],date(2024, 1, 15)]
vinosApiTrapiche = [vinoAPI1_trapiche,vinoAPI2_trapiche,vinoAPI3_trapiche,vinoAPI4_trapiche]

bodega3.agregarVinosApi(vinosApiTrapiche)

#--------------------------bodega 4--------------------#

bodega4 = Bodega(
    coordenadaUbicacion=(-33.0244, -68.7845),
    descripcion="Especializada en la producción de vinos de alta gama, con un enfoque en terroir y sostenibilidad.",
    historia="Establecida en 1997, ha ganado numerosos premios internacionales.",
    nombre="Bodega Luigi Bosca",
    periodoActualizacion=2,
    ultimaActualizacion=date(2024, 2, 11)
)

#vinos

vino1_luigi = Vino("Luigi Bosca Malbec", "luigi_bosca_malbec.jpg", "Aromas de frutas rojas maduras y especias.", 1400, 2019, date(2024, 1, 30))
vino2_luigi = Vino("Luigi Bosca Cabernet Sauvignon", "luigi_bosca_cabernet.jpg", "Notas de frutos negros y pimientos.", 1500, 2018, date(2024, 1, 30))
vino3_luigi = Vino("Luigi Bosca Chardonnay", "luigi_bosca_chardonnay.jpg", "Fresco y equilibrado con un toque de vainilla.", 1300, 2020, date(2024, 1, 30))
vino4_luigi = Vino("Luigi Bosca Syrah", "luigi_bosca_syrah.jpg", "Intenso y especiado con taninos suaves.", 1600, 2017, date(2024, 1, 30))

#varietales
vino1_luigi.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_luigi.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_luigi.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_luigi.agregarVarietal(Varietal("Vino 100% Syrah", 100, uva5))

#maridajes

vino1_luigi.agregarMaridaje(maridaje1)
vino1_luigi.agregarMaridaje(maridaje9)
vino2_luigi.agregarMaridaje(maridaje2)
vino2_luigi.agregarMaridaje(maridaje14)
vino3_luigi.agregarMaridaje(maridaje5)
vino3_luigi.agregarMaridaje(maridaje6)
vino4_luigi.agregarMaridaje(maridaje1)
vino4_luigi.agregarMaridaje(maridaje8)

bodega4.agregar_vino(vino1_luigi)
bodega4.agregar_vino(vino2_luigi)
bodega4.agregar_vino(vino3_luigi)
bodega4.agregar_vino(vino4_luigi)

#api

vinoAPI1_luigi = ["Luigi Bosca Malbec", "luigi_bosca_malbec.jpg", "Aromas de frutas rojas maduras y especias.", 2500, 2019,["Carne Asada", "Aves y Cordero", "Ensalada y Pescado"], [["Vino 100% Malbec", 100, "Malbec"]], date(2024, 1, 30)]
vinoAPI2_luigi = ["Luigi Bosca Cabernet Sauvignon", "luigi_bosca_cabernet.jpg", "Notas de frutos negros y pimientos.", 1500, 2018, ["Caza","Queso Duro"] ,[["Vino 100% Cabernet Sauvignon", 100, "Cabernet Sauvignon"]],date(2024, 1, 30)]
vinoAPI3_luigi = ["Luigi Bosca Chardonnay", "luigi_bosca_chardonnay.jpg", "Fresco y equilibrado con un toque de vainilla.", 3500, 2020,["Ensalada y Pescado","Mariscos"] ,[["Vino 100% Chardonnay", 100, "Chardonnay"]],date(2024, 1, 30)]
vinoAPI4_luigi = ["Luigi Bosca Syrah", "luigi_bosca_syrah.jpg", "Intenso y especiado con taninos suaves.", 1600, 2017,["Carne Asada","Comida Picante"],[["Vino 100% Syrah", 100, "Syrah"]] ,date(2024, 1, 30)]
vinoAPI5_luigi = ["Luigi Bosca Intensidad", "luigi_bosca_FAKER.jpg", "Aromas cautivadores de frutos rojos maduros, notas de vainilla y sutiles toques de cacao..", 5200, 2013,["Mariscos"],[["Vino 100% Syrah", 100, "Syrah"]] ,date(2024, 4, 25)]

vinosApiLuigi = [vinoAPI1_luigi,vinoAPI2_luigi,vinoAPI3_luigi,vinoAPI4_luigi,vinoAPI5_luigi]
bodega4.agregarVinosApi(vinosApiLuigi)


#------------------------------------------------------------------BODEGA 5--------------------------------------------------------------------#
bodega5 = Bodega(
    coordenadaUbicacion=(-32.9295, -68.8018),
    descripcion="Una bodega boutique que produce vinos artesanales en pequeñas cantidades.",
    historia="Desde 1999, ha sido reconocida por su enfoque en la calidad y la atención al detalle.",
    nombre="Bodega Achaval Ferrer",
    periodoActualizacion=4,
    ultimaActualizacion=date(2024, 2, 27)
)

vino1_achaval = Vino("Achaval Ferrer Malbec", "achaval_ferrer_malbec.jpg", "Notas de frutos rojos y negros con un toque de roble.", 2000, 2018, date(2024, 2, 5))
vino2_achaval = Vino("Achaval Ferrer Quimera", "achaval_ferrer_quimera.jpg", "Complejo con notas de frutas negras y especias.", 2500, 2017, date(2024, 2, 5))
vino3_achaval = Vino("Achaval Ferrer Finca Bella Vista", "achaval_ferrer_bella_vista.jpg", "Intenso y elegante con notas de ciruela y chocolate.", 3000, 2016, date(2024, 2, 5))
vino4_achaval = Vino("Achaval Ferrer Cabernet Franc", "achaval_ferrer_cabernet_franc.jpg", "Aromas de pimiento y frutos negros.", 2200, 2018, date(2024, 2, 5))


#varietales
vino1_achaval.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1))
vino2_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2))
vino3_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 90, uva1))
vino3_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 10, uva2))
vino4_achaval.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))

#maridajes
vino1_achaval.agregarMaridaje(maridaje1)
vino2_achaval.agregarMaridaje(maridaje2)
vino2_achaval.agregarMaridaje(maridaje9)
vino3_achaval.agregarMaridaje(maridaje1)
vino3_achaval.agregarMaridaje(maridaje3)
vino4_achaval.agregarMaridaje(maridaje1)
vino4_achaval.agregarMaridaje(maridaje2)

bodega5.agregar_vino(vino1_achaval)
bodega5.agregar_vino(vino2_achaval)
bodega5.agregar_vino(vino3_achaval)
bodega5.agregar_vino(vino4_achaval)

#api
vinoAPI1_achaval = ["Achaval Ferrer Malbec", "achaval_ferrer_malbec.jpg", "Notas de frutos rojos y negros con un toque de roble.", 2000, 2018,["Carne Asada"], [["Vino 100% Malbec", 100, "Malbec"]], date(2024, 2, 5)]

vinoAPI2_achaval = ["Achaval Ferrer Quimera", "achaval_ferrer_quimera.jpg", "Complejo con notas de frutas negras y especias.", 2500, 2017,["Caza","Aves y Cordero"],[["Blend de Malbec y Cabernet Sauvignon", 80, "Malbec"],["Blend de Malbec y Cabernet Sauvignon", 20, "Cabernet Sauvignon"]], date(2024, 2, 5)]

vinoAPI3_achaval = ["Achaval Ferrer Finca Bella Vista", "achaval_ferrer_bella_vista.jpg", "Intenso y elegante con notas de ciruela y chocolate.", 3000, 2016,["Carne Asada","Pasta con Salsa de Tomate" ],[["Blend de Malbec y Cabernet Sauvignon", 90, "Malbec"],["Blend de Malbec y Cabernet Sauvignon", 10, "Cabernet Sauvignon"]], date(2024, 2, 5)]

vinoAPI4_achaval = ["Achaval Ferrer Cabernet Franc", "achaval_ferrer_cabernet_franc.jpg", "Aromas de pimiento y frutos negros.", 9000, 2018,["Carne Asada", "Caza" ],[["Vino 100% Cabernet Sauvignon", 100, "Cabernet Sauvignon"]], date(2024, 3, 15)]
vinoAPI5_achaval = ["Achaval Ferrer Finca Altamira Malbec", "achaval_ferrer _finca_Altamira.jpg", "Intensos aromas a frutas negras maduras como ciruelas y moras.", 9999, 2010,["Sushi", "Risotto" ],[["Vino 100% Merlot", 100, "Merlot"]], date(2024, 3, 15)]
vinoAPI6_achaval = ["Achaval Ferrer Al que madruga Dios Lo Ayuda", "achaval_ferrer _diosAyuda.jpg", "Aromas a frutos oscuros y especias, que invitan a explorar cada sorbo con expectación", 3500, 2010,["Postres"],[["Vino 100% Tempranillo", 100, "Tempranillo"]], date(2024, 4, 20)]

vinosApiAchaval = [vinoAPI1_achaval,vinoAPI2_achaval,vinoAPI3_achaval,vinoAPI4_achaval,vinoAPI5_achaval,vinoAPI6_achaval]

bodega5.agregarVinosApi(vinosApiAchaval)

#_----------------------------------------------------------------------------------------------------------------------------------------------------------


# bodegas del sistema_: 
bodegasSistema = [bodega1, bodega2, bodega3, bodega4, bodega5]

maridajesSistema=[maridaje1, maridaje2, maridaje3,maridaje4, maridaje5, maridaje6, maridaje7,maridaje8, maridaje9,maridaje10, maridaje11,maridaje12,maridaje13,maridaje14,maridaje15,maridaje16]

