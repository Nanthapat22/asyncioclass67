# running a function with arguments in another thread
from time import sleep,ctime 
from threading import Thread

def task (sleep_time, message):
    sleep(sleep_time)
    print(f'{ctime()} {message}')
    
thread = Thread(target=task, args=(1.5,'New message from another thre'))

thread.start()
print(f'{ctime()} waiting for the thread...')
thread.join()