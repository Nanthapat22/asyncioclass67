# running a function in another thread
<<<<<<< HEAD
from time import sleep,ctime 
from threading import Thread


def task():
    
    sleep(1)

    print(f'{ctime()} This is from another thread')  
   
    
thread = Thread(target=task)
thread.start()
print(f'{ctime()} waiting for the thread...')
thread.join() 
=======
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> 36bd7d438baf7a78c533f17abd8ac6f054dcf2a7
