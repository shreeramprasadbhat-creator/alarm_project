import datetime
import time
import pygame

# Use raw string or double backslashes to avoid syntax errors
sound_path = r"C:\Users\shree\Downloads\rooster (1).mp3"

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(sound_path)

hour = int(input("Hour (1–12): "))
minute = int(input("Minute (0–59): "))
period = input("AM or PM: ").lower()

if period == "pm" and hour != 12:
    hour += 12
elif period == "am" and hour == 12:
    hour = 0

print("Alarm set!")

while True:
    now = datetime.datetime.now()
    if now.hour == hour and now.minute == minute:
        print("Wake up!")
        pygame.mixer.music.play()
        break
    time.sleep(1)