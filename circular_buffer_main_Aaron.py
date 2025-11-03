# Program Description:
# Author: Aaron Moreno
# Date: November 2, 2025
"""
Test the CircularBuffer class by performing a series of operations.
"""

from circular_buffer import CircularBuffer

def add_all(cb):
    """
    Add all items currently in the buffer and return the sum.
    """
    total = 0
    for item in cb.get_buffer():
        if item is not None:
            total += item
    return total

def get_max_index(cb):
    """
    Return the index of the largest item in the buffer.
    """
    max_val = None
    max_index = -1
    for i, val in enumerate(cb.get_buffer()):
        if val is not None and (max_val is None or val > max_val):
            max_val = val
            max_index = i
    return max_index

def get_min_index(cb):
    """
    Return the index of the smallest item in the buffer.
    """
    min_val = None
    min_index = -1
    for i, val in enumerate(cb.get_buffer()):
        if val is not None and (min_val is None or val < min_val):
            min_val = val
            min_index = i
    return min_index

def main():
    """Main function to test the functionality of the CircularBuffer."""
    capacity = int(input("Enter Buffer Capacity: "))
    cb = CircularBuffer(capacity)

    print("1. Delete operation:")
    cb.delete()
    print("2. Add 15:")
    cb.add(15)
    print("Buffer:", cb)

    print("3. Add 5:")
    cb.add(5)
    print("Buffer:", cb)

    print("4. Delete operation:")
    cb.delete()
    print("Buffer:", cb)

    print("5. Add 3:")
    cb.add(3)
    print("Buffer:", cb)

    print("6. Add 26:")
    cb.add(26)
    print("Buffer:", cb)

    print("7. Delete operation:")
    cb.delete()
    print("Buffer:", cb)

    print("8. Add 76:")
    cb.add(76)
    print("Buffer:", cb)

    print("9. Add 105:")
    cb.add(105)
    print("Buffer:", cb)

    print("10. Search 48:")
    if cb.find(48):
        print("48 is in the buffer")
    else:
        print("48 is not in the buffer")

    print("11. Display items at first and last")
    first = cb.peek_first()
    last = cb.peek_last()
    print(f"{first} is the first item, and {last} is the last item")

    print("12. Add all items:")
    total = add_all(cb)
    print("Sum =", total)

    print("13. Locate the largest/smallest item")
    max_index = get_max_index(cb)
    min_index = get_min_index(cb)
    buffer = cb.get_buffer()
    print(f"The largest item = {buffer[max_index]} and the smallest item = {buffer[min_index]}")

    print("14. Clear the buffer")
    cb.clear()
    print(cb)

if __name__ == '__main__':
    main()
