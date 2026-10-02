import threading
import time

def order_complete(seconds):
    print(f"order will complete in {seconds} seconds")
    time.sleep(seconds)

# order_complete(4)
# order_complete(2)
# order_complete(1)

t1 = threading.Thread(target=order_complete, args=[4])
t2 = threading.Thread(target=order_complete, args=[2])
t3 = threading.Thread(target=order_complete, args=[1])

t1.start()
t2.start()
t3.start()
