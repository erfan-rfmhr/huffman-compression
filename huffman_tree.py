import heapq
import os


class Node:
    def __init__(self, char: str, frequency: int) -> None:
        self.char = char
        self.frequency = frequency
        self.right = None
        self.left = None
        
class Huffman:
    def __init__(self) -> None:
        self.codes = {}
        self.priority_queue = []