#Number and arithmetic in Python
spam_amount = 0
type(spam_amount)

type(19.95)
#True division
print(5 / 2)
print(6 / 2)
#Flooor division
print(5 // 2)
print(6 // 2)

#Order of operations
print(8 - 3 + 2)
print(-3 + 4 * 2)

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

#Builtin functions for working with numbers
print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)