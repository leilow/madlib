#---ROSES ARE RED MADLIB---#

print("\n\n\nWelcome to my MadLib! You'll be prompted to enter some information soon.")
noun = input("\nThink of a noun and enter: ")
adjective = input("\nThink of an adjective and enter: ")
second_noun = input("\nThink of another noun and enter: ")
second_adjective = input("\nThink of another adjective and enter: ")
third_noun = input("\nThink of yet another noun and enter: ")
third_adjective = input("\nLast adjective of the Madlib, promise: ")
fourth_noun = input("\nLast but not least, we need one more noun: ")
print("\nHere it comes! Your very own Madlib: ")

# madlib
print(f"\n{noun} are {adjective}, \n{second_noun} are {second_adjective}, \n{third_noun} is {third_adjective}, \nand so are {noun}.")





# # --- Ada Builds Madlib --- #

# # list to store all the parts of speech
# # list are objects for storing data that you can access throughout the program

# parts_speech = [ 
#     'noun',
#     'noun, plural',
#     'adjective',
#     'second_adjective',
#     'adverb',
#     'verb',
#     'second_verb',
#     'verb, past tense',
#     'verb, ing',
#     'conjunction',
#     'number',
# ]

# # dictionary to store user input
# # dictionary is left empty to take in arguments as the loop runs (left empty to be filled)
# parts_speech_and_words = {}

# # loop to prompt the user for input
# # this loop is iterating over parts of speech from our list as it shows the user...
# # ... questions for input
# print(f"\n-----\nWelcome. Let's play a game of Madlibs!")


# for part in parts_speech:
#   word = input(f'Please enter {part}: ') # input is a simple function that takes in data and directs it to desired output
#   parts_speech_and_words[part] = word # parts of speech are the words our user inputs, 'part' is the item placeholder name

# # print(parts_speech_and_words) # this is a test, it should print out the key-value pairs created with user input

# # print madlib using the list in {} and the item name in []
# # use an fstring with {parts_speech_and_words['part']}
# # parts_speech_and_words is the user generated through input dictionary of words

# print(f"\n-----\nWhat a {parts_speech_and_words['adjective']} day to be alive ... {parts_speech_and_words['conjunction']} not?")
# print(f"The plan is to go to the Big {parts_speech_and_words['noun'].title()} Downtown.")
# print(f"Afterward go for a quick {parts_speech_and_words['verb']} at the park.")
# print(f"Then lunch with my best {parts_speech_and_words['noun, plural']} in Chinatown.")
# print(f"Maybe an afternoon {parts_speech_and_words['second_verb']} is in order too.")
# print(f"Yesterday was also {parts_speech_and_words['adjective']}! {parts_speech_and_words['verb, past tense'].capitalize()} from 3pm-5pm sharp.")
# print(f"What\'s for dinner you ask?")
# print(f"How about a {parts_speech_and_words['number']} {parts_speech_and_words['adverb']} delicious noodles.")
# print(f"Dont worry about {parts_speech_and_words['verb, ing']}, I'll take care of it later!")