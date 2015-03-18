class Solution:
    # @return an integer
    def numTrees(self, n):
        #dynamic programming
        #for each i, caculate how many unique bst are there when i is root
        #store them in res(when caculate i+1, we can use the result of i)
        ###################
        res = [1,1]
        #caculate how many unique bst are there when i is root
        for i in range(2,n+1):
            sum = 0
            #sum is the number of bst when i is root
            #enumerate different left/right subtree(use j as control variable)
            for j in range (0,i):
                sum += res[j]*res[i-j-1]
            res.append(sum)
        return res[n]