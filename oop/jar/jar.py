class Jar:
    def __init__(self,capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid Input")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if n <= self.capacity and n + self.size <= self.capacity:
            self._size += n
        else:
             raise ValueError("Out of capacity")

    def withdraw(self, n):
        if n <= self.size:
            self._size -= n
        else:
            raise ValueError("Invalid")
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
