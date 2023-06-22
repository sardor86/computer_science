class Stack:
    class Data:
        def __init__(self, data, old_data):
            self.data = data
            self.old_data = old_data

    def __init__(self):
        self.head = self.Data(None, None)

    def add(self, data):
        data = self.Data(data, self.head)
        self.head = data

    def get(self):
        return self.head.data

    def remove(self) -> None:
        if self.head.old_data is None:
            raise IndexError('list index out of range')
        self.head = self.head.old_data

    def __str__(self) -> str:
        return str(self.head.data)

    def __repr__(self) -> str:
        return str(self.head.data)
