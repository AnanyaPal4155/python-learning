#Q1
from enum import unique
import numbers
from operator import truediv
from tokenize import Number


data = [[10, 20], [30, 40, 50], [60]]
data[1][1] = 400
print(data)

#Q2
nums = [9, 1, 6, 4, 8, 2]
nums.sort(reverse=True)
print(nums)

#Q3
numbers = []
for i in range(1,6):
  numbers.append(i)
print(numbers)

number = [i for i in range(1,6) ]
print(number)

#Q4
names = ["Aman", "Karan", "Neha", "Rohan", "Simran"]
names.insert(3,"Python")
print(names)

#Q5
x = [10, 20, 30, 40, 50, 60]
del x[0:3]
print(x)

#Q6
new= []
for x in [1,2,3]:
  new.append(x*2)
print(new)

new = [i*2 for i in [1,2,3]]
print(new)

#Q7
even= []
for x in range(1,11):
  if x % 2 == 0:
    even.append(x)
print(even)

evens = [x for x in range(1,11) if x % 2 == 0 ]
print(even)

#Q8
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
first_col = []
for row in matrix:
  first_col.append(row[0])

first_col = [row[0] for row in matrix]

#Q9:
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
 squares.append(x*x)
print(squares)

nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]
print(squares)

#Q10
nums = [3, 6, 9, 12]
squares = [x*x for x in nums]
print(squares)

#Q1.
nums = [10, 20, 30, 40, 50]
print(nums[3],nums[4])

#Q2:Remove last element from the list without usings index
num = [10, 20, 30, 40, 50]
num.pop()
print(num)

#Q3:Append operation test: Make a Empty list → 3 values user se input lekar list me add karo.

data = []

for i in range(3):
    value = input("Enter value:")
    data.append(value)

print(data)

#Q4:
numbers = []
total = 0
for i in range(5):
  values = int(input("Enter numbers:"))
  numbers.append(values)
  total += values
print("Numbers:", numbers)
print("Total =", total)

# second way best choice
numbers = []
for i in range(5):
    numbers.append(int(input("Enter a number:")))

print("Numbers:", numbers)
print("Total =",sum(numbers))

#Q5:
even_numbers = []
total_even = 0

for i in range(5):
    value = int(input("Enter number: "))
    if value % 2 == 0:
        even_numbers.append(value)
        total_even += value

print("Even Numbers:", even_numbers)
print("Total Even =", total_even)

#Q6:
odd_numbers = []
total_odd = 0

for i in range(7):
    value = int(input("Enter Number"))
    if value % 2 != 0:
      odd_numbers.append(value)
      total_odd += value

odd_numbers.sort(reverse=True)
print("Odd Numbers (sorted):", odd_numbers)
print("Total Odd =", total_odd)

 # another way to solve
numbers = [int(input("Enter Number: ")) for _ in range(7)]

odd_numbers = sorted([n for n in numbers if n % 2 != 0], reverse=True)
total_odd = sum(n for n in numbers if n % 2 != 0)

print("Odd Numbers (sorted):", odd_numbers)
print("Total Odd =", total_odd)

#Q6:Count occurrences of "banana" without .count()

fruits = ["apple", "banana", "mango", "banana", "grapes"]
count = 0

for fruit in fruits:
   if fruit == "banana":
     count +=1
print("Banana appears:", count)

#Q7: Reverse a list without .reverse() or slicing

lst = [1, 2, 3, 4, 5]
reversed_lst = []

for i in range(len(lst)-1,-1, -1):
    reversed_lst.append(lst[i])

print("Reversed lst:", reversed_lst)

#Q8:Max & Min without max() & min()
marks = [22, 45, 78, 12, 90, 56]

max_val = marks[0]
min_val = marks[0]

for mark in marks:
    if mark > max_val:
        max_val = mark
    if mark < min_val:
        min_val = mark

print("Max:", max_val)
print("Min:", min_val)

# Q8: Even / Odd filter
numbers = [10, 23, 45, 66, 77, 88]
evens = []
odds = []

for n in numbers:
   if n % 2 == 0:
     evens.append(n)
   else:
     odds.append(n)

print("Even:", evens)
print("Odd:", odds)

# Q9: Duplicate removal (order preserve, set() not allowed)

data = [1, 2, 3, 2, 4, 3, 5]
unique = []

for item in data:
    if item not in unique:
        unique.append(item)

print("Unique list:", unique)

#Q10: Swap first and last element
lst = [10, 20, 30, 40]
lst[0], lst[-1] = lst[-1], lst[0]
print("After swap:", lst)

#Q11: Replace "c" with "C" safely

names = ["a", "b", "c", "d"]

for i in range(len(names)):
    if names[i] == "c":
       names[i] = "C"
       break # first occurrence only
print("Updated list:", names)

#Q12: Sum of list elements without sum()
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n

print("Total sum:", total)

#Q13: Two lists match check element-wise (no ==)

a = [1,2,3]
b = [1,2,3]

if len(a) != len(b):
   print("Not equal")  # Agar size alag hai → compare karne ka koi fayda nahi. [1,2,3] vs [1,2,3,4]  ❌
else:
    equal = True
    for i in range(len(a)):
        if a[i] != b[i]:
            equal = False
            break
print("Lists are equal" if equal else "Lists are not equal")

#Q14: Sorted copy without touching original

original = [5, 2, 9, 1]
sorted_copy = []

for n in original:
    sorted_copy.append(n)
