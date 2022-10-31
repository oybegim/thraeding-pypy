import threading
import time

def otchestva1():
    for x in range(30):
        time.sleep(0.2)
        print("Sanjar qizi")

o1 = threading.Thread(target=otchestva1)

o1.start()