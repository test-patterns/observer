""" Sample problem featuring the observer pattern. """

from observable import Observable

class PizzaOven():
    """ An oven that makes pizzas """
    def __init__(self):
        self.pizza_started_event = PizzaOven.PizzaStartedEvent()
        self.pizza_done_event = PizzaOven.PizzaDoneEvent()

    def make_pizza(self):
        """ Makes a pizza """
        self.pizza_started()
        # wait
        self.pizza_done()

    def pizza_started(self):
        """ Called when a pizza is started """
        self.pizza_started_event.notify("The pizza just started cooking")

    def pizza_done(self):
        """ Called when a pizza is done """
        self.pizza_done_event.notify("The pizza is done")

    class PizzaStartedEvent(Observable):
        """ An observable pizza start event """
        def __init__(self):
            Observable.__init__(self)

    class PizzaDoneEvent(Observable):
        """ An observable pizza done event """
        def __init__(self):
            Observable.__init__(self)
