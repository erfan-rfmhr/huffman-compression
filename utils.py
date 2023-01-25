from huffman_tree import Huffman

# * Functions for compressing

# Read a file and return the content in a string
def read_original_file(path: str) -> str:
    # Open file with 'r' flag
    with open(path, 'r') as file:
        # Read contents and return
        return file.read()

    
# Write processed file to destination
def write_decompressed_file(path: str, data: str) -> None:
    # Open file with 'w' flag
    with open(path, 'w') as file:
        # Write data to file
        file.write(data)
    
    
# Write compressed data to file
def write_cmp_file(path: str, data: bytes) -> None:
    # Open file with 'wb' flag
    with open(path, 'wb') as file:
        # Write data to file
        file.write(data)        


# Compress a file using Huffman encoding
def compress(origin_path: str = "/home/erfan/Desktop/huffman-compression/sample.txt",
             cmp_path: str = "/home/erfan/Desktop/huffman-compression/sample.cmp") -> None:
    # Read file content as string
    file_text = read_original_file(origin_path)
    # Construct Huffman tree
    tree = Huffman()
    # Encode file text using Huffman encoding
    encoded_text = tree.encode_text(file_text)
    # Write encoded data to file
    write_cmp_file(cmp_path, encoded_text) 
    
    
# * Functions for decompressing

# Remove padding from encoded text
def remove_padding(padded_encoded_text: str):
    # Get padding bit length from first 8 characters
    padded_info = padded_encoded_text[:8]
    # Convert bit length to integer
    extra_padding = int(padded_info, 2)
    # Remove padding info from encoded text
    padded_encoded_text = padded_encoded_text[8:] 
    # Remove extra padding
    encoded_text = padded_encoded_text[:-1*extra_padding]
    # Return encoded text
    return encoded_text
   
 
# Read an encoded file and return as bit string
def read_cmp_file(path: str) -> str:
    # Open file in binary
    with open(path, 'rb') as file:
        # Initials empty bit string
        bit_string = ""
        # Read single byte from file
        byte = file.read(1)
        # Keep reading bytes until EOF
        while(len(byte) > 0):
            # Get byte as integer
            byte = ord(byte)
            # Convert byte to bit string
            bits = bin(byte)[2:].rjust(8, '0')
            # Append bit string
            bit_string += bits
            # Read next byte
            byte = file.read(1)
    # Return bit string
    return bit_string    

 
# Decompress a file using Huffman encoding
def decompress(cmp_path: str = "/home/erfan/Desktop/huffman-compression/sample.cmp",
               decmp_path: str = "/home/erfan/Desktop/huffman-compression/dcmp_sample.txt") -> None:
    # Read file content as bit string
    bit_string = read_cmp_file(cmp_path)
    # Remove padding from encoded text
    encoded_text = remove_padding(bit_string)
    # Get number of characters from next 8 bits
    num_of_chars = int(encoded_text[:8], 2)
    # Remove number of characters bits from encoded text
    encoded_text = encoded_text[8:]
    # Initialise empty frequencies dict
    frequencies = {}
    # Extract character frequency pairs
    for _ in range(num_of_chars):
        # Get character bit length from next 8 bits
        char_bits_len = encoded_text[:8]
        char_bits_len = int(char_bits_len, 2)
        # Get character bit string from next calculated no. of bits
        char_bits = encoded_text[8:8+char_bits_len]
        # Remove character bits from encoded text
        encoded_text = encoded_text[8+char_bits_len:]
        # Get frequency bit length from next 8 bits
        freq_bits_len = encoded_text[:8]
        freq_bits_len = int(freq_bits_len, 2)
        # Get frequency bit string from next calculated no. of bits
        freq_bits = encoded_text[8:8+freq_bits_len]
        # Remove frequency bits from encoded text
        encoded_text = encoded_text[8+freq_bits_len:]
        # Convert character bits to integer
        char_ord = int(char_bits, 2)
        # Get character from integer 
        char = chr(char_ord)
        # Convert frequency bits to integer
        freq = int(freq_bits, 2)
        # Add character, frequency pair to frequencies dict
        frequencies[char] = freq
    # Get Huffman tree for frequencies
    tree = Huffman()
    # Decode encoded text and reconstruct original text
    origin_text = tree.decode_text(encoded_text, frequencies)
    # Write decompressed text to file
    write_decompressed_file(decmp_path, origin_text)