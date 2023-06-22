class Queue:
    class Data:
        def __init__(self, data, old_data):
            self.data = data
            self.old_data = old_data

    def __init__(self):
        self.head = self.Data(None, None)
        self.size = 0

    def add(self, data):
        old_data = self.head

        for this_data in range(self.size):
            old_data = old_data.old_data

        old_data.old_data = self.Data(data, None)

        self.size += 1

    def get(self):
        return self.head.old_data.data

    def remove(self) -> None:
        if self.size <= 0:
            raise IndexError('list index out of range')

        self.head = self.head.old_data
        self.size -= 1

    def __str__(self):
        return self.head.old_data.data

    def __repr__(self):
        return self.head.old_data.data
