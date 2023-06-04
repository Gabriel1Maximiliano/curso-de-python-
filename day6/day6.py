
# import os
# text_file = open('ejerciciodearchivos.txt')
# print( text_file.read() )

#print('basename:    ', os.path.basename(__file__))


# text_file = open('mi_archivo.txt','w')
# text_file.write('Nuevo texto')
# text_file.close()
# text_file = open('mi_archivo.txt','r')
# print( text_file.read() )
# text_file.close()

# archivo = open("mi_archivo.txt", "w")
# archivo.write("Nuevo texto")
# archivo.close()
# archivo = open("mi_archivo.txt", "r")
# print(archivo.read())

# archivo = open('registro.txt','a')
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# for log in registro_ultima_sesion:
#     archivo.writelines(log+"\t")
# archivo.close()

# archivo = open('registro.txt','r')
# print(archivo.read())
# archivo.close()

# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# file = open('registro.txt','a')

# for file in registro_ultima_sesion:
#     file.write(file + '\t')
    
# file.close()

# file = open('registro.txt','r')

# print( file.readLines() )

# import os
 
# text_file = os.chdir('C:\\Users\\Gabriel\\Desktop\\CursosFreeCodecamp\\Python')

# file = open('ejerciciodearchivos.txt')

# print( file.read() )

from pathlib import Path
# base = Path.home()
# guia = Path('Barcelona','sagrada')
# print(base)
# print(guia)
# from pathlib import Path
# ruta_base = Path.home()
# print( ruta_base )

ruta = Path('Curso Python', 'Dia 6',  'practicas_path.py')
ruta2 = Path( Path.home(),'Curso Python', 'Dia 6',  'practicas_path.py' )
print( ruta )
print( ruta2 )