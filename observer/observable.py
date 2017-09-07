""" Sample problem featuring the observer pattern. """

class Observable():
    """ Base class for observable events """

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        """ Subscribes an observer by adding it to the internal list """
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        """ Unsubscribes an observer by removing it from the internal list  """
        self._observers.remove(observer)

    def notify(self, arg=None):
        """ Sends a notification to each subscribed observer """
        for observer in self._observers:
            observer.notify(arg)
