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
        # Initialize the dictionary of codes for encoding
        self.__codes = {}
        # Initialize the dictionary of reverse mapping for decoding
        self.__reverse_mapping = {}
        # Initialize the priority queue
        self.__priority_queue = []
        # Initialize the counter of frequencies
        self.__frequencies = Counter()
        # Initialize the root node
        self.__root = None
            
    
    def __find_frequencies(self, text: str) -> None:
        # Update the frequencies with the given text
        self.__frequencies.update(text)
    
    
    def __build_priority_queue(self) -> None:
        # Iterate over the frequencies
        for char, frequency in self.__frequencies.items():
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
            self.__codes[root.char] = current_code
            return
        # Recursively call the method for the left subtree
        self.__find_codes(root.left, current_code + '0')
        # Recursively call the method for the right subtree
        self.__find_codes(root.right, current_code + '1')
        
        
    def __build_reverse_mapping(self, root: Node, current_code: str = '') -> None:
        # Stop the recursion when the given node is None
        if root is None:
            return
        # When the node's character is of length 1, assign that code to the dictionary
        if len(root.char) == 1:
            self.__reverse_mapping[current_code] = root.char
            return
        # Recursively call the method for the left subtree
        self.__build_reverse_mapping(root.left, current_code + '0')
        # Recursively call the method for the right subtree
        self.__build_reverse_mapping(root.right, current_code + '1')
        
        
    def encode_text(self, text) -> bytes:
        """Encodes the given text using Huffman encoding.
        
        Params:
            text (str): The text to encode.
        
        Returns:
            bytes: The encoded text.
        """
        # Initialize the encoded text string
        encoded_text = ''

        # Count the frequencies of characters in the text
        self.__find_frequencies(text)

        # Create a priority queue of tuples representing
        # the characters and their frequencies
        self.__build_priority_queue()

        # Build the Huffman tree using the priority queue
        self.__build_tree()

        # Calculate the Huffman codes
        self.__find_codes(self.__root)

        # Create a bytearray object to store the encoded output
        array = bytearray()

        # Calculate the number of characters (codes)
        num_of_chars = len(self.__frequencies)

        # Encode the number of codes
        encoded_text += f"{num_of_chars:08b}"

        # Encode the character codes and their respective frequencies
        for char, freq in self.__frequencies.items():
            bin_char = bin(ord(char))[2:]
            bin_freq = bin(freq)[2:]
            encoded_text += f"{len(bin_char):08b}" + bin_char + f"{len(bin_freq):08b}" + bin_freq 

        # Encode the characters in the original text
        for char in text:
            encoded_text += self.__codes[char]

        # Pad out the encoded text to a multiple of 8 bits
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        # Store the padding information at the beginning of the encoded text
        padded_info = f"{extra_padding:08b}"
        encoded_text = padded_info + encoded_text
        # Convert the encoded text to bytes
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            array.append(int(byte, 2))

        # Return the bytes object
        return bytes(array)


    def decode_text(self, encoded_text: str, frequencies: dict) -> str:
        """Decodes the given text using Huffman encoding.
        
        Params:
            encoded_text (str): The encoded text to decode.
            frequencies (dict): The frequencies of characters in the original text.
        
        Returns:
            str: The decoded text.
        """
        # Set the frequencies attribute using the provided dictionary
        self.__frequencies = frequencies

        # Create the priority queue and Huffman tree    
        self.__build_priority_queue()
        self.__build_tree()

        # Create a reverse mapping of characters and bit strings
        self.__build_reverse_mapping(self.__root)
        # Initialise a string to store the current bit string
        bit_string = ""
        # Initialise a string to store the decoded text
        decoded_text = ""

        # Iterate through the encoded text
        for bit in encoded_text:
            # Append each bit to the bit string
            bit_string += bit
            # If the current bit string matches a character in the reverse mapping
            if bit_string in self.__reverse_mapping:
                # Add the character it matches to the decoded text
                decoded_text += self.__reverse_mapping[bit_string]
                # Reset the bit string
                bit_string = ""

        # Return the decoded text
        return decoded_text