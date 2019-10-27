import hash

if __name__ == "__main__":
    size = 101
    hash1 = hash.Hash(size)

    for i in range(size):
        hash1.set(i, i * i)

    
