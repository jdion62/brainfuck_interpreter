class State:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.AST = None
        memory = [0]*30000
        dataIndex = 0

state = State()