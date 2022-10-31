import threading
import time

def otchestva():
    for x in range(30):
        time.sleep(0.2)
        print("Sanjar ogli")

o = threading.Thread(target=otchestva)

o.start()