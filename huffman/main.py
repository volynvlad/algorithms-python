import sys

from huffman import HuffmanCoding

if __name__ == "__main__":
    if len(sys.argv) == 2:
        huffman_code = HuffmanCoding(sys.argv[1])

        output_path = huffman_code.compress()
        huffman_code.decompress(output_path)
