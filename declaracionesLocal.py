from clases.Maridaje import *
from clases.ClaseBodega import *
import datetime
from clases.Maridaje import *
from clases.TipoUva import *
from clases.Varietal import *


##BodegasDelASistema


bodega1 = Bodega(
    coordenadaUbicacion=(-32.89084, -68.845),
    descripcion="Una de las bodegas más prestigiosas de Argentina, conocida por sus Malbecs de alta gama.",
    historia="Fundada en 1902 por Nicola Catena, es una de las bodegas más antiguas de Mendoza.",
    nombre="Bodega Catena Zapata",
    periodoActualizacion=2,  # En meses
    ultimaActualizacion=datetime.datetime(2024, 1, 1)
)

bodega2 = Bodega(
    coordenadaUbicacion=(-32.9312, -68.7885),
    descripcion="Bodega con una larga tradición en la elaboración de vinos de calidad, ubicada en Luján de Cuyo.",
    historia="Desde su fundación en 1895, ha sido pionera en la viticultura argentina.",
    nombre="Bodega Norton",
    periodoActualizacion=3,
    ultimaActualizacion=datetime.datetime(2024, 2, 1)
)

bodega3 = Bodega(
    coordenadaUbicacion=(-33.0068, -68.8628),
    descripcion="Reconocida por sus vinos Malbec y Cabernet Sauvignon de alta calidad.",
    historia="Con una historia que data de 1884, esta bodega ha sido un pilar en la industria del vino argentino.",
    nombre="Bodega Trapiche",
    periodoActualizacion=1,
    ultimaActualizacion=datetime.datetime(2024, 1, 15)
)

bodega4 = Bodega(
    coordenadaUbicacion=(-33.0244, -68.7845),
    descripcion="Especializada en la producción de vinos de alta gama, con un enfoque en terroir y sostenibilidad.",
    historia="Establecida en 1997, ha ganado numerosos premios internacionales.",
    nombre="Bodega Luigi Bosca",
    periodoActualizacion=4,
    ultimaActualizacion=datetime.datetime(2024, 1, 27)
)

bodega5 = Bodega(
    coordenadaUbicacion=(-32.9295, -68.8018),
    descripcion="Una bodega boutique que produce vinos artesanales en pequeñas cantidades.",
    historia="Desde 1999, ha sido reconocida por su enfoque en la calidad y la atención al detalle.",
    nombre="Bodega Achaval Ferrer",
    periodoActualizacion=5,
    ultimaActualizacion=datetime.datetime(2024, 2, 27)
)

bodega6 = Bodega(
    coordenadaUbicacion=(-32.8228, -68.8593),
    descripcion="Conocida por sus Malbecs y su enfoque en la viticultura biodinámica.",
    historia="Fundada en 1998, ha sido pionera en prácticas agrícolas sostenibles.",
    nombre="Bodega Domaine Bousquet",
    periodoActualizacion=2,
    ultimaActualizacion=datetime.datetime(2024, 1, 20)
)

bodega7 = Bodega(
    coordenadaUbicacion=(-33.0385, -68.8449),
    descripcion="Una de las bodegas más grandes y reconocidas de Argentina, con una amplia gama de vinos.",
    historia="Con más de 100 años de historia, ha sido un líder en la industria vinícola argentina.",
    nombre="Bodega Navarro Correas",
    periodoActualizacion=3,
    ultimaActualizacion=datetime.datetime(2024, 1, 25)
)

bodega8 = Bodega(
    coordenadaUbicacion=(-32.9138, -68.8226),
    descripcion="Especializada en la producción de vinos espumosos y tranquilos de alta calidad.",
    historia="Desde 1959, ha sido conocida por su innovación y calidad constante.",
    nombre="Bodega Chandon Argentina",
    periodoActualizacion=1,
    ultimaActualizacion=datetime.datetime(2024, 1, 10)
)

bodega9 = Bodega(
    coordenadaUbicacion=(-32.9791, -68.7979),
    descripcion="Famosa por sus vinos de alta gama y su enfoque en la viticultura de precisión.",
    historia="Establecida en 1932, ha sido un referente en la producción de vinos premium.",
    nombre="Bodega Pulenta Estate",
    periodoActualizacion=4,
    ultimaActualizacion=datetime.datetime(2024, 1, 5)
)

bodega10 = Bodega(
    coordenadaUbicacion=(-32.9452, -68.8567),
    descripcion="Conocida por su excelencia en la producción de Malbec y otras variedades tintas.",
    historia="Desde su fundación en 1998, ha sido aclamada por la calidad de sus vinos.",
    nombre="Bodega Ruca Malen",
    periodoActualizacion=6,
    ultimaActualizacion=datetime.datetime(2024, 1, 18)
    )

#VinosDeBodegas

### Instancias de Vinos para Cada Bodega

# Vinos para Bodega Catena Zapata
vino1_catena = Vino("Catena Alta Malbec", "catena_alta_malbec.jpg", "Notas de ciruela, higos y un toque de especias.", 1500, 2018, datetime.datetime(2024, 1, 1))
vino2_catena = Vino("Catena Zapata Adrianna Vineyard", "catena_adrianna_vineyard.jpg", "Aromas de violetas y frutos negros con un final largo.", 3500, 2016, datetime.datetime(2024, 1, 1))
vino3_catena = Vino("Catena Chardonnay", "catena_chardonnay.jpg", "Fresco, con notas cítricas y un toque de vainilla.", 1200, 2019, datetime.datetime(2024, 1, 1))
vino4_catena = Vino("Catena Malbec", "catena_malbec.jpg", "Frutal y especiado con taninos suaves.", 1100, 2020, datetime.datetime(2024, 1, 1))

# Agregando vinos a la bodega
bodega1.agregar_vino(vino1_catena)
bodega1.agregar_vino(vino2_catena)
bodega1.agregar_vino(vino3_catena)
bodega1.agregar_vino(vino4_catena)

# Vinos para Bodega Norton
vino1_norton = Vino("Norton Malbec", "norton_malbec.jpg", "Aromas de frutas rojas maduras y especias.", 800, 2020, datetime.datetime(2024, 2, 1))
vino2_norton = Vino("Norton Reserva Cabernet Sauvignon", "norton_reserva_cabernet.jpg", "Complejo con notas de pimiento y frutos negros.", 950, 2018, datetime.datetime(2024, 2, 1))
vino3_norton = Vino("Norton Chardonnay", "norton_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 700, 2019, datetime.datetime(2024, 2, 1))
vino4_norton = Vino("Norton Reserva Malbec", "norton_reserva_malbec.jpg", "Intenso y frutal con taninos suaves.", 1000, 2017, datetime.datetime(2024, 2, 1))

bodega2.agregar_vino(vino1_norton)
bodega2.agregar_vino(vino2_norton)
bodega2.agregar_vino(vino3_norton)
bodega2.agregar_vino(vino4_norton)

# Vinos para Bodega Trapiche
vino1_trapiche = Vino("Trapiche Malbec", "trapiche_malbec.jpg", "Notas de frutas rojas y negras con un toque de especias.", 850, 2019, datetime.datetime(2024, 1, 15))
vino2_trapiche = Vino("Trapiche Reserva Cabernet Sauvignon", "trapiche_reserva_cabernet.jpg", "Aromas de frutos negros y especias.", 900, 2018, datetime.datetime(2024, 1, 15))
vino3_trapiche = Vino("Trapiche Chardonnay", "trapiche_chardonnay.jpg", "Fresco con notas cítricas y tropicales.", 750, 2020, datetime.datetime(2024, 1, 15))
vino4_trapiche = Vino("Trapiche Broquel Malbec", "trapiche_broquel_malbec.jpg", "Intenso con notas de ciruela y chocolate.", 950, 2017, datetime.datetime(2024, 1, 15))

bodega3.agregar_vino(vino1_trapiche)
bodega3.agregar_vino(vino2_trapiche)
bodega3.agregar_vino(vino3_trapiche)
bodega3.agregar_vino(vino4_trapiche)

# Vinos para Bodega Luigi Bosca
vino1_luigi = Vino("Luigi Bosca Malbec", "luigi_bosca_malbec.jpg", "Aromas de frutas rojas maduras y especias.", 1400, 2019, datetime.datetime(2024, 1, 30))
vino2_luigi = Vino("Luigi Bosca Cabernet Sauvignon", "luigi_bosca_cabernet.jpg", "Notas de frutos negros y pimientos.", 1500, 2018, datetime.datetime(2024, 1, 30))
vino3_luigi = Vino("Luigi Bosca Chardonnay", "luigi_bosca_chardonnay.jpg", "Fresco y equilibrado con un toque de vainilla.", 1300, 2020, datetime.datetime(2024, 1, 30))
vino4_luigi = Vino("Luigi Bosca Syrah", "luigi_bosca_syrah.jpg", "Intenso y especiado con taninos suaves.", 1600, 2017, datetime.datetime(2024, 1, 30))

bodega4.agregar_vino(vino1_luigi)
bodega4.agregar_vino(vino2_luigi)
bodega4.agregar_vino(vino3_luigi)
bodega4.agregar_vino(vino4_luigi)

# Vinos para Bodega Achaval Ferrer
vino1_achaval = Vino("Achaval Ferrer Malbec", "achaval_ferrer_malbec.jpg", "Notas de frutos rojos y negros con un toque de roble.", 2000, 2018, datetime.datetime(2024, 2, 5))
vino2_achaval = Vino("Achaval Ferrer Quimera", "achaval_ferrer_quimera.jpg", "Complejo con notas de frutas negras y especias.", 2500, 2017, datetime.datetime(2024, 2, 5))
vino3_achaval = Vino("Achaval Ferrer Finca Bella Vista", "achaval_ferrer_bella_vista.jpg", "Intenso y elegante con notas de ciruela y chocolate.", 3000, 2016, datetime.datetime(2024, 2, 5))
vino4_achaval = Vino("Achaval Ferrer Cabernet Franc", "achaval_ferrer_cabernet_franc.jpg", "Aromas de pimiento y frutos negros.", 2200, 2018, datetime.datetime(2024, 2, 5))

bodega5.agregar_vino(vino1_achaval)
bodega5.agregar_vino(vino2_achaval)
bodega5.agregar_vino(vino3_achaval)
bodega5.agregar_vino(vino4_achaval)

# Vinos para Bodega Domaine Bous


vino1_domaine = Vino("Domaine Bousquet Malbec", "domaine_bousquet_malbec.jpg", "Notas de frutas rojas y un toque de roble.", 900, 2019, datetime.datetime(2024, 1, 20))
vino2_domaine = Vino("Domaine Bousquet Reserve Cabernet Sauvignon", "domaine_bousquet_reserve_cabernet.jpg", "Aromas de frutos negros y especias.", 1100, 2018, datetime.datetime(2024, 1, 20))
vino3_domaine = Vino("Domaine Bousquet Chardonnay", "domaine_bousquet_chardonnay.jpg", "Fresco con notas cítricas y tropicales.", 850, 2020, datetime.datetime(2024, 1, 20))
vino4_domaine = Vino("Domaine Bousquet Gran Malbec", "domaine_bousquet_gran_malbec.jpg", "Intenso con notas de ciruela y chocolate.", 1300, 2017, datetime.datetime(2024, 1, 20))

bodega6.agregar_vino(vino1_domaine)
bodega6.agregar_vino(vino2_domaine)
bodega6.agregar_vino(vino3_domaine)
bodega6.agregar_vino(vino4_domaine)

# Vinos para Bodega Navarro Correas
vino1_navarro = Vino("Navarro Correas Malbec", "navarro_correas_malbec.jpg", "Aromas de frutas rojas y negras con un toque de especias.", 850, 2019, datetime.datetime(2024, 1, 25))
vino2_navarro = Vino("Navarro Correas Reserva Cabernet Sauvignon", "navarro_correas_reserva_cabernet.jpg", "Complejo con notas de pimiento y frutos negros.", 950, 2018, datetime.datetime(2024, 1, 25))
vino3_navarro = Vino("Navarro Correas Chardonnay", "navarro_correas_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 700, 2019, datetime.datetime(2024, 1, 25))
vino4_navarro = Vino("Navarro Correas Reserva Malbec", "navarro_correas_reserva_malbec.jpg", "Intenso y frutal con taninos suaves.", 1000, 2017, datetime.datetime(2024, 1, 25))

bodega7.agregar_vino(vino1_navarro)
bodega7.agregar_vino(vino2_navarro)
bodega7.agregar_vino(vino3_navarro)
bodega7.agregar_vino(vino4_navarro)

# Vinos para Bodega Chandon Argentina
vino1_chandon = Vino("Chandon Extra Brut", "chandon_extra_brut.jpg", "Fresco y burbujeante con notas cítricas.", 1200, 2020, datetime.datetime(2024, 1, 10))
vino2_chandon = Vino("Chandon Brut Nature", "chandon_brut_nature.jpg", "Elegante con notas de frutas y un toque de levadura.", 1400, 2019, datetime.datetime(2024, 1, 10))
vino3_chandon = Vino("Chandon Demi Sec", "chandon_demi_sec.jpg", "Dulce y afrutado con notas de miel y manzana.", 1100, 2020, datetime.datetime(2024, 1, 10))
vino4_chandon = Vino("Chandon Rosé", "chandon_rose.jpg", "Fresco y frutal con notas de frutos rojos.", 1300, 2019, datetime.datetime(2024, 1, 10))

bodega8.agregar_vino(vino1_chandon)
bodega8.agregar_vino(vino2_chandon)
bodega8.agregar_vino(vino3_chandon)
bodega8.agregar_vino(vino4_chandon)

# Vinos para Bodega Pulenta Estate
vino1_pulenta = Vino("Pulenta Estate Malbec", "pulenta_estate_malbec.jpg", "Notas de frutas rojas maduras y especias.", 1800, 2019, datetime.datetime(2024, 1, 5))
vino2_pulenta = Vino("Pulenta Estate Gran Cabernet Franc", "pulenta_gran_cabernet_franc.jpg", "Aromas de pimiento y frutos negros.", 2000, 2018, datetime.datetime(2024, 1, 5))
vino3_pulenta = Vino("Pulenta Estate Chardonnay", "pulenta_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 1500, 2020, datetime.datetime(2024, 1, 5))
vino4_pulenta = Vino("Pulenta Estate Gran Malbec", "pulenta_gran_malbec.jpg", "Intenso con notas de ciruela y chocolate.", 2200, 2017, datetime.datetime(2024, 1, 5))

bodega9.agregar_vino(vino1_pulenta)
bodega9.agregar_vino(vino2_pulenta)
bodega9.agregar_vino(vino3_pulenta)
bodega9.agregar_vino(vino4_pulenta)

# Vinos para Bodega Ruca Malen
vino1_ruca = Vino("Ruca Malen Malbec", "ruca_malen_malbec.jpg", "Aromas de frutas rojas y negras con un toque de especias.", 900, 2019, datetime.datetime(2024, 1, 18))
vino2_ruca = Vino("Ruca Malen Reserva Cabernet Sauvignon", "ruca_malen_reserva_cabernet.jpg", "Complejo con notas de pimiento y frutos negros.", 1100, 2018, datetime.datetime(2024, 1, 18))
vino3_ruca = Vino("Ruca Malen Chardonnay", "ruca_malen_chardonnay.jpg", "Fresco y equilibrado con notas cítricas.", 800, 2019, datetime.datetime(2024, 1, 18))
vino4_ruca = Vino("Ruca Malen Reserva Malbec", "ruca_malen_reserva_malbec.jpg", "Intenso y frutal con taninos suaves.", 1000, 2017, datetime.datetime(2024, 1, 18))

bodega10.agregar_vino(vino1_ruca)
bodega10.agregar_vino(vino2_ruca)
bodega10.agregar_vino(vino3_ruca)
bodega10.agregar_vino(vino4_ruca)


# bodegas del sistema_: 
bodegasSistema = [bodega1, bodega2, bodega3, bodega4, bodega5, bodega6, bodega7, bodega8, bodega9, bodega10]

for bodega in bodegasSistema:
    print("Bodega: ",bodega.nombre)
    bodega.mostrarVinos()
    print('-'*50)

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


# Creación de varietales y asignación a los vinos

# Bodega Catena Zapata
vino1_catena.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_catena.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1))
vino2_catena.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2))
vino3_catena.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_catena.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))

# Bodega Norton
vino1_norton.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_norton.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_norton.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_norton.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 90, uva1))
vino4_norton.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 10, uva2))

# Bodega Trapiche
vino1_trapiche.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_trapiche.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_trapiche.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_trapiche.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 70, uva1))
vino4_trapiche.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 30, uva2))

# Bodega Luigi Bosca
vino1_luigi.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_luigi.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_luigi.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_luigi.agregarVarietal(Varietal("Vino 100% Syrah", 100, uva5))

# Bodega Achaval Ferrer
vino1_achaval.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1))
vino2_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2))
vino3_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 90, uva1))
vino3_achaval.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 10, uva2))
vino4_achaval.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))

# Bodega Domaine Bousquet
vino1_domaine.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_domaine.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_domaine.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_domaine.agregarVarietal(Varietal("Blend de Malbec y Merlot", 90, uva1))
vino4_domaine.agregarVarietal(Varietal("Blend de Malbec y Merlot", 10, uva4))

# Bodega Navarro Correas
vino1_navarro.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_navarro.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_navarro.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_navarro.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1))
vino4_navarro.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2))

# Bodega Chandon Argentina
vino1_chandon.agregarVarietal(Varietal("Vino 100% Sauvignon Blanc", 100, uva7))
vino2_chandon.agregarVarietal(Varietal("Blend de Sauvignon Blanc y Chardonnay", 80, uva7))
vino2_chandon.agregarVarietal(Varietal("Blend de Sauvignon Blanc y Chardonnay", 20, uva3))
vino3_chandon.agregarVarietal(Varietal("Vino 100% Torrontés", 100, uva8))
vino4_chandon.agregarVarietal(Varietal("Vino 100% Pinot Noir", 100, uva6))

# Bodega Pulenta Estate
vino1_pulenta.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_pulenta.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_pulenta.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_pulenta.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 70, uva1))
vino4_pulenta.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 30, uva2))

# Bodega Ruca Malen
vino1_ruca.agregarVarietal(Varietal("Vino 100% Malbec", 100, uva1))
vino2_ruca.agregarVarietal(Varietal("Vino 100% Cabernet Sauvignon", 100, uva2))
vino3_ruca.agregarVarietal(Varietal("Vino 100% Chardonnay", 100, uva3))
vino4_ruca.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 80, uva1))
vino4_ruca.agregarVarietal(Varietal("Blend de Malbec y Cabernet Sauvignon", 20, uva2))


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

# Asignación de maridajes a los vinos

# Bodega Catena Zapata
vino1_catena.agregarMaridaje(maridaje1)
vino1_catena.agregarMaridaje(maridaje4)
vino2_catena.agregarMaridaje(maridaje2)
vino2_catena.agregarMaridaje(maridaje9)
vino3_catena.agregarMaridaje(maridaje5)
vino3_catena.agregarMaridaje(maridaje6)
vino4_catena.agregarMaridaje(maridaje1)
vino4_catena.agregarMaridaje(maridaje8)

# Bodega Norton
vino1_norton.agregarMaridaje(maridaje1)
vino1_norton.agregarMaridaje(maridaje11)
vino2_norton.agregarMaridaje(maridaje2)
vino2_norton.agregarMaridaje(maridaje14)
vino3_norton.agregarMaridaje(maridaje5)
vino3_norton.agregarMaridaje(maridaje15)
vino4_norton.agregarMaridaje(maridaje1)
vino4_norton.agregarMaridaje(maridaje9)

# Bodega Trapiche
vino1_trapiche.agregarMaridaje(maridaje1)
vino1_trapiche.agregarMaridaje(maridaje3)
vino2_trapiche.agregarMaridaje(maridaje2)
vino3_trapiche.agregarMaridaje(maridaje5)
vino3_trapiche.agregarMaridaje(maridaje6)
vino4_trapiche.agregarMaridaje(maridaje1)
vino4_trapiche.agregarMaridaje(maridaje4)

# Bodega Luigi Bosca
vino1_luigi.agregarMaridaje(maridaje1)
vino1_luigi.agregarMaridaje(maridaje9)
vino2_luigi.agregarMaridaje(maridaje2)
vino2_luigi.agregarMaridaje(maridaje14)
vino3_luigi.agregarMaridaje(maridaje5)
vino3_luigi.agregarMaridaje(maridaje6)
vino4_luigi.agregarMaridaje(maridaje1)
vino4_luigi.agregarMaridaje(maridaje8)

# Bodega Achaval Ferrer
vino1_achaval.agregarMaridaje(maridaje1)
vino2_achaval.agregarMaridaje(maridaje2)
vino2_achaval.agregarMaridaje(maridaje9)
vino3_achaval.agregarMaridaje(maridaje1)
vino3_achaval.agregarMaridaje(maridaje3)
vino4_achaval.agregarMaridaje(maridaje1)
vino4_achaval.agregarMaridaje(maridaje2)

# Bodega Domaine Bousquet
vino1_domaine.agregarMaridaje(maridaje1)
vino1_domaine.agregarMaridaje(maridaje12)
vino2_domaine.agregarMaridaje(maridaje2)
vino3_domaine.agregarMaridaje(maridaje5)
vino3_domaine.agregarMaridaje(maridaje15)
vino4_domaine.agregarMaridaje(maridaje1)
vino4_domaine.agregarMaridaje(maridaje9)

# Bodega Navarro Correas
vino1_navarro.agregarMaridaje(maridaje1)
vino1_navarro.agregarMaridaje(maridaje11)
vino2_navarro.agregarMaridaje(maridaje2)
vino2_navarro.agregarMaridaje(maridaje9)
vino3_navarro.agregarMaridaje(maridaje5)
vino3_navarro.agregarMaridaje(maridaje6)
vino4_navarro.agregarMaridaje(maridaje1)
vino4_navarro.agregarMaridaje(maridaje8)

# Bodega Chandon Argentina
vino1_chandon.agregarMaridaje(maridaje5)
vino2_chandon.agregarMaridaje(maridaje10)
vino2_chandon.agregarMaridaje(maridaje15)
vino3_chandon.agregarMaridaje(maridaje6)
vino3_chandon.agregarMaridaje(maridaje13)
vino4_chandon.agregarMaridaje(maridaje7)
vino4_chandon.agregarMaridaje(maridaje16)

# Bodega Pulenta Estate
vino1_pulenta.agregarMaridaje(maridaje1)
vino1_pulenta.agregarMaridaje(maridaje12)
vino2_pulenta.agregarMaridaje(maridaje2)
vino3_pulenta.agregarMaridaje(maridaje5)
vino3_pulenta.agregarMaridaje(maridaje13)
vino4_pulenta.agregarMaridaje(maridaje1)
vino4_pulenta.agregarMaridaje(maridaje9)

# Bodega Ruca Malen
vino1_ruca.agregarMaridaje(maridaje1)
vino2_ruca.agregarMaridaje(maridaje2)
vino2_ruca.agregarMaridaje(maridaje14)
vino3_ruca.agregarMaridaje(maridaje5)
vino3_ruca.agregarMaridaje(maridaje6)
vino4_ruca.agregarMaridaje(maridaje1)
vino4_ruca.agregarMaridaje(maridaje9)

#Maridajes  del sistema: 
maridajesSistemas = [maridaje1,maridaje2,maridaje3,maridaje4,maridaje5,maridaje6,maridaje7,maridaje8,maridaje9,maridaje10,maridaje11,maridaje12,maridaje13,maridaje14,maridaje15,maridaje16]

for maridaje in maridajesSistemas:
    print(maridaje.nombre)
    print("-"*50)
