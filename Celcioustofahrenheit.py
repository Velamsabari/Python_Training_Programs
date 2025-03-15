#celcious to fahrenheit conversion
celcious = input("Enter the celcious value : \n")
celValue = float(celcious)
fahrenheit = celValue*(9/5) + 32
print(f"The fahrenheit value of given celcious value is: {fahrenheit}")

#Fahrenheit to celcious conversion
fahrenheit = input("Enter the fahrenheit value : \n")
farValue = float(fahrenheit)
celcious = (farValue - 32)*(5/9)
print(f"The celcious value of given fahrenheit value is: {celcious}")
