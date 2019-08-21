import math
n=int(input())
prime=[]
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=="__main__":
    for i in range(2,int(math.sqrt(n))+1):
        if isPrime(i):
            prime.append(i)
    time=0
    for i in range(int(math.sqrt(n))+1,n+1):
        if isPrime(i):
            time+=1
    for i in prime:
        time+=math.floor(math.log(n,i))
    print (int(time))

