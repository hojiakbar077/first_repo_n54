# --------Python Sequence Types-------- #

# String
string_example = "Hello, World!"
print("String Example:", string_example)
print("First character:", string_example[0])
print("Slice [7:12]:", string_example[7:12])
print("Reversed string:", string_example[::-1])

# List
list_example = [10, 20, 30, 40, 50]
print("\nList Example:", list_example)
print("First element:", list_example[0])
print("Slice [1:4]:", list_example[1:4])
list_example.append(60)
print("After appending 60:", list_example)
list_example[2] = 35
print("After modifying third element:", list_example)

# Tuple
tuple_example = (100, 200, 300, 400, 500)
print("\nTuple Example:", tuple_example)
print("First element:", tuple_example[0])
print("Slice [1:4]:", tuple_example[1:4])

# Range
range_example = range(1, 10, 2)
print("\nRange Example:", list(range_example))
print("First element:", range_example[0])
print("Slice [1:3]:", list(range_example)[1:3])

# Byte Sequence
byte_example = b"Hello"
print("\nByte Example:", byte_example)
print("First byte:", byte_example[0])
print("Slice [1:4]:", byte_example[1:4])

# Bytearray
bytearray_example = bytearray(b"Hello")
print("\nBytearray Example:", bytearray_example)
print("First byte:", bytearray_example[0])
bytearray_example[1] = ord(b"a")
print("After modifying second byte:", bytearray_example)

# Memoryview
memoryview_example = memoryview(bytearray_example)
print("\nMemoryview Example:", memoryview_example)
print("First byte:", memoryview_example[0])
print("Slice [1:4]:", memoryview_example[1:4].tobytes())
