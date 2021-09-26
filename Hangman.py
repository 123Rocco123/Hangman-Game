#Hangman Game
from module1 import game, question, lst

Game_Option = str(input("Do you want to use custom or pre-generated words (custom / pre)? "))

#The if statement is to determine if the player wants to create a list containing their own words, or random ones.
if Game_Option == "custom":
    #The file variable is assigned to the custom file in the file directory.
        #It's used to open and get the words from it.
    #The word variable is to split the different lines, so that each one is considered its own word.

    for i in range(len(question)):
        lst.append("_")

    game()

    list_length = len(lst)
    end_list_length = 0

    for elements in lst:
        if elements != "_":
            end_list_length += 1
            if end_list_length == end_list_length:
                print("Congrats, you win!")
                quit()
