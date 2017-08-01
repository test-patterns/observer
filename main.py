#!/usr/bin/env python
""" Sample problem featuring the observer pattern. """

import argparse

from pizza_oven import PizzaOven
from sms_notification import SMSNotification

def main():
    """ Execute the program """
    args = parse_args()
    pizza_oven = PizzaOven()
    pizza_sms_notification = SMSNotification()
    pizza_oven.pizza_started_event.subscribe(pizza_sms_notification)
    for _ in range(int(args.quantity)):
        pizza_oven.make_pizza()
    pizza_oven.pizza_started_event.unsubscribe(pizza_sms_notification)

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
