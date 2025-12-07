#Q1.
String = "Python"
new_string = "I am learning " + String
print(new_string)

#Q2.
name = "Aditi"
age = 20
txt = f"{name} is {age} years old"
print(txt)

#Q3.
fruit = "Mango"
price = 50.5
txt = f"{fruit} price is {price:.2f}"
print(txt)

#Q4
city = "Delhi"
print(f"{city:>10}")

#Q5
Quote = "Hello"
print(f"{Quote!r}")

#Q6 :Print: "Laptop costs ₹49,999.95" using f-string with comma formatting and 2 decimals.

item = "Laptop"
price = 49999.95
print("")

#Q7: Print: "Name: Kohli, Virat" using format() method (not f-string).
first = "Virat"
last = "Kohli"
print("Name: {}, {}".format(first,last))

#Q8 Print: "5 + 10 = 15" using f-string and expressionu inside {}. (No extra variables allowed for sum.)
x = 5
y = 10
print(f"{x} + {y} = {x+y} ")

#Q9: Convert to: "python" using formatting (no .lower() allowed).
