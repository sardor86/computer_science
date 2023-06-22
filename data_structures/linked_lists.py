class LinkedLists:
    class Data:
        def __init__(self, data, next_data):
            self.data = data
            self.next_data = next_data

    def __init__(self):
        self.head = self.Data(None, None)
        self.size = 0

    def add(self, data):
        old_data = self.head

        for this_data in range(self.size):
            old_data = old_data.next_data

        old_data.next_data = self.Data(data, None)

        self.size += 1

    def check_index(self, index: int) -> None:
        if index >= self.size:
            raise IndexError('list index out of range')

    def get(self, index: int):
        self.check_index(index)

        data = self.head

        for _ in range(index + 1):
            data = data.next_data

        return data.data

    def remove(self, index: int) -> None:
        self.check_index(index)

        data = self.head

        for index_number in range(self.size):
            old_data = data
            data = data.next_data

            if index_number == index:
                old_data.next_data = data.next_data

        self.size -= 1

    def __str__(self) -> str:
        list_str = '[ '

        data = self.head

        for _ in range(self.size - 1):
            data = data.next_data
            list_str += f'{data.data}, '

        return list_str + ' ]'
