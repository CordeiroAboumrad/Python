import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
data_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dictionary)

is_wrong = True
while is_wrong:
    try:
        word = input("Type the word desired for the NATO conversion: ")
        word_to_NATO = [data_dictionary[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters are allowed for the conversion.")
    else:
        print(word_to_NATO)
        print("Application successful.")
        is_wrong = False
