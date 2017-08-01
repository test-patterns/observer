""" Sample problem featuring the observer pattern. """

from observer import Observer

class SMSNotification(Observer):
    def notify(observable, arg):
        print("SMS notification sent to customer")