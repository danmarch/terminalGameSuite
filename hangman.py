#The terminal game suite!
#Made for recreation by Dan March

import math
import random

def terminalGameSuite():
    for _ in range(100):
        print("\n")
    print("Welcome to the Terminal Game Suite!\n")
    print("Which game would you like to play? Please type the number corresponding to the name.\n")
    print("Options:\n    1) Hangman")
    input_game = raw_input()
    if input_game == "1" or input_game == "one":
        hangman()

def addspace():
    print("\n\n\n")

def startboard(word):
    print("-------")
    print("|     |\n")
    print("|\n")
    print("|\n")
    print("|\n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def onegot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|\n")
    print("|\n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def twogot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|     |\n")
    print("|\n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def threegot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|    /|\n")
    print("|\n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def fourgot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|    /|\ \n")
    print("|\n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def fivegot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|    /|\ \n")
    print("|     / \n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def sixgot(word):
    addspace()
    print("-------\n")
    print("|     |\n")
    print("|     O\n")
    print("|    /|\ \n")
    print("|     /\ \n")
    print("|\n")
    print("-------\n")
    print("\n")
    print(word)

def callToP2():
    print("Player two: guess a letter")

def callToP1():
    print("Guess a letter:")

def hangman():
    current_board = []
    contained_letters = []
    list_of_words = ["james franco", "john cena"]
    star_wars_words = ["he is a political idealist", "ki adi mundi", "mygeeto", "kashyyyk", "han solo dies",
                        "aweeeeeeeeeeeba", "darth darth binks", "meesa going home", "dellow felegates",
                        "i slaughtered them like animals", "only a sith deals in absolutes", "killing younglings",
                        "i hate sand", "midichlorians", "i have the high ground", "so uncivilized",
                        "meesa call for vote of no confidence", "they must be dead by now"]
    print("\n\n\n\n\n")
    print("How many players are there? Please answer 1 or 2.")
    inputSatisfied = False
    while not inputSatisfied:
        AI_or_naw = raw_input()
        if AI_or_naw == "1" or AI_or_naw == "one":
            input_word = random.choice(list_of_words)
            inputSatisfied = True
            print("Would you like to play with subjects? yes/no")
            inputIsGood = False
            while not inputIsGood:
                answer2 = raw_input()
                if answer2 == "yes" or answer2 == "Yes" or answer2 == "y" or answer2 == "Y":
                    print("Please select the number corresponding to a subject:\n")
                    print("   1) Star Wars")
                    desiredSubjectIsGood = False
                    while not desiredSubjectIsGood:
                        desiredSubject = raw_input()
                        if desiredSubject == "1" or desiredSubject == "one":
                            input_word = random.choice(star_wars_words)
                            desiredSubjectIsGood = True
                        else:
                            print("Please input a valid number.")
                    inputIsGood = True
                elif answer2 == "No" or answer2 == "no" or answer2 == "n" or answer2 == "N":
                    input_word = random.choice(list_of_words)
                    inputIsGood = True
                else:
                    print("Please enter yes or no.")
        elif AI_or_naw == "2" or AI_or_naw == "two":
            print("\n\nPlayer one: please input a word or phrase.")
            input_word = raw_input()
            input_word = input_word.lower()
            inputSatisfied = True
        else:
            print("Please type in 1 or 2")
    for _ in range(100):
        print("\n")
    print("CAUTION: if you scroll up, you will see player one's word.")

    for x in range(len(input_word)):
        current_board.append('_')
    if " " in input_word:
        index_stuff = []
        counter1 = 0
        while counter1 < len(input_word):
            if input_word[counter1] == " ":
                index_stuff.append(counter1)
            counter1 += 1
        for spaces in index_stuff:
            current_board[spaces] = "  "
    gameStillGoing = True
    NumErrors = 0
    current_state = 0
    startboard(current_board)

    while gameStillGoing:
        if AI_or_naw == "1" or AI_or_naw == "one":
            callToP1()
        else:
            callToP2()
        input_char = raw_input()
        input_char = input_char.lower()
        if len(input_char) != 1:
            print("Please input a single character")
            continue
        if input_char in contained_letters:
            print("You have already guessed this letter!\n")
            print("You've guessed:\n")
            print(contained_letters)
            print("\n\n\n")
            continue
        contained_letters.append(input_char)
        if input_char in input_word:
            counter = 0
            index_list = []
            while counter < len(input_word):
                if input_word[counter] == input_char:
                    index_list.append(counter)
                counter += 1
            for element in index_list:
                current_board[element] = input_char

            if current_state == 0:
                startboard(current_board)
            elif current_state == 1:
                onegot(current_board)
            elif current_state == 2:
                twogot(current_board)
            elif current_state == 3:
                threegot(current_board)
            elif current_state == 4:
                fourgot(current_board)
            elif current_state == 5:
                fivegot(current_board)

            if '_' not in current_board:
                print("\n")
                if AI_or_naw == "2" or AI_or_naw == "two":
                    print("Player two wins!")
                else:
                    print("You win!")
                gameStillGoing = False

        else:
            NumErrors += 1
            if NumErrors == 1:
                onegot(current_board)
                current_state = 1
            elif NumErrors == 2:
                twogot(current_board)
                current_state = 2
            elif NumErrors == 3:
                threegot(current_board)
                current_state = 3
            elif NumErrors == 4:
                fourgot(current_board)
                current_state = 4
            elif NumErrors == 5:
                fivegot(current_board)
                current_state = 5
            elif NumErrors == 6:
                sixgot(current_board)
                print("\n")
                if AI_or_naw == "2" or AI_or_naw == "two":
                    print("Player one wins!")
                else:
                    print("You lose!")
                print("The word was: " + input_word)
                gameStillGoing = False

    print("Would you like to play again? yes/no:")
    answer = raw_input()
    if answer == "yes" or answer=="Yes" or answer=="y" or answer=="Y":
        current_board = []
        hangman()
    else:
        for _ in range(100):
            print("\n")
        terminalGameSuite()
