class Node:
    def __init__(self, value: str, frequency: int) -> None:
        self.value = value
        self.frequency = frequency
        self.right = None
        self.left = None