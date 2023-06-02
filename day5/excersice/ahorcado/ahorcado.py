from random import choice 


allowed_words = ["hola","chau"]
user_lifes = 3

def mix_words( allowed_words ):
     word_to_guess =choice(allowed_words)  
     return word_to_guess


def input_user_letter( user_lifes ):
    lifes = user_lifes
    user_letter=''
    guessed_word = []
    counter_success =1
    choiced_word = mix_words( allowed_words )
    for letter in list(choiced_word):
        guessed_word.append('#')
    print(f"La palabra elegida es { choiced_word }")
    
    
    while lifes > 0:
            user_letter = input( "Ingrese una letra: " )
            if choiced_word.find( user_letter ) == -1:
                print("Letra equivocada")
                lifes -=1
                print(f"Te quedan { lifes } vidas")
            else:
                counter_success+=1
                if counter_success <= len( choiced_word ) and counter_success >= 0:
                    lista =  list(choiced_word)
                    for index,item in enumerate( lista ) :
                        if user_letter == item:
                            guessed_word[index] = user_letter
                    print( guessed_word )
                    print(f"Acertaste todavia tenés { lifes } vidas")    
                else:
                    print( list( choiced_word ) )
                    print("Adivinaste la palabra!!")
                    return
    
       
    
input_user_letter( user_lifes )