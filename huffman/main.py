from algorithms_python.huffman.huffman import HuffmanCoding

if __name__ == "__main__":
    path = 'python_5th_edition.txt'
    huffman_code = HuffmanCoding(path)

    output_path = huffman_code.compress()
    huffman_code.decompress(output_path)
