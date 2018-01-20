

import time
import webbrowser
import random
import os




# check if the user has the YT.txt file in the same area as python-alarm-clock.py

if os.path.isfile("YT.txt") == False:
    print "ERROR: YT.txt file not present. Creating file..."
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY 
    filecreate = os.O_CREAT | os.O_EXCL | os.O_WRONLY 
    with os.fdopen(fisierCreat, 'w') as fileCreated:
        filecreated.write("https://youtu.be/tSPLpQZnPXA")

# user can set the time they want to wake-up. 
print "What time do you want to wake up?"
print "Use this form.\nExample: 0630"
Alarm = raw_input("> ")



# State the Time variable so it's usable in the while-loop
Time = time.strftime("%H:%M")

# Open the text file with the youtube links
with open("YT.txt") as f:
        # urls are stored in the content variable
        content = f.readlines()

# when the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:
    print "The time is: " + Time

    # Restate Time variable allows the time to refresh
    # when I tried keeping the varible outside of the loop it just repeated the initial time
    Time = time.strftime("%H:%M")

    # This keeps the loop from flooding the command line with "time" updates
    time.sleep(1)

# If the Time variable is equal to the alarm string this code is run
if Time == Alarm:

    print "Time to wake up, playa!"
    # from the variable content a random link is chosen and then that link is stored in random_video variable
    random_video = random.choice(content)
    # using the webbrowser library it opens the youtube video link
    # videos can be whatever user prefers
    webbrowser.open(random_video)
