""" Sample problem featuring the command pattern. """

import unittest

from test_context import PizzaOven

class TestPizzaOven(unittest.TestCase):
    """ Tests the PizzaOven class """

    def test_init(self):
        """ Tests the constructor of the PizzaOven class """
        test_pizza_oven = PizzaOven()
        self.assertEqual(type(test_pizza_oven.pizza_started_event), PizzaOven.PizzaStartedEvent)
        self.assertEqual(type(test_pizza_oven.pizza_done_event), PizzaOven.PizzaDoneEvent)

if __name__ == '__main__':
    unittest.main()
