# Task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(7):
    random_mood = random.choice(moods)

    print(f"On {day_of_week[day]}, you were feeling {random_mood}.")
