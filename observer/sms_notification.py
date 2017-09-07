""" Sample problem featuring the observer pattern. """

from observer import Observer

class SMSNotification(Observer):
    """ Sends an SMSM notification to a customer """

    def notify(self, arg):
        print("SMS notification: " + arg)
