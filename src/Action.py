

class Action(object):

    def __init__(self, name, nextFunction):
        self.name = name
        self.nextFunction = nextFunction
        pass

    def next(self, currentState):
        return self.nextFunction(currentState)