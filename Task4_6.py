# Lesson 4: Python Loop Statements
# 6. Advanced Looping Techniques

import random

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: The Selective DJ
print("Task 1: The Selective DJ")
selected_genres = genres[1:4]  # Slice from index 1 (inclusive) to index 4 (exclusive)
for genre in selected_genres:
    print(genre)

# Task 2: The One-Liner Band with List Comprehensions
print("\nTask 2: The One-Liner Band with List Comprehensions")
new_genres = [genre + " Music" for genre in genres]
print(new_genres)

# Task 3: Numerical Beats with range
print("\nTask 3: Numerical Beats with range")
for num in range(10, 0, -1):  # Start at 10, stop before 0, decrement by 1
    print(num)
print("The beat drops now!")
