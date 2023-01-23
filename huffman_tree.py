import heapq
import os
from collections import Counter


class Node:
    def __init__(self, char: str, frequency: int) -> None:
        # Initializes the character
        self.char = char
        # Initializes the frequency
        self.frequency = frequency
        # Initializes the pointer to the right subtree
        self.right = None
        # Initializes the pointer to the left subtree
        self.left = None
        
class Huffman:
    def __init__(self) -> None:
        # Initialize the dictionary of codes
        self.__codes = {}
        # Initialize the priority queue
        self.__priority_queue = []
        # Initialize the root node
        self.__root = None
        
    @property
    def codes(self):
        # Returns the dictionary of codes
        # It does'nt have setter
        return self.__codes
        
    @property
    def root(self):
        # Returns the root node
        # It does'nt have setter
        return self.__root
    
    
    @staticmethod
    def find_frequencies(text: str) -> Counter:
        # Initialize a Counter
        frequencies = Counter()
        # Update the frequencies with the given text
        frequencies.update(text)
        # Returns the frequencies
        return frequencies
    
    def build_priority_queue(self, frequencies: Counter) -> None:
        # Iterate over the frequencies
        for char, frequency in frequencies.items():
            # Create a node
            node = Node(char, frequency)
            # Push the node into the priority queue
            heapq.heappush(self.__priority_queue, node)