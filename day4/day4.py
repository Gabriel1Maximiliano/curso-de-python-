
# frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
# palabra1 = "éxito"
# palabra2 = "tecnología"


# mi_bool = frase.find("éxito")  >= 0 and frase.find("tecnología") >= 0
# print(mi_bool)

# num1 = int(input("Ingresa un número:"))
# num2 = int(input("Ingresa otro número:"))

# f"{num1} es mayor que {num2}"
# "num2 es mayor que num1"
# "num1 y num2 son iguales"
# if num1 > num2: True
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print(f"{num1} y {num2} son iguales")


# edad = 16
# tiene_licencia = False



# if tiene_licencia and edad >= 18:
#     print("Puedes conducir")
# elif edad < 18:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# elif not ( tiene_licencia ):
#     print("No puedes conducir. Necesitas contar con una licencia")

habla_ingles = False
sabe_python = True








# if habla_ingles and sabe_python:
#     print("Cumples con los requisitos para postularte")
# elif not habla_ingles and not sabe_python:
#     print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
# elif not habla_ingles and sabe_python:
#     print("Para postularte, necesitas tener conocimientos de inglés")
# else: print("Para postularte, necesitas saber programar en Python")

# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma = 0
# for num in lista_numeros:
#     suma +=num

# print(suma)

# numero = 10

# while numero > -1:
#     print(numero)
#     numero-=1


# numero = 50

# while numero > -1:
#     if numero % 5 == 0:
#         print(numero)
#         numero -=1
#     else: 
#         numero -=1
#         continue
# print(numero)



# lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# for num in lista_numeros:
#     if num < 0: break
#     else:print(num)

# mi_lista = list(range(3,301,3))

# print( mi_lista )

# suma_cuadrados = 0
# num = 1
# while num < 16:
#    suma_cuadrados += (num*num)
#    num+=1
    
# print(suma_cuadrados)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

indice=[]
for name in lista_nombres:
   if name[0] == 'M':
       indice.append( lista_nombres.index(name) )
# tupla = tuple(enum_list)
#print(tupla)
# for tuple_name in tupla:
#     print(tuple_name)
   
# for index_of in indice:
#     print(index_of)

# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# for capital, country in list( zip( capitales,paises ) ):
#     print(f"La capital de {country} es {capital}")

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

# number_1 = list('uno', 'um', 'one')
# number_2 = list('dos', 'dois', 'two')
# number_3 = list('tres', 'três', 'three')
# number_4 = list('cuatro ', 'quatro ', 'four')
# number_5 = list('cinco ', 'cinco ', 'five')
# lista_numbers = [('uno', 'um', 'one'),('dos', 'dois', 'two'),
#                  ('tres', 'três', 'three'),('cuatro ', 'quatro ', 'four'),('cinco ', 'cinco ', 'five')]
# numbers_to_translate = [1,2]

# numeros = list(zip( lista_numbers,numbers_to_translate ))

# print( numeros )

# lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
# valor_maximo = max( lista_numeros )
# print(valor_maximo)

# diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

# edad_minima = min( diccionario_edades.values() )
# ultimo_nombre = max( diccionario_edades )
# print(ultimo_nombre)
# print( edad_minima )

from random import *

aleatorio = random()
print( aleatorio )