# play_with_arrays.py
original_array = [1, 5, 9, 7, 9, -11, 13, 5, 7,]
new_array = [x + 2 for x in original_array if x + 2 > 5]
print(original_array)
print(new_array)