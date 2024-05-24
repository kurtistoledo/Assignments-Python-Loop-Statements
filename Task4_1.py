# Lesson 4: Python Loop Statements
# 1. The Range Riddle

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(len(days_of_week)):
    mood = moods[day % len(moods)]
    print(f"On {days_of_week[day]}, you were feeling {mood}.")
