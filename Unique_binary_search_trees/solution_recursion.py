class Solution:
    # @return an integer
    def numTrees(self, n):
        #basic idea: 
        #for each i in sequence n: calculate how many unique bst when i is root,
        #add these sum together, then we have the total number of bst.
        ###############
        #calculate the number of bst for i: 
        #(number of left childtree) * (number of right childtree)
        #which is: (numTrees(i-1))*(numTrees(n-i))
        ###############
        #special condition: n=0 and n=1 don't fit in this equation
        #so we need to filter them out.
        sum = 0
        if n==0: return 1
        if n==1: return 1
        for i in range(1,n+1):
            sum = sum+self.numTrees(i-1)*self.numTrees(n-i)
        return sum