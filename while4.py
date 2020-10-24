n=eval(input('Introduceti un numar:'))
c=0
s=0
p=1

while c<n:
    c+=1
    s+=c
    p*=c

print(f'Suma={round(s, 2)}',f'Produsul={round(p, 2)}',f'Media aritmetica={round(s/c, 2)}', sep='\n')