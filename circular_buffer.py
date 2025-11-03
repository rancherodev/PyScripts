# Program Description:
# Author: Aaron Moreno
# Date: November 2, 2025
"""
Create a CircularBuffer class to perform data operations such as add, delete, search,
peek, and clear using a queue-based circular structure.
"""

class CircularBuffer:
    """Implements a fixed-size circular buffer (queue-like data structure)."""

    def __init__(self, capacity):
        """
        Initialize the circular buffer with the given capacity.
        Each position is initialized to None.
        """
        self.__capacity = capacity
        self.__size = 0
        self.__buffer = [None] * capacity
        self.__head = 0
        self.__tail = 0

    # ---------------------- Getters / Setter ----------------------

    def get_capacity(self):
        """Return the maximum capacity of the buffer."""
        return self.__capacity

    def set_capacity(self, capacity):
        """Set a new capacity (not typically used in fixed-size buffers)."""
        self.__capacity = capacity

    def get_buffer(self):
        """Return the internal buffer list."""
        return self.__buffer

    def get_head(self):
        """Return the current head index."""
        return self.__head

    def get_tail(self):
        """Return the current tail index."""
        return self.__tail

    def get_size(self):
        """Return the current number of items in the buffer."""
        return self.__size

    # ---------------------- Core Methods ----------------------

    def add(self, item):
        """
        Insert an item at the tail position.
        If the buffer is full, overwrite the oldest item.
        """
        self.__buffer[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity

        # If overwriting (buffer full), move head forward
        if self.__size == self.__capacity:
            self.__head = (self.__head + 1) % self.__capacity
        else:
            self.__size += 1

    def delete(self):
        """
        Delete the item at the head position and return it.
        Display an error if the buffer is empty.
        """
        if self.is_empty():
            print("Buffer is empty")
            return None
        deleted_item = self.__buffer[self.__head]
        self.__buffer[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        print(f"{deleted_item} has been deleted")
        return deleted_item

    def clear(self):
        """Reset the buffer and indices."""
        self.__buffer = [None] * self.__capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        """Return True if buffer is empty."""
        return self.__size == 0

    def peek_first(self):
        """Return the first (oldest) item in the buffer."""
        if self.is_empty():
            return None
        return self.__buffer[self.__head]

    def peek_last(self):
        """Return the last (newest) item in the buffer."""
        if self.is_empty():
            return None
        last_index = (self.__tail - 1 + self.__capacity) % self.__capacity
        return self.__buffer[last_index]

    def find(self, item):
        """Return True if item exists in the buffer."""
        return item in [x for x in self.__buffer if x is not None]

    def __str__(self):
        """Display buffer items from head to tail in readable order."""
        if self.is_empty():
            return "Buffer is empty"
        items = []
        idx = self.__head
        for _ in range(self.__size):
            items.append(str(self.__buffer[idx]))
            idx = (idx + 1) % self.__capacity
        return " --> ".join(items)
