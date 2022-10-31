import threading
import time

def ism():
    for x in range(30):
        time.sleep(0.2)
        print("Dilshod")

i = threading.Thread(target=ism)

i.start()