class Solution {
public:
    int numTrees(int n) {
        //dp
        vector<int> res;
        res.push_back(1);
        res.push_back(1);
        if(n==0) return res[0];
        if(n==1) return res[1];
        for(int i=2; i<=n; i++){
            int sum = 0;
            for(int j=0; j<i; j++){
                sum = sum+res[j]*res[i-j-1];
            }
            res.push_back(sum);
        }
        return res[n];
    }
};