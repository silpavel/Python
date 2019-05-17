#prime numerals
prime=[3,5]
isPrime=True
for num in range(7,100,2):
    isPrime=True
    for prm in prime:
        if num%prm==0:
            isPrime=False
            break
    if isPrime:
        prime.append(num)
print(prime)




