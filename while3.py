s=0
n=eval(input('Introduceti un numar:'))

while n%2==0 or (n%2!=0 and n%3!=0):
    if n%2==0:
        s+=n
    
    n=eval(input('Introduceti un numar:'))

print('Suma numerelor pare introduse:',s)