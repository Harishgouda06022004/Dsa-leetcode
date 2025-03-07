class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # l=[]
        # if left <= 2 <= right:
        #     l.append(2)
        #     left = 3  
        # if left % 2 == 0:
        #     left += 1
        
        # for i in range(left,right+1,2):
        #     is_prime=True
        #     for j in range(2,int(i**0.5)+1):
        #         if i%j==0:
        #             is_prime=False
        #             break
        #     if is_prime:
        #         l.append(i)
        # print(l)
        # if len(l)<2:
        #     return [-1,-1]
        # closet=[]
        # min_diff=float('inf')
        # for i in range(len(l)-1):
        #     n=l[i+1]-l[i]
        #     min_diff =min(min_diff,n)
        # print(min_diff)
        # for i in range(len(l)-1):
        #     if l[i+1]-l[i]==min_diff:
        #         closet.append(l[i])
        #         closet.append(l[i+1])
        #         break
        # return closet
        LIMIT = right + 1
        is_prime = [True] * LIMIT
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(LIMIT ** 0.5) + 1):
            if is_prime[i]:  # If i is prime, mark multiples as non-prime
                for j in range(i * i, LIMIT, i):
                    is_prime[j] = False

        # Step 2: Extract prime numbers in range [left, right]
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        # Edge Case: If less than 2 primes exist, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]

        # Step 3: Find the closest prime pair
        min_diff = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair


            