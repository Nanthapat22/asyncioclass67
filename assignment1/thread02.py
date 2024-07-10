# running a function with arguments in another thread
<<<<<<< HEAD
from time import sleep,ctime 
from threading import Thread

def task (sleep_time, message):
    sleep(sleep_time)
    print(f'{ctime()} {message}')
    
thread = Thread(target=task, args=(1.5,'New message from another thre'))

thread.start()
print(f'{ctime()} waiting for the thread...')
thread.join()
=======
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> 36bd7d438baf7a78c533f17abd8ac6f054dcf2a7
