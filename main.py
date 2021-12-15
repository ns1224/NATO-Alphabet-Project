import pandas as pd

# Reads nato codes into df obj
df_nato = pd.read_csv('nato_phonetic.csv')

# Creates dict, form letter: code name
nato_dict = {row.letter: row.code for (index, row) in df_nato.iterrows()}

# Takes user input word, returns Code output
# E.g. input ('Thomas') e.g. output ['Tango', 'Hotel', 'Oscar', 'Mike', 'Alfa', 'Sierra']


def nato_encoder(word):
    """Returns Nato code for letters in user inputted word"""
    letters = [letter for letter in word.strip().upper()]
    code_list = [nato_dict[letter] for letter in letters]

    return code_list


def main():

    word = ""
    while word != "DONE":

        word = input("Enter a word: ").upper()

        if word == "DONE":
            break

        elif word != "DONE":
            print(nato_encoder(word))
            word = input("Enter a word: ").upper()

    print("Thanks for using the NATO coder!")


main()
