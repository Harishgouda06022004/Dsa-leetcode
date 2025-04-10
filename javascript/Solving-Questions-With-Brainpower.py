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
        def backtrack(i):
            if i>=len(questions):
                return 0
            if cache[i]:
                return cache[i]
            points,brainpower=questions[i]
            cache[i]= max(
                backtrack(i+1),
                points+backtrack(i+1+brainpower)
            )
            return cache[i]
        return backtrack(0)