#Algorithm 3
import numpy as np
import time
import matplotlib.pyplot as plt

def f1(n):
    if n<=2:
        return 1
    else:
        return f1(n-1) + f1(n-2)

def f2(n):
    if n<=2:
        return 1
    else:
        p=1
        q=1
        for i in range(3,n+1):
            r = p+q
            p = q
            q = r
        return r
    
G = np.array([[0,1],[1,1]])
def Power_of_G(n):
    if n==1:
        return G;
    else:
        if n%2 == 0:
            H = Power_of_G(n/2);
            return np.dot(H,H)
        else:
            H = Power_of_G((n-1)/2)
            return np.dot(H, np.dot(H,G))
        
def f3(n):
    temp = Power_of_G(n)
    return temp[0][1]

inputs = np.arange(5, 30, 1)
inputs2 = np.arange(100,10000,1)

def timecalc(algorithm, inputs):
    times=[]
    for i in inputs:
        start = float(time.time())
        answer = algorithm(i)
        end = float(time.time())
        runtime = float(end - start)
        times.append(runtime)
    return times

        
f1_times = timecalc(f1, inputs)
f2_times = timecalc(f2, inputs2)
f3_times = timecalc(f3, inputs2)

plt.plot(inputs, f1_times, 'r') # plotting t, a separately 
plt.title('Runtime of F1()')
plt.xlabel('Value of N or Input')
plt.ylabel('Running Time')



plt.plot(inputs2, f2_times, inputs2, f3_times) # plotting t, a separately 
plt.title('Running time of F2 vs F3')
plt.gca().legend(('F2','F3'))
plt.xlabel('Value of N or Input')
plt.ylabel('Running Time')

