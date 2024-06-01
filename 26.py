temp=float(input("enter the temperature in centigrade:"))
if temp < 0:
    print("Freezing weather")
elif temp <= 10:
    print("very cold weather")    
elif temp <= 20:
    print("cold weather")    
elif temp <= 30:    
    print("normal in temperature")
elif temp <= 40:    
    print("it's hot")
else:
    print("it's very hot")    