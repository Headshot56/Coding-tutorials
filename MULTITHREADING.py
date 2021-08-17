#In python 3 make sure to add the underscore
import _thread as thread
import time

#Create a function for the threads
def print_time(delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ((time.ctime(time.time())))

#Create 2 threads
try:
    thread.start_new_thread(print_time, (2, ))
    thread.start_new_thread(print_time, (4, ))
except:
    print("Error: unable to start threads")

while 1:
    pass
