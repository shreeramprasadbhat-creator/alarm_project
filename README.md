# alarm_project
- datetime: Lets you check the current time (hour, minute, etc.). - time: Used to pause the program for 1 second between checks. - pygame: A game library. Here, it’s used to play sound.
- r"...": Raw string format to avoid errors with backslashes (\) in file paths.
- This line tells Python where your alarm sound file is saved.

 Initializing and Loading Sound
pygame.mixer.init()
pygame.mixer.music.load(sound_path)


- pygame.mixer.init(): Starts the sound system.
- load(sound_path): Loads your MP3 file so it’s ready to play.

 Getting User Input for Alarm Time
hour = int(input("Hour (1–12): "))
minute = int(input("Minute (0–59): "))
period = input("AM or PM: ").lower()


- Asks the user to enter the alarm time.
- .lower() makes sure AM/PM is in lowercase for easy comparison.

 Converting to 24-Hour Format
if period == "pm" and hour != 12:
    hour += 12
elif period == "am" and hour == 12:
    hour = 0


- Converts 12-hour input to 24-hour format (used by datetime).
- Example: 2 PM becomes 14, and 12 AM becomes 0.

 Confirmation Message
print("Alarm set!")


- Just tells the user that the alarm is ready.

 Checking Time in a Loop
while True:
    now = datetime.datetime.now()
    if now.hour == hour and now.minute == minute:
        print("Wake up!")
        pygame.mixer.music.play()
        break
    time.sleep(1)


- while True: Keeps checking the time every second.
- datetime.datetime.now(): Gets the current time.
- If the current hour and minute match your alarm:
- It prints “Wake up!”
- Plays the alarm sound
- break stops the loop.
- time.sleep(1): Waits 1 second before checking again (saves CPU).
