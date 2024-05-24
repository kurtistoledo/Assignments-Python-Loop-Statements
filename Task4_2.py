# Lesson 4: Python Loop Statements
# 2. Double Scoop with Nested Loops

import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Tired"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were feeling {mood}.")
