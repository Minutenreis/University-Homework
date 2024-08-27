
time = input("Enter the time in seconds: ")
time = int(time)

seconds = time % 60
time = time // 60

minutes = time % 60
time = time // 60

hours = time % 24
time = time // 24

days = time

print("The time is:")
print(days, "d", hours, "h", minutes, "m", seconds, "s")