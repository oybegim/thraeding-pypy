import threading
import time

def familiya():
    for x in range(30):
        time.sleep(0.2)
        print("Mustafoyev")

f = threading.Thread(target=familiya)

f.start()