cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("\n")
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())