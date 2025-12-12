#Mijanur Rahman- 2212342642
import threading
import time

# Version 1: WITHOUT LOCK

class Counter_NoLock:
    def __init__(self):
        self.value = 0

    def increment(self):
        temp = self.value
        time.sleep(0.0001)    
        temp = temp + 1
        self.value = temp

# Version 2: WITH LOCK

class Counter_WithLock:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            temp = self.value
            time.sleep(0.0001)  
            temp = temp + 1
            self.value = temp


def run_counter(counter_obj):
    for _ in range(1000):
        counter_obj.increment()



counter1 = Counter_NoLock()
threads = []

for _ in range(3):
    t = threading.Thread(target=run_counter, args=(counter1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("WITHOUT LOCK:")
print("Final counter value:", counter1.value)   # Expected wrong result (< 3000)


counter2 = Counter_WithLock()
threads = []

for _ in range(3):
    t = threading.Thread(target=run_counter, args=(counter2,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nWITH LOCK:")
print("Final counter value:", counter2.value)   # Expected = 3000
