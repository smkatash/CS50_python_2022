import sys

class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError("Negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.capacity < n:
            raise ValueError("Capacity exceeded.")
        if self.size + n > self.capacity:
            raise ValueError("Capacity exceeded.")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
             raise ValueError("Not enough cookies.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

if __name__ == "__main__":
    main()