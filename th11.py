import threading
import time

def familiya1():
    for x in range(30):
        time.sleep(0.2)
        print("Mustafoyeva")

f1 = threading.Thread(target=familiya1)

f1.start()