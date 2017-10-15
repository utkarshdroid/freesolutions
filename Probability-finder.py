__author__ = 'RAJAT'
import math
def count_odd(L):
    if len(L)==0:
        return 0
    return (L[0]%2) + count_odd(L[1:])
def count_even(L):
    if len(L)==0:
        return 0
    return (L[0]%2 ==0) + count_even(L[1:])
def gcdIter(a, b):
    if b == 0:
        return a
    else:
        return gcdIter(b, a % b)
t = int(input())
while t:
    t -= 1
    n ,q = map(int, input().split())
    arr = list(map(int, input().split()))
    while q:
        q -= 1
        k , l, r = map(int, input().split())

        if l == r:
                print(0)
        else:
            if k == 0:
                slicedArray = arr[l-1 : r+1]
                count = 0
                # print(math.ceil(((r-l)+1)/2))
                n = math.ceil(((r-l)+1)/2)
                for i in range(n):
                    if slicedArray[i] % 2 ==0:
                        count += 1
                    if i!= n-1:
                        if slicedArray[(r-l)-i] % 2 ==0:
                            count +=1

                # evenArray = count_even(slicedArray)
                # evenArray = sum([1 for n in slicedArray if n%2 ==0])

                gcd = gcdIter(count, ((r-l)+1))
                # nominalForm = Fraction(evenArray, len(slicedArray))

                num = count//gcd
                deno = ((r-l)+1)//gcd
                if num == 0:
                    print(0)
                elif num ==  deno:
                    print(num)
                else:
                    print(num, deno)
            else:
                slicedArray = arr[l-1 : r+1]
                count = 0
                # print(math.ceil(((r-l)+1)/2))
                n = math.ceil(((r-l)+1)/2)
                if  n% 2 == 0:
                    b = False
                for i in range(n):
                    if slicedArray[i] % 2 !=0:
                        count += 1

                    if i!= n-1:
                        if slicedArray[(r-l)-i] % 2 !=0:
                            count +=1
                print(count)
                # oddArray = count_odd(slicedArray)
                # OddArray = sum([1 for n in slicedArray if n%2])
                gcd = gcdIter(count, ((r-l)+1))
                # nominalForm = Fraction(oddArray, len(slicedArray))
                num = count//gcd
                deno = ((r-l)+1)//gcd
                if num == 0:
                    print(0)
                elif num == deno:
                    print(num)
                else:
                    print(num, deno)
