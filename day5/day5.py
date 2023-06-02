# print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))
# SELECCION ALEATORIA DE PALITOS 
# from random import shuffle

# stick_list = ['-', '--', '---', '----']


# def mix_sticks(stick_list):
#     shuffle(stick_list)
#     return stick_list


# def try_your_luck():
#     try_user = ''
#     while try_user not in ['1', '2', '3', '4']:
#         try_user = input("Choose a number from 1 to 4: ")
#     return int(try_user)


# def check_your_try(stick_list, try_user):
#     selected_stick = stick_list[try_user - 1]
#     if selected_stick == '-':
#         print("You lose")
#     else:
#         print("You win")
#     print(f"You have touched the stick {selected_stick}")


# mixed_sticks = mix_sticks(stick_list)
# try_user = try_your_luck()
# check_your_try(mixed_sticks, try_user)

# import random

# def tirar_dados():
#     dice_1 = random.randint( 1,6 )
#     dice_2 = random.randint( 1,6 )
#     return dice_1,dice_2

# def evaluar_jugada():
#     res = tirar_dados()
#     suma_dados = res[0] + res[1]
#     if suma_dados <= 6:
#         print("La suma de tus dados es {suma_dados}. Lamentable")
#     elif suma_dados > 6 and suma_dados < 10:       
#         print("La suma de tus dados es {suma_dados}. Tienes buenas chances")
#     elif suma_dados >= 10: 
#         print("La suma de tus dados es {suma_dados}. Parece una jugada ganadora")    
# evaluar_jugada()

lista_numeros = [1,2,3,3,3,3,4]

def reducir_lista( lista_numeros ):
    
    no_repeat = set( lista_numeros )
    return list(no_repeat)
    


print(reducir_lista(lista_numeros))

def promedio(lista = reducir_lista(lista_numeros)):
    suma=0
    for num in lista:
        suma += num
        res = (float) (suma/(len( lista )))
    return res

print( promedio(reducir_lista(lista_numeros)) )