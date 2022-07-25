from abc import ABC


class PlayerInterface(ABC):

    def __init__(self):
        pass


class HumanInterface(PlayerInterface):

    def __init__(self):
        super().__init__()


class AiInterface(PlayerInterface):

    def __init__(self):
        super().__init__()
