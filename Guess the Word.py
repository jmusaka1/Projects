import random
import math

print("Welcome to Guess the Word!🕵️‍♀️")
print("Make sure to type the letters in order.")

#List of words to choose from
word_list = ["Apple", "Orange", "Banana", "Cherry", "Guava", "Red", "Magenta", "Blue", "Brown", "Black", "Panda", "Cat", "Dog", "Rabbit", "Monkey"]

while True:
    #Computer generates a random word and tells how many letters in that word
    random_word = random.choice(word_list)
    word_length = len(random_word)
    halfway = math.ceil(word_length/2)-1
    #Each letter a user correctly enters is saved
    user_word = ""
    counter = 0
    counter_1 = word_length

    while counter < word_length:
        #User enters a letter
        enter_a_letter = input("Enter a letter: ")

        while enter_a_letter.isdigit() or not enter_a_letter.isalpha():
            enter_a_letter = input("Please enter a letter: ")
            
        if enter_a_letter.isalpha():
            if counter == 0:
                enter_a_letter = enter_a_letter.upper()
            else:
                enter_a_letter = enter_a_letter.lower()

            if enter_a_letter == random_word[counter]:
                user_word += random_word[counter]
                counter_1 -= 1

                if counter_1 == 0:
                    break
                
                #Halfway mark
                print(f"That's correct! Only {counter_1} to go!")
                if counter == halfway:
                    print("You're at the halfway mark!")

                counter += 1
                
            #giving up
            elif counter > halfway:
                give_up = input("That's incorrect. Give up? (y/n): ").lower()
                while give_up != 'n' and give_up != 'y':
                    give_up = input("Please type y or n: ").lower()
                    
                if give_up == 'y':
                    play_again = input(f"The mystery word is {random_word}. Play another round? (y/n): ").lower()
                    while play_again != 'n' and play_again != 'y':
                        play_again = input("Please type y or n: ").lower()

                    if play_again == 'y':
                        break
                    
                    if play_again == 'n':
                        print("Thanks for playing!")
                        break

            else:
                print("That's incorrect. Try again. ")
                
        else:
            print("That's incorrect. Try again. ")

    if user_word != random_word and play_again == 'n':
        break
    
    #Playing another round
    if user_word == random_word:
        play_again = input(f"You've guessed it! It's {random_word}! Play again? (y/n)").lower()
        while play_again != 'n' and play_again != 'y':
            play_again = input("Please type y or n: ").lower()
                
        if play_again == 'n':
            print("Thanks for playing!")
            break
        