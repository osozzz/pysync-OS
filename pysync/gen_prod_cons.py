import threading

class GenProdCons:
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Size must be > 0")
        self.size = size
        self.buffer = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def put(self, e):
        with self.not_full:
            while len(self.buffer) >= self.size:
                self.not_full.wait()
            self.buffer.append(e)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            self.not_full.notify()
            return item

    def __len__(self):
        with self.lock:
            return len(self.buffer)
