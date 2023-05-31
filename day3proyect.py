phrase = "Le vAs a decir al usuario cuántas palabras hay a lo largo de todo el texto"
letters_to_Search = ['a', 'b', 'c']

count_of_firstLetter = phrase.lower().count(letters_to_Search[0].lower())
count_of_secondLetter = phrase.lower().count(letters_to_Search[1].lower())
count_of_thirdLetter = phrase.lower().count(letters_to_Search[2].lower())

word_count = len(phrase.split(" "))
print("Welcome to Day 3 Python course")

print(f"The count of '{lettersToSearch[0]}' is {count_of_firstLetter}")
print(f"The count of '{lettersToSearch[1]}' is {count_of_secondLetter}")
print(f"The count of '{lettersToSearch[2]}' is {count_of_thirdLetter}")
print(f"The count of words is {word_count}\n")

first_letter = phrase[0]
last_letter = phrase[len(phrase) - 1]
print(f"The first letter of the phrase is: {first_letter}\n")
print(f"The last letter of the phrase is: {last_letter}\n")

reverse_phrase = phrase[::-1]
print("Reverse phrase")
print(f"'{reverse_phrase}'")
print("Is the word Python in this text?")
print("Python" in phrase)
