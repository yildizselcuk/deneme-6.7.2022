secret_word = "Serdar"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("type your guesses :")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of guesses, please try again")
else:
    print("You won!")