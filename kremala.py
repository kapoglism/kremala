lexh="Μαριος"

meg=len(lexh)
x="_"
   
for i in range(0,meg-1):
    x=x+" _"
        
vrethike=False
lathi=0
print(f"Η λέξη έχει {meg} γράμματα: ")
print(x)

while lathi<=5 and vrethike==False:
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
        print(f"Υπάρχει το γράμμα : {gr}")
    else:  
        print(f"Δεν υπάρχει το γράμμα : {gr}")  
        lathi=lathi+1
        print(f"Έχετε ακόμα {6-lathi} προσπάθειες")
    
    
        
    if flag==True:
        for i in thesh:
            x=list(x)
            x[i]=gr
            x="".join(x)    
    if "_" not in x:
        vrethike=True
    print(x)
    
if  vrethike==True:
    print("Βρήκατε τη λέξη!")
else:
    print(f"Δεν βρήκατε τη λέξη! Η λέξη ήταν: {lexh}")