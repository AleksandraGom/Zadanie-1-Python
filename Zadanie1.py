import time

a = float(input("Base length: "))
b = float(input("Base width: "))
h = float(input("Height: "))

area = 2 * a * b + 2 * b * h + 2 * a * h
volume = a * b * h

print("Area: ", area)
print("Volume: ", volume)

time.sleep(60)
