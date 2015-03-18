/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode *root) {
        int max_depth = 0;
        stack<TreeNode*> s;
        TreeNode *cur,*visited;
        cur = root;
        while(cur || !s.empty()){
            while(cur){
                s.push(cur);
                cur = cur->left;
            }
            cur = s.top();
            //for every leafnode, the stack has its path to root
            if(!cur->left && !cur->right){
                if(s.size()>max_depth){
                    max_depth = s.size();
                }
            }
            if(cur->right && cur->right!=visited){
                cur = cur->right;
            }else{
                s.pop();
                visited = cur;
                cur = NULL;
            }
        }
        return max_depth;
    }
};