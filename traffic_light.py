from enum import Enum, auto
import time

class State(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLightFSM:
    def __init__(self):
        self.state = State.RED

    def transition(self):
        if self.state == State.RED:
            self.state = State.GREEN
        elif self.state == State.GREEN:
            self.state = State.YELLOW
        elif self.state == State.YELLOW:
            self.state = State.RED

    def __str__(self):
        return f"Traffic Light is {self.state.name}"
