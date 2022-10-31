import threading
import time

def ism1():
    for x in range(30):
        time.sleep(0.2)
        print("Dilshoda")

i1 = threading.Thread(target=ism1)

i1.start()