userInput1= float(input("Enter the currency in INR =>"))
userInput2=str(input("Enter the convertable currency =>"))
if (userInput2.upper() == "USD"):
 print(f"{0.012 * userInput1} USD")
elif (userInput2.upper() == "JPY"):
 print(f"{1.74 * userInput1} JPY")
elif (userInput2.upper() == "SGD"):
 print(f"{0.015 * userInput1} SGD")
elif (userInput2.upper() == "AED"):
 print(f"{0.042 * userInput1} AED")
elif (userInput2.upper() == "EURO"):
 print(f"{0.011 * userInput1} Euro")
else:
 print("No valid input")
 