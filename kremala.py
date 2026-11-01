lexh="Μαριος"
gr=input("Δώσε γράμμα ")

flag=False
for i in lexh:
    if i.lower()==gr:
        flag=True

if flag==True:
    print("Υπάρχει το γράμμα")
else:  
    print("Δεν υπάρχει το γράμμα")  