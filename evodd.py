def classify_number(num):
    if num > 0:
        category = "Positive"
    elif num < 0:
        category = "Negative"
    else:
        category = "zero"
    even_odd = "even" if num%2==0 else "odd"
    return f"{num} is {category} and {even_odd}"
print(f"\nNumber Classification:")
numb = [-5,0,7,12,-8]
for i in numb:
    print(classify_number(i))
