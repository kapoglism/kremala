import random as rd
lexeis = ["θαλασσα", "ελεφαντας", "πεταλουδα", "σουβλακι", "παραθυρο",
          "κατσαρολα", "λουλουδι", "φεγγαρι", "ποδηλατο", "μπαλκονι",
          "σοκολατα", "καραβι", "χελωνα", "βιβλιοθηκη", "ουρανος",
          "δελφινι", "παγωτο", "κουταλι", "πορτοκαλι", "ηφαιστειο"]
lexh=rd.choice(lexeis)
lathosgr=[]
swstagr=[]
meg=len(lexh)
x="_"
me_tono    = ["ά", "έ", "ή", "ί", "ό", "ύ", "ώ", "ϊ", "ϋ", "ΐ", "ΰ", "Ά", "Έ", "Ή", "Ί", "Ό", "Ύ", "Ώ", "Ϊ", "Ϋ"]
xwris_tono = ["α", "ε", "η", "ι", "ο", "υ", "ω", "ι", "υ", "ι", "υ", "Α", "Ε", "Η", "Ι", "Ο", "Υ", "Ω", "Ι", "Υ"]

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
        if gr in me_tono:
            thesh=me_tono.index(gr)
            gr=xwris_tono[thesh]
        if len(gr)==1 and gr.isalpha() and gr!="" and gr.lower() not in lathosgr and gr.lower() not in swstagr and gr.upper() not in lathosgr and gr.upper() not in swstagr:
            flag=False
        else:
            flag=True 
        if flag==True:
            print("Λάθος εισαγωγή")
        
    flag2=False
    j=0
    thesh2=[]
    for i in lexh:
        if i=="σ" and gr=="ς":
            flag2=True 
            gr="σ"
        elif i=="ς" and gr=="σ":
            flag2=True 
            gr="ς"
        if i.lower()==gr or i.upper()==gr:
            flag2=True
            thesh2.append(j)
        j=j+2    

    if flag2==True:
        print(f"Υπάρχει το γράμμα : {gr}")
        swstagr.append(gr)
    else:  
        print(f"Δεν υπάρχει το γράμμα : {gr}")  
        lathi=lathi+1
        lathosgr.append(gr)
        print(f"Έχετε ακόμα {6-lathi} προσπάθειες")
    

        
    if flag2==True:
        for i in thesh2:
            x=list(x)
            x[i]=gr
            x="".join(x)    
    if "_" not in x:
        vrethike=True
    print(x)
    gr=gr.lower()#### 
    
if  vrethike==True:
    print("Βρήκατε τη λέξη!")
else:
    print(f"Δεν βρήκατε τη λέξη! Η λέξη ήταν: {lexh}")