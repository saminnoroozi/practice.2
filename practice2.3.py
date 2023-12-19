name=input("Enter your name: ")
family=input("Enter your last name: ")
score1=float(input("Enter your first score: "))
score2=float(input("Enter your second score: "))
score3=float(input("Enter your third score: "))

moadel=(score1+score2+score3)/3
if moadel<10:
    show="failed"
if 10<moadel<15:
    show="middle"
if 15<moadel<=20:
     show="pass"

print("hi,",name,family,"your moadel",moadel,"and you",show)