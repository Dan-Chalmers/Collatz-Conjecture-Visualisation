# Collatz Conjecture

import matplotlib.pyplot as plt

def collatzConjecture(val, cnt):
    if val == 1:
        return cnt
    else:
        cnt += 1
        if val % 2 == 0:
            val = val * 0.5
        else:
            val = (3 * val) + 1
        #print ('Epoch', str(cnt), '=', int(val))
        return collatzConjecture(val, cnt)
    
#val = int(input('Input positive integer: '))
cnt, i = 0, 1
valArr, intArr = [], []
while i < 100000:
    finalInt = collatzConjecture(i, cnt)
    valArr.append(finalInt)
    intArr.append(i)
    print (finalInt)
    i += 1
    #if i == 1:
    #    i += 9
    #else:
    #    i += 10

plt.scatter(intArr, valArr, 5, color='red')
plt.xlabel('Starting int')
plt.ylabel('# of epochs to get to 1')
plt.title('Collatz Conjecture')
plt.show()

