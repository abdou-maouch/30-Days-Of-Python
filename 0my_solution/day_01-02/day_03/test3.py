age = 21
height = 6.1
next_year_age = age + 1

# input() always returns a string
base = float(input("Enter base: "))
tri_height = float(input("Enter height: "))
print("The area of the triangle is", 0.5 * base * tri_height)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("The perimeter of the triangle is", a + b + c)

length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("The area of the rectangle is", length * width)

print(len("python") == len("dragon"))
print("on" in "python" and "on" in "dragon")
print("on" not in "python" and "on" not in "dragon")

x = len("python")
print(x)
print(float(x))
print(str(x))

n = int(input("Enter a number: "))
print("The number is even." if n % 2 == 0 else "The number is odd.")

print(type(10) == type("10"))
print(type(9.8) == type(10))

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is:", hours * rate)

for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)