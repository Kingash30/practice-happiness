a=b=c=0
print('Enter three numbers to compare: ')
a  = input()
b = input()
c = input()
if (a>b):
    if(a>c):
        print(a,' is the largest number')
    else:
        print(c,' is the largest number')
else:
    if(b>c):
        print(b,' is the largest number')
    else:
        print(c,' is the largest number')
quit()