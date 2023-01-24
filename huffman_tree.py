import heapq
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
        
    def __lt__(self, __o: object) -> bool:
        return self.frequency < __o.frequency
    
    def __eq__(self, __o: object) -> bool:
        return self.frequency == __o.frequency
        
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
    
    def __build_priority_queue(self, frequencies: Counter) -> None:
        # Iterate over the frequencies
        for char, frequency in frequencies.items():
            # Create a node
            node = Node(char, frequency)
            # Push the node into the priority queue
            heapq.heappush(self.__priority_queue, node)
            
    def __build_tree(self) -> None:
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
            # Check if node1 is less than node2 
            if node1 < node2:
                # Set the parent's left child to node1 and right child to node2
                parent.left = node1
                parent.right = node2
            # Otherwise 
            else: 
                # Set the parent's left child to node2 and right child to node1
                parent.left = node2
                parent.right = node1
            # Push the parent node back to the priority queue
            heapq.heappush(self.__priority_queue, parent)

        # Set the root as the only item left in the list
        self.__root = heapq.heappop(self.__priority_queue)

    def __find_codes(self, root: Node, current_code: str = '') -> None:
        # Stop the recursion when the given node is None
        if root is None:
            return
        # When the node's character is of length 1, assign that code to the dictionary
        if len(root.char) == 1:
            self.codes[root.char] = current_code
            return
        # Recursively call the method for the left subtree
        self.__find_codes(root.left, current_code + '0')
        # Recursively call the method for the right subtree
        self.__find_codes(root.right, current_code + '1')
        
    # Encoding text into bytes
    def encode_text(self, text: str) -> bytes:
        """This function encodes the given text into bytes using a given code. 
        
        This function first finds the frequency of each character in the given string, 
        builds a priority queue from the given frequencies and creates a tree from 
        that queue. After the tree is created, it finds the codes for each character
        and encodes the given text with the found codes.
        
        Params:
            text (str): The text to be encoded
        
        Returns:
            bytes: The encoded version of the given text
        """
        frequencies = self.find_frequencies(text)
        self.__build_priority_queue(frequencies)
        self.__build_tree()
        self.__find_codes(self.root)
        array = bytearray()
        num_of_codes = len(self.codes)
        array.append(num_of_codes)
        # Append the ordinal of each character
        for char, code in self.codes.items():
            array.append(ord(char))
            # Encode each character with a padding of 1
            code = '1' + code
            decimal_code = int(code, 2)
            array.append(decimal_code)
        # Append the encoded version of each character in the text    
        for char in text:
            padded_encoded_char = '1' + self.codes[char]
            array.append(int(padded_encoded_char, 2))
        return bytes(array)