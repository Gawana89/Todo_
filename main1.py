f = open('figure.txt', 'w')

def stroka(wide):
    stroka_f = ""
    for i in range(wide):  
        if i == 0 or i == wide-1:
            stroka_f += '@'* wide
            stroka_f += '\n'
        else:
            stroka_f += '@'+ ' '*(wide-2) +'@'
            stroka_f += '\n'
       
    return stroka_f


for i in stroka(5):
    f.write(i)
f.close()
f = open('figure.txt', 'r')
st = f.read()
for i in st:
    print(i,end='')