class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # n=len(questions)
        # max_points=0
        # for i in range(0,n):
        #     points=0
        #     index=i
        #     while index<n:
        #         points+=questions[index][0]
        #         index+=questions[index][1]+1
        #         # print(index)
        #     max_points=max(max_points,points)
        # return max_points
        cache=[0]*len(questions)
        # print(cache)
        def backtrack(i):
            if i>=len(questions):
                # print(f"Reached end at i={i}, returning 0")
                return 0
            if cache[i]:
                # print(f"Using cached value at i={i} → {cache[i]}")
                return cache[i]
            points,brainpower=questions[i]
            # print(f"\nAt i={i}, Question: [points={points}, brainpower={brainpower}]")
            # print(f"--> Calling backtrack({i + 1}) to skip")
            # print(f"--> Calling backtrack({i + 1 + brainpower}) to solve and jump")
            skip =backtrack(i+1)
            solve=points+backtrack(i+1+brainpower)
            cache[i]= max(skip,solve)
            # print(cache)
            # print(f"Computed cache[{i}] = {cache[i]}")
            return cache[i]
           
        return backtrack(0)