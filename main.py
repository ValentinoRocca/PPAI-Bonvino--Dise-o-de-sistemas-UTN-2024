from Bodega import Bodega
from clases import Enofilo
from Vino import Vino
from clases import Varietal
from clases import TipoUva
from clases import Siguiendo
from clases import Maridaje
from clases import Usuario
import datetime
from interfaz import interfaz

#fecha = datetime.datetime(2020,5,17)
fecha = datetime.datetime(2024,1,17)

fecha2 = datetime.datetime(2024,1,15)
fecha3 = datetime.datetime(2021,4,20)
#---INSTANCIAS DE USUARIO---
usuario1 = Usuario("Carlos Gomez", "carlos@example.com", "contraseña123")
usuario2 = Usuario("Marcos Diaz", "Marcos@example.com", "segura456")
usuario3 = Usuario("Juan Ricciardo", "juan@example.com", "clave789")
#---INSTANCIAS DE BODEGA---#

bodega = Bodega(None, None,None, 'BodegaMalbec', 2, fecha )
bodega2 = Bodega(None, None,None, 'holex', 2, fecha2 )
bodega3 = Bodega(None, None,None, 'holaa', 2, fecha3 )
#print(bodega.nombre)

'''bodega1 = Bodega("42.4194° N, 71.1062° W", "Viñedos del Valle es una bodega familiar dedicada a la producción de vinos orgánicos y sostenibles.", "Fundada en 1998 por la familia Martínez, Viñedos del Valle ha crecido hasta convertirse en una de las bodegas líderes de la región.", "Viñedos del Valle", 6, fecha )

bodega2 = Bodega("36.7783° N, 119.4179° W",
"Una bodega innovadora en el corazón de California, conocida por sus vinos orgánicos y prácticas sostenibles.",
"Fundada en 1990, Bodega del Sol ha liderado el movimiento de la vinificación sostenible. Con más de 30 años de experiencia, ha ganado numerosos premios por la calidad de sus vinos.",
"Bodega del Sol",6,fecha2)

bodega3 = Bodega("40.7128° N, 74.0060° W","Ubicada en el pintoresco valle de Hudson, Bodega Las Estrellas es conocida por sus exquisitos vinos tintos y blancos.","Desde su establecimiento en 2005, Bodega Las Estrellas ha combinado métodos tradicionales con innovación moderna para producir vinos que reflejan la riqueza del terruño de Nueva York.","Bodega Las Estrellas",12,fecha3)'''



#Crear clases
#---INSTANCIAS DE ENOFILO---#
'''
enofilo1 = Enofilo("Carlos","Gomez","ImagenPerfil",[bodega1,bodega2],usuario1)

enofilo2 = Enofilo("Marcos","Diaz","ImagenPerfil",[bodega1,bodega3],usuario2)

enofilo3= Enofilo("Juan","Ricciardo","ImagenPerfil",[bodega1,bodega2,bodega3],usuario3)

#---INSTANCIAS DE MARIDAJE---#
maridaje1 = Maridaje("Queso y Vino Tinto", "Un clásico maridaje donde los sabores intensos del queso se equilibran con la riqueza y los taninos del vino tinto.")

maridaje2 = Maridaje("Mariscos y Vino Blanco", "Los mariscos frescos combinan perfectamente con la acidez y frescura de un vino blanco joven.")

maridaje3 = Maridaje("Chocolate y Vino de Postre", "El dulzor del chocolate encuentra su mejor complemento en la complejidad y dulzura de un vino de postre.")
#---INSTANCIAS DE TIPO DE UVA---#
tipo_de_uva1 = TipoUva("Cabernet Sauvignon", "El Cabernet Sauvignon es una variedad de uva tinta conocida por su intensidad y estructura, con sabores a grosellas, moras y pimientos verdes.")

tipo_de_uva2 = TipoUva("Chardonnay", "El Chardonnay es una uva blanca versátil que produce vinos con una amplia gama de sabores, desde cítricos frescos hasta aromas a mantequilla y vainilla, dependiendo de la vinificación.")

tipo_de_uva3 = TipoUva("Malbec", "El Malbec es una uva tinta de origen francés que se ha convertido en la variedad emblemática de Argentina, produciendo vinos de cuerpo medio a completo con notas a ciruelas, moras y especias.")

#Instancias Varietal



#-------- PROBANDO VINOS ------

vinoac1 = Vino("Gordo","img1", "Nota1", 3441, "añada", [], [],[], bodega1, datetime(2003,5,18) )
vinoac2 = Vino("Gordasa","img2", "Nota2", 34241, "añada2", [], [],[], bodega1, datetime(2004,5,18) )
vinosAct =[vinoac1, vinoac2]

vinoprueba = Vino("Gordito","img3", "Nota3", 3443, "aniadir", [], [],[], bodega2, datetime(2004,1,13) )

# validamos que esté para actualizar (deberia devolver true y un print)
paraAct =  vinoprueba.SosVinoAActualizar(vinosAct)


#Probando los seteos para act

print(vinoprueba.notaCataVino)
vinoprueba.setNotaCata("umadelisia")
print(vinoprueba.notaCataVino)
'''

# Inicializar interfaz
interfaz.inicializar_interfaz(bodega)










