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
            
    def make_tree(self) -> None:
        # Initialize the node variables
        node1: Node
        node2: Node
        # While the priority queue is not empty
        while len(self.__priority_queue) > 1:
            # Pop the two minimum values from the queue
            node1 = heapq.heappop(self.__priority_queue)
            node2 = heapq.heappop(self.__priority_queue)
            # Re-create the nodes' attributes to form the parent node
            parent_char = node1.char + node2.char
            parent_freq = node1.frequency + node2.frequency
            parent = Node(parent_char, parent_freq)
            # Push the parent node back to the priority queue
            heapq.heappush(self.__priority_queue, parent)

        # Set the root as the only item left in the list
        self.__root = heapq.heappop(self.__priority_queue)

    def find_codes(self, root: Node, code: str) -> None:
        # Stop the recursion when the given node is None
        if root is None:
            return
        # When the node's character is of length 1, assign that code to the dictionary
        if len(root.char) == 1:
            self.codes[root.char] = code
            return
        # Recursively call the method for the left subtree
        self.find_codes(root.left, code + "0")
        # Recursively call the method for the right subtree
        self.find_codes(root.right, code + "1")