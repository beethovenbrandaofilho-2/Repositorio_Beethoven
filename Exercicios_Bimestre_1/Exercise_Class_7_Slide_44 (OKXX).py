
# coding: utf-8

# In[ ]:


# Implemente o problema do produtor consumidor usando RLock ao inves de uma fila

from threading import Thread, Event
from queue import Queue
import time
import random

class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify: item Nº %d appended to queue by %s\n' % (item, self.name))
            time.sleep(1)

class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify: %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()
            
if __name__ == '__main__':
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t4 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()


# In[ ]:


from threading import Thread, Event
import time
import random

class producer(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        item = random.randint(0, 256)
        print('Producer notify: item Nº %d appended by %s\n' % (item, self.name))
        time.sleep(1)
        
class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify: %d popped by %s' % (item, self.name))
            
if __name__ == '__main__':
    t1 = producer()
    t2 = consumer()
    t3 = consumer()
    t4 = consumer()
    for i in range(10):
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()


# In[ ]:


from threading import Thread, Event
import time
import random

class Product(object):
    
    lock = threading.RLock()
    
    def __init__(self):
        self.total_items = 0
        
    def execute(self, n):
        Product.lock.acquire()
        self.total_items += n
        Product.lock.release()
        
    def append(self):
        Product.lock.acquire()
        self.execute(1)
        Product.lock.release()
        
    def pop(self):
        Product.lock.acquire()
        self.execute(-1)
        Product.lock.release()
        
def producer(product, items):
    while items > 0:
        print("Producer notify: item Nº %d appended by %s\n" % (item, self.name))
        product.append()
        time.sleep(1)
    
def consumer(product, items):
    while items > 0:
        print("Consumer notify: %d popped by %s" % (item, self.name))
        product.pop()
        time.sleep(1)
    
if __name__ == '__main__':
    
    items = 10
    product = Product()
    t1 = threading.Thread(target = producer, args = (product, items))
    t2 = threading.Thread(target = consumer, args = (product, items))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

