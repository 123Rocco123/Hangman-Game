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

def end_func():
    global end_list_length

    list_length = len(lst)
    end_list_length = 0

    for i in range(list_length):
        if lst[i] != "_":
            end_list_length += 1

            if end_list_length == list_length:
                print("Congrats, you win!")
                quit()

#Game Function
def game():
    global lst, guesses

    index_list = []

    print(" ".join(lst))

    guess = str(input("What letter do you guess? "))

    #print(question)

    #Function used to change list index to actual letter
    def indexes(list_name, index_search):
        nonlocal index_list

        #Variable used to store a copy of the word in a list format
        list_copy = list(list_name)

        #For loop used to see if the user's guess is correct.
            #It will use the length of the list to check the indexes of the list copy, and see if the guess is the same letter as whats in the list.
        for i in range(len(list_name)):
            if list_copy[i] == index_search:
                #It will then append the inside to the nonlocal list "index_list".
                    #The indexes will then be used to change the list that's being printed to the terminal.
                index_list.append(i)

        #print(index_list)

    for i in question:
        if i == guess:
            indexes(question, guess)

            for x in index_list:
                lst[x] = guess
                end_func()

            game()
        else:
            guesses -= 1
