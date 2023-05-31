# first step the user input a phrase 
phrase = "Le vAs a decir al usuario cuántas palabras hay a lo largo de todo el texto"
#second the user input 3 letters
lettersToSeach = ['a','b','c']

amount_of_firstLetter  = phrase.lower().count( lettersToSeach[0].lower() )
amount_of_secondLetter = phrase.lower().count( lettersToSeach[1].lower() )
amount_of_thirdLetter  = phrase.lower().count( lettersToSeach[2].lower() )
#thrid we count the amount of words in this phrase

amount_of_words = len( phrase.split(" "))
print( "Welcome to Day 3 Python course" )

print( f"The amount of '{lettersToSeach[0]}' is {amount_of_firstLetter}" )
print( f"The amount of '{lettersToSeach[1]}' is {amount_of_secondLetter}" )
print( f"The amount of '{lettersToSeach[2]}' is {amount_of_thirdLetter}" )
print( f"The amount of words is { amount_of_words }\n")

# fourth we need the first and the last letter of the phrase
first_phrase_letter       =  phrase[0] 
last_letter_of_the_phrase = phrase[len(phrase) - 1] 
print( f"The first letter of the phrase is: { first_phrase_letter  }\n" )
print( f"The last letter of the phrase is: { last_letter_of_the_phrase }\n" )

#reverese phrase
print("Reverse phrase")
reverse_phrase = phrase[::-1]
print( f"'{reverse_phrase}'" )
print("Is the word Python in this text?")
print( "Python" in phrase )



