# Lesson 4: Python Loop Statements
# 4. Python's Random Game Night

import random

items = ["apple", "banana", "cherry", "date", "elderberry"]
selected_item = random.choice(items)

guess = input(f"Guess which item was selected from the following list: {items}\nYour guess: ")

if guess == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Sorry, you guessed wrong. The correct item was {selected_item}.")
