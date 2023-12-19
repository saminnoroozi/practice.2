import random
system_namber=random.randint(1,6)
for a in range(10):
    person_number=int(input("Enter your number: "))
    if person_number==system_namber:
        show="good job"
    elif person_number!=system_namber:
         show="your loss, again!!"
    elif person_number==6:
        import random
        for a in range(1):
            show="you can try again"
print(show)
        

                