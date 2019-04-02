# Traditional Approach
pow2 = []
for x in range(10):
   pow2.append(2 ** x)


# # list comprehension approach
pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# print(pow2)

## list comprehension with if statements
even_square = [x for x in range(50) if x%2 == 0]
# print(even_square)

list_of_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 

nested_list_comprehension = [i for x in list_of_list for i in x]
print(nested_list_comprehension)