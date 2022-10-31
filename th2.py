import threading
import time

def ism1():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Mehrangiz")

def familiya1():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Amirbekova")

def otchestva1():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Samirbek qizi")


i1 = threading.Thread(target= ism1)
f1 = threading.Thread(target=familiya1)
o1 = threading.Thread(target=otchestva1)

i1.start()
f1.start()
o1.start()