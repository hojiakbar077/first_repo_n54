
my_list = [1, 2, 3, 4, 5]           
my_tuple = (1, 2, 3, 4, 5)           
my_string = "Hello, World!"          
my_range = range(1, 6)               

print("List:", my_list)
print("Tuple:", my_tuple)
print("String:", my_string)
print("Range:", list(my_range))

for seq in [my_list, my_tuple, my_string, list(my_range)]:
    print(f"\nSequence: {seq}")
    print("Length:", len(seq))          
    print("First element:", seq[0])     
    print("Last element:", seq[-1])     
    print("Sliced sequence (1:4):", seq[1:4])
