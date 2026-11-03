# Week 1 practice task: unit converter (model solution).
# Uses only variables, input(), float(), round(), arithmetic and print().

kilometres = float(input("Enter a distance in kilometres: "))
miles = kilometres * 0.621371

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(kilometres, "km is", round(miles, 2), "miles")
print(celsius, "C is", round(fahrenheit, 2), "F")
