//shipping cost calculator 

//input the package weight and shipping rate 

weight = float(input("Enter wight in kilograms"))
rate = float(input("Enter shipping rate per kg"))

shipping_cost = weight*rate

print(f"SHipping Cost : {shipping_cost} USD")
