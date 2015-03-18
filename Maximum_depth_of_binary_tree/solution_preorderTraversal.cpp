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
        stack<TreeNode*> node;
        stack<int> depth;
        TreeNode *cur;
        int cur_depth = 0;
        int max_depth = 0;
        cur = root;
        while(cur!=NULL || node.size()!=0){
            if(cur!=NULL){
                cur_depth++;
                if(cur->right!=NULL){
                    node.push(cur->right);
                    depth.push(cur_depth);
                }
                cur=cur->left;
            }else{
                cur = node.top();
                node.pop();
                cur_depth = depth.top();
                depth.pop();
            }
            if(max_depth<cur_depth){
                max_depth = cur_depth;
            }
        }
        return max_depth;
    }
};