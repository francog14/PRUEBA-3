"""import json
with open ('biblioteca.json', 'r') as archivo:
    datos_leidos = json.load(archivo)
print (datos_leidos)"""

Autor= datos_leidos['Autor']
Categoria= datos_leidos['Categoria']
Libro= datos_leidos['Libro']
Usuario= datos_leidos['Usuario']
Prestamo= datos_leidos['Prestamo']

print ("********************************")
print ("*         MUNDO LIBRO          *")
print ("********************************")
def inicio(): 
 mantener=print("[1]-Mantener libros")
 reportes=print("[2]-Reportes")
 salir=print("[3]-Salir")



 return

inicio()
bienvenido= print(input("Bienvenido a mundo libro ingrese una opción: "))

if bienvenido == "3":  
   print("A salido")

if bienvenido == "2":
 print ("reportes")



if bienvenido == "1":
 print ("********************************")
 print ("*     MANTENEDOR DE LIBROS     *")
 print ("********************************")

agregar= print("[1]-Agregar libro")
editar= print("[2]-Edita libro")
eliminar= print("[3]-Eliminar libro")
buscar = print("[4]-Buscar libro")
volver= print("[5]-Volver")

pregunta= print(input("Indique una opción: "))

#import json
#with open ('biblioteca.json', 'w') as archivo:
 #   datos_leidos = json.(archivo)


#Autor= datos_leidos['Autor']
#Categoria= datos_leidos['Categoria']
#Libro= datos_leidos['Libro']
#Usuario= datos_leidos['Usuario']
#Prestamo= datos_leidos['Prestamo']

if pregunta == '1':
 with open("biblioteca.json", "w")as archivo_json:
  json.dump  (datos_leidos, archivo_json) 



if pregunta == "2":
   print
if (pregunta == 5):
 print (inicio())
 
 
 
 
 
"""import json
with open ('biblioteca.json', 'r') as archivo:
    datos_leidos = json.load(archivo)


Autor= datos_leidos['Autor']
Categoria= datos_leidos['Categoria']
Libro= datos_leidos['Libro']
Usuario= datos_leidos['Usuario']
Prestamo= datos_leidos['Prestamo']"""



