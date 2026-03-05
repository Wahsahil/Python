print("Enter the temperature")
temp = int(input())
if temp>50 and temp<60:
    print("Extereme Temperature")
elif temp>30 and temp <50:
    print("Hot temperature")
elif temp>18 and temp <24:
    print("Normal Temperature")
elif temp<18:
    print("To cold ")
else :
    print("invalid")