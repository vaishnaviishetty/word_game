import random

word_game = ["apple", "kiwi", "mango", "orange"]
hints = ["A red fruit", "green inside brown outside", "king of fruits", "its colour is the name of the fruit"]

# pick a word and its matching hint together
index = random.randint(0, len(word_game) - 1)
chosen_word = word_game[index]
hint = hints[index]

print("Hint:", hint)

length = len(chosen_word)
display = ["_"] * length   # separate variable, a list of underscores
print(" ".join(display))

start_game = True
lives = 4

while start_game:
    guess = input("Guess a character: ").lower()

    # check each position for a match
    for i in range(length):
        if chosen_word[i] == guess:
            display[i] = guess

    print(" ".join(display))

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong! {lives} lives left")

    if lives == 0:
        start_game = False
        print(f"You lost! The word was '{chosen_word}'")

    if "_" not in display:   # literal string, not the leftover loop variable
        start_game = False
        print("You won!")