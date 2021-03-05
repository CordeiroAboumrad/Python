import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
data_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dictionary)

word = input("Type the word desired for the NATO conversion: ")
word_to_NATO = [data_dictionary[letter.upper()] for letter in word]
print(word_to_NATO)
