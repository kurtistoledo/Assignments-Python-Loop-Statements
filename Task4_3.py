# Lesson 4: Python Loop Statements
# 3. Loop Condition Logic

count = 0
while True:  # Infinite loop condition
    print("This is iteration number", count + 1)
    count += 1
    if count >= 5:
        break  # Exit the loop after 5 iterations

count = 0
while count < 5:  # Loop will terminate when count is no longer less than 5
    print("This is iteration number", count + 1)
    count += 1