class Solution {
public:
    int numTrees(int n) {
        //recursion
        if(n==0) return 1;
        if(n==1) return 1;
        int sum = 0;
        for(int i=1; i<=n; i++){
            //i is root, caculate how many bst are there
            sum = sum + numTrees(i-1)*numTrees(n-i);
        }
        return sum;
    }
};