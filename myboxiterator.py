class MyBoxIterator:
    def __init__(self, start=0):
        self.color = start

    def __iter__(self):
        return self

    def __next__(self):
        color = self.color
        self.color = 'red'
        return color
