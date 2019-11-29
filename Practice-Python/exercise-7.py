"""
Learning Outcomes:
1.List Comprehensions
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [element for element in a if element % 2 == 0]   #This is special!!!

print(b)
