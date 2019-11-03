class Bucket:        
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "Bucket[key: {}, value: {}]".format(self.key, self.value)

    def __call__(self):
        return self