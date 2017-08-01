""" Sample problem featuring the observer pattern. """

class Observable():
    def _init_(self):
        self.observers = []

    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, arg=None):
        for observer in self.observers:
            observer.notify(self, arg)