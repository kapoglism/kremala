lexh="Μαριος"
gr=input("Δώσε γράμμα ")

flag=False
j=0
thesh=[]
for i in lexh:
    if i.lower()==gr or i.upper()==gr:
        flag=True
        thesh.append(j)
    j=j+2    

if flag==True:
    print("Υπάρχει το γράμμα")
else:  
    print("Δεν υπάρχει το γράμμα")  
    
meg=len(lexh)
x="_"
for i in range(0,meg-1):
    x=x+" _"
    
if flag==True:
    for i in thesh:
        x=list(x)
        x[i]=gr
        x="".join(x)    

print(x)