import threading
import time
def ism():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Mustafo")

def familiya():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Amirbekov")

def otchestva():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Samirbek o'g'li")
    
i = threading.Thread(target=ism)
f = threading.Thread(target=familiya)
o = threading.Thread(target=otchestva)

i.start()
f.start()
o.start()
