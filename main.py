num = 55
guess = 0
guesses_count = 3

limit = 0
out_of_guesses = False

while int(guess) != num and not out_of_guesses:
    if guesses_count > limit:
        # print(f"{guesses_count} guesses remaining")
        guess = input("Guess a # between 1-100: ")
        guesses_count -= 1
        if int(guess) > num:
          
            print("Your guess was too high")
            print(f"{guesses_count} guesses remaining")
        elif int(guess) < num:
            
            print("Your guess was too low")
            print(f"{guesses_count} guesses remaining")

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You ran out of guesses")
else:
    print("You guessed it! Great job!")