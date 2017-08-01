class Customer():
    def __init__(self, name):
        self.name = name
        self

    class StartObserver(Observer):
        def update(self, observable, arg):
            print(self.name + "pizza just started cooking!")

