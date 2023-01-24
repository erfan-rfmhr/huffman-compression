from huffman_tree import Huffman


def compress(input_path: str = "/home/erfan/Desktop/huffman-compression/sample.txt", output_path: str = "/home/erfan/Desktop/huffman-compression/sample.cmp") -> None:
    with open(input_path, 'r') as reader:
        file_text = reader.read()
    tree = Huffman()
    encoded_text = tree.encode_text(file_text)
    with open(output_path, 'wb') as writer:
        writer.write(encoded_text)