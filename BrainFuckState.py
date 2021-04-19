class State:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.AST = None
        self.memory = [0]*30000
        self.dataIndex = 0
        self.instructionIndex = 0

state = State()