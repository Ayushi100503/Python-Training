nums = [10, 11, 12, 13, 17, 20, 23]
primes =[]
for n in nums:
    if  n>1:
        
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
             break
        else:
            primes.append(n)
            
print(primes)
        