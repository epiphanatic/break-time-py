import time
import webbrowser

# total_breaks is how many times this will run
# time.sleep() holds number of seconds between breaks
# so to take a break every hour, and do so 6 times, you would put
#   total_breaks = 6, and time.sleep(3600)
# the url below you can change to whatever you would like to open on
#   your screen when it's time for a break
total_breaks = 6
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=ckhasegf2wA")
    break_count = break_count + 1
