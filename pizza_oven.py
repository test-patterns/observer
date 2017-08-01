""" Sample problem featuring the observer pattern. """

from observable import Observable

class PizzaOven():
    def __init__(self):
        self.pizzaStartedEvent = PizzaOven.PizzaStartedEvent()
        self.pizzaDoneEvent = PizzaOven.PizzaDoneEvent()

    def pizzaStarted(self):
        self.pizzaStartedEvent.notify("The pizza just started cooking")

    def pizzaDone(self):
        self.pizzaDoneEvent.notify("The pizza is done")

    def make_pizza(self):
        self.pizzaStarted()
        self.pizzaDone()

    class PizzaStartedEvent(Observable):
        def __init__(self):
            Observable.__init__(self)

    class PizzaDoneEvent(Observable):
        def __init__(self):
            Observable.__init__(self)