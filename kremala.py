lexh="Μαριος"
lathosgr=[]
swstagr=[]
meg=len(lexh)
x="_"
   
for i in range(0,meg-1):
    x=x+" _"
        
vrethike=False
lathi=0
print(f"Η λέξη έχει {meg} γράμματα: ")
print(x)

while lathi<=5 and vrethike==False:
    flag=True
    while flag==True:   
        gr=input("Δώσε γράμμα")   
        if len(gr)==1 and gr.isalpha() and gr!="" and gr not in lathosgr and gr not in swstagr:
            flag=False
        else:
            flag=True 
        if flag==True:
            print("Λάθος εισαγωγή")
        
    flag2=False
    j=0
    thesh=[]
    for i in lexh:
        if i.lower()==gr or i.upper()==gr:
            flag2=True
            thesh.append(j)
        j=j+2    

    if flag2==True:
        print(f"Υπάρχει το γράμμα : {gr}")
        swstagr.append(gr)
    else:  
        print(f"Δεν υπάρχει το γράμμα : {gr}")  
        lathi=lathi+1
        lathosgr.append(gr)
        print(f"Έχετε ακόμα {6-lathi} προσπάθειες")
    
    print(swstagr)
        
    if flag2==True:
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