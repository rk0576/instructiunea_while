n=0
sp=0
sn=0
np=0
nn=0
c=0
while c<12:
    n=eval(input("Introduceti temperatura:"))
    if n<55 and n>-60:
        c+=1
        if n>0:
            sp+=n
            np+=1
        elif n<0:
            sn+=n
            nn+=1 
    else: print("Introduceti o temperatura valida:")           
if np>0:
    print("medie_poz: ",round(float(sp/np), 2))
else:print("Nu au fost temperaturi pozitive:")

if nn>0:
    print("medie_neg=",round(float(sn/nn), 2))
else:print("Nu au fost temperaturi negative=")