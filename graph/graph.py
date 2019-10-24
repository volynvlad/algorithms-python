class Graph:

    class Node:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.neighbors = []


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    
    