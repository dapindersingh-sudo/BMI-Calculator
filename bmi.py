w=input("Enter your weight in kg->")
h=input("Enter your height in feet->")
weight=float(w)
hei=float(h)
height=hei/3.281
height=height*height
bmi=(weight/height)
print (bmi)
if bmi>25.0:
    {
        print("You are overweight")
    }
elif bmi<18.5:
    {
        print("You are underweight")
    }
elif bmi>18.5 and bmi<24.9:
    {
        print("Yor weight is good")
    }