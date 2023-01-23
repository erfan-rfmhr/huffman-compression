import heapq
import os


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
    def priority_queue(self):
        # Returns the priority queue
        # It does'nt have setter
        return self.__priority_queue
    
    @property
    def root(self):
        # Returns the root node
        # It does'nt have setter
        return self.__root
    
    