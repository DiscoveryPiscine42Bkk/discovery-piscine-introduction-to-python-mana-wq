# play_with_arrays.py
original_array = [1, 3, 5, 7, 9]
new_array = [x + 2 for x in original_array if x + 2 > 5]
print("original array:",original_array)
print("new array (each element +2 and  >5)",new_array)