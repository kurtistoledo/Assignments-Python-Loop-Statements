# Lesson 4: Python Loop Statements
# 5. Looping Lists - The Rhythm of Repetition

import random

# Task 1: The for Loop DJ Set
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Using a for loop with a counter
print("Task 1: The for Loop DJ Set")
for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: Now playing {genre}!")

print("\n")

# Task 2: The Remix Artist with while
# Using a while loop with a condition to stop if "Hip-hop" is played
print("Task 2: The Remix Artist with while")
index = 0
while index < len(genres):
    genre = genres[index]
    print(f"Track {index + 1}: Now playing {genre}!")
    if genre == 'Hip-hop':
        break
    index += 1

print("\n")

# Task 3: Light Show Technician Loop
# Using the range() function to loop through genres by index and skip "Classical"
print("Task 3: Light Show Technician Loop")
for index in range(len(genres)):
    genre = genres[index]
    if genre == 'Classical':
        continue
    print(f"Track {index + 1}: Light show is ready for {genre}!")