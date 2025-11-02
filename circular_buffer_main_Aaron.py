# Program Description: Test program for CircularBuffer class
# Author: Aaron Moreno
# Date: 11-1-2025
"""
Test circular buffer class to perform data operations such as add, delete, search, peek, clear,
calculate sum, find max and min values, and display buffer contents.
"""

# Import CircularBuffer class
from circular_buffer import CircularBuffer

def add_all(cb):
    """
    Calculate and return the sum of all items in the circular buffer.
    
    Parameters:
    cb (CircularBuffer): The circular buffer object.
    
    Returns:
    int: Sum of all items in the buffer.
    """
    total = 0
    index = cb.get_head()
    for _ in range(cb.get_size()):
        total += cb.get_buffer()[index]
        index = (index + 1) % cb.get_capacity()
    return total

def get_max_index(cb):
    """
    Find the index of the largest item in the circular buffer.
    
    Parameters:
    cb (CircularBuffer): The circular buffer object.
    
    Returns:
    int: Index of the largest item in the buffer.
    """
    max_val = float('-inf')
    max_index = -1
    index = cb.get_head()
    for _ in range(cb.get_size()):
        if cb.get_buffer()[index] > max_val:
            max_val = cb.get_buffer()[index]
            max_index = index
        index = (index + 1) % cb.get_capacity()
    return max_index

def get_min_index(cb):
    """
    Find the index of the smallest item in the circular buffer.
    
    Parameters:
    cb (CircularBuffer): The circular buffer object.
    
    Returns:
    int: Index of the smallest item in the buffer.
    """
    min_val = float('inf')
    min_index = -1
    index = cb.get_head()
    for _ in range(cb.get_size()):
        if cb.get_buffer()[index] < min_val:
            min_val = cb.get_buffer()[index]
            min_index = index
        index = (index + 1) % cb.get_capacity()
    return min_index

def main():
    """Main function to test the functionality of the CircularBuffer class."""
    
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
    found = cb.find(48)
    print("48 is in the buffer" if found else "48 is not in the buffer")
    
    print("11. Display items at first and last")
    first = cb.peek_first()
    last = cb.peek_last()
    print(f"{first} is the first item, and {last} is the last item")
    
    print("12. Add all items:")
    total_sum = add_all(cb)
    print("Sum =", total_sum)
    
    print("13. Locate the largest/smallest item")
    max_index = get_max_index(cb)
    min_index = get_min_index(cb)
    print(f"The largest item = {cb.get_buffer()[max_index]} and the smallest item = {cb.get_buffer()[min_index]}")
    
    print("14. Clear the buffer")
    cb.clear()
    print(cb)

if __name__ == '__main__':
    main()
