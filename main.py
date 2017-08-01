#!/usr/bin/env python
""" Sample problem featuring the observer pattern. """

import argparse

from pizza_oven import PizzaOven
from sms_notification import SMSNotification
from observable import Observable
from observer import Observer

def main():
    """ Execute the program """
    args = parse_args()
    orderPizza(args.quantity)


    pizzaSquaredOven = PizzaOven()
    pizzaSquaredSubscriberSMS = SMSNotification()
    pizzaSquaredOven.pizzaStartedEvent.subscribe(pizzaSquaredSubscriberSMS)

    for x in range(0, int(args.quantity)):
        pizzaSquaredOven.pizzaStarted()
        pizzaSquaredOven.pizzaDone()
        pizzaSquaredSubscriberSMS.update(pizzaSquaredOven.pizzaStartedEvent)

    pizzaSquaredOven.pizzaStartedEvent.unsubscribe(pizzaSquaredSubscriber)

def orderPizza(quantity):
    print("Recorded a new pizza order: " + quantity)

def parse_args():
    """ Parse input arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q",
        "--quantity",
        help="The number of pizzas to order.",
        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    main()