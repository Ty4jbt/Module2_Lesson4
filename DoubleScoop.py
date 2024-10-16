# Task 1
import random

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Tired", "Excited"]
time_of_day = ["morning", "afternoon", "evening"]

for day in day_of_week:
    for time in time_of_day:
        random_mood = random.choice(mood)
        print(f"On {day} {time} you were {random_mood}")