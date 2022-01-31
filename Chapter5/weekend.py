import datetime

def DailyGreeting():
    from datetime import datetime
    now = datetime.now()
    currentTime = now.hour
    
    if currentTime < 12 and currentTime >=5:
        timeOfDay = "Good morning"
    elif currentTime >= 12 and currentTime < 16:
        timeOfDay = "Good afternoon"
    elif currentTime >= 16 and currentTime < 24:
        timeOfDay = "Good evening"
    else:
        timeOfDay = "Good night"
    return timeOfDay

print(DailyGreeting(), end='! ')


# I changed how the code was written because it wasn't outputting properly for me, hopefully this is an acceptable submission
# If not let me know and i'll type up the code the way you had it

weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

now = datetime.date.today()
dayOfWeek=now.weekday()
today=weekDays[dayOfWeek]


if today=='Sunday':
    print(f'It\'s {today}, my CIT 228 homework is due tonight!')
elif today=='Monday':
    print(f'Ugh, it\'s {today}, and my CIT 190 homework is due')
elif today=='Tuesday':
    print(f'YIPEE IT\'S TACO {today.upper()}!!!!')
elif today=='Wednesday':
    print(f'IT\'S WEENEIE {today.upper()}!!!')
elif today=='Thursday':
    print(f'It must be {today}, I never could get the hang of {today}\'s...')
else:
    print(f'Woo hoo, the weekend')
