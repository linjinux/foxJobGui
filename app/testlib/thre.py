import threading
def func1():
    print('Do something.')
    global timer
    timer = threading.Timer(3, func1)
    timer.start()
func1()