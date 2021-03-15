tempincelsius = input("Please enter a temperature in celsius...")
# print(tempincelsius)
# print(type(tempincelsius))

tempinfahrenheit = float (tempincelsius) * 1.8 + 32
# print(tempfahrenhit)
# print(type(tempfahrenhit))

roundedF = round(tempinfahrenheit, 2)
#still a float!

print(tempincelsius + " degrees celsius is " + str(roundedF) + " degrees fahrenheit.")
