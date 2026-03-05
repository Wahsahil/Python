#Create a program to convert the temperature of celcius into fahrenheit
def conver(cel):
    res = cel * (9/5) + 32
    print("Temperature in Fahrenheit:", res)

cel = float(input("Enter the temperature in Celsius: "))
conver(cel)
