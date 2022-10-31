import threading
import time

def ogil():
    for x in range(30):
        time.sleep(0.2)
        print("Ogil:")
o1 = threading.Thread(target=ogil)

o1.start()