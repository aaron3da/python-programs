import math

hours = float(input("Enter parking duration in hours: "))

if hours <= 0:
    print("Invalid parking duration")
elif hours <= 2:
    print("Parking fee: Rs. 30")
else:
    extra_hours = math.ceil(hours - 2)
    fee = 30 + extra_hours * 10
    print("Parking fee: Rs.", fee)
