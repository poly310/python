maths=float(input("enter marks in maths:"))
physics=float(input("enter marks in physics:"))
chemistry=float(input("enter marks in chemistry:"))
if(maths >= 65 and physics >= 55 and chemistry >= 50) or (maths + physics + chemistry >= 180) or (math + physics >= 140):
print("eligible for admission")
else:
print("not eligible for admission")