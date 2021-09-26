import random

file = open("custom.txt", "r")
word = file.read().split("\n")

#The index variable used to find a random word in the custom list.
index = random.randint(0, (len(word) - 1))
#The variable which stores the word to it after an index has been found in the custom.txt file.
question = word[index]

#Where the game function is stored
#The amount of guesses that the player has available to them.
guesses = 10
lst = []
#The list contianing the empty word.



#Game Function
def game():
    global lst, guesses

    index_list = []

    print(" ".join(lst))

    guess = str(input("What letter do you guess? "))

    print(question)

    def indexes(list_name, index_search):
        nonlocal index_list

        list_copy = list(list_name)

        for i in range(len(list_name)):
            if list_copy[i] == index_search:
                index_list.append(i)

        print(index_list)

    for i in question:
        if i == guess:
            indexes(question, guess)

            for x in index_list:
                lst[x] = guess

            game()
        else:
            guesses -= 1
