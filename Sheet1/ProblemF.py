# One day Dola was walking in the garden and when he sat to rest, he found a piece of paper written on it the number n, Dola decided to play a game with you. Dola will give you the number he found on the paper and wants you to tell him all the good numbers of the number n good numbers are the divisors of n
# , Ex. 3 is a good number for 6, but 4 is not a good number for 7.
n = int(input())
arr = []
for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)
for i in arr:
     print(i, end = " ")