""" Sample problem featuring the observer pattern. """

class Observer():
    """ An interface for event observers """

    def notify(self, arg):
        """ Base method to send a notification """
        raise NotImplementedError
