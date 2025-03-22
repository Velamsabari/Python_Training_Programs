#Qn1:Write Python code to create a string variable containing your name and another string variable containing your age as a string. Then concatenate them with appropriate spacing to form a complete sentence.

name = "Velam"
age = "30"
print(f"My name is {name} and I am {age} years old")

"""Qn-2: Given the sets A = {1, 3, 5, 7, 9} and B = {2, 3, 5, 7}, write the Python code to find:
   * The union of sets A and B
   * The intersection of sets A and B
   * The difference A - B
   * The difference B - A """
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7}
D = A.union(B)
print(D)
E = A.intersection(B)
print(E)
F = A.difference(B)
print(F)
G = B.difference(A)
print(G)
#Qn:3 - Write Python code to create a new list containing only the even numbers from the original list data = [10, 21, 32, 43, 54, 65, 76]
data = [10,21,32,43,54,65,76]
for x in data:
 if(x % 2 == 0):
  print(x)

"""Qn:4 For the nested list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write code to:
   * Access the element at the second row and third column
   * Extract the second row as a list
   * Create a new list containing the first element of each nested list"""
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]
print(matrix[1][2])
print(matrix[2])
newList = matrix[0][0], matrix[1][0],matrix[2][0]
print(newList)

"""QN-5 - Given names = ["Alice", "Bob", "Charlie", "David"], show the Python code to:
   * Reverse the list in-place
   * Create a new list with names sorted alphabetically
   * Modify the original list to have all names in uppercase"""
names = ["Bob","Alice", "Charlie", "David"]
print(names[::-1])
print(names)
names.sort()
print(names)
for x in names:
 print(x.upper())
