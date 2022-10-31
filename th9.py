import threading
import time

def qiz():
    for x in range(30):
        time.sleep(0.2)
        print("Qiz:")

q = threading.Thread(target=qiz)

q.start()