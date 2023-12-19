w=int(input("Enter your weight(kg): "))
h=float(input("Enter your heght(m) : " ))
mbi=w/(h*2)
print("your mbi =",mbi)
if mbi<18.5:
    show="weight loss"
    if 18.5<mbi>24.9:
        show="normal weight"
    if 25<mbi>29.9:
        show="overweight"
    if mbi>30:
        show="obesity"

        print(show)
    