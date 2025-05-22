import threading

class RendezvousDEchange:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.has_first = False
        self.first_value = None
        self.second_value = None

    def echanger(self, value):
        with self.condition:
            if not self.has_first:
                self.first_value = value
                self.has_first = True
                self.condition.wait()
                result = self.second_value
                self.condition.notify()
                return result
            else:
                self.second_value = value
                self.has_first = False
                self.condition.notify()
                self.condition.wait()
                return self.first_value
