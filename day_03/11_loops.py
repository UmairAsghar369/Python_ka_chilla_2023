# while and for loops 
a = 0
while (a<5):
    print(a)
    a = a+1

# for loop
for x in range(5,10):
    print(x)

# array loop
days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
for d in days:
  #  if (d=="Fri"):break        # loop stops
    if (d=="Fri"):continue        # Skips  d (friday)
    print(d)