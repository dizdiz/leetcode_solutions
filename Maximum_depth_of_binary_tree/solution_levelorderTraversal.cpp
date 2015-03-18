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
        if(root==NULL) return 0;
        int level = 0;
        queue<TreeNode*> cur_level,next_level;
        queue<TreeNode*> *cur, *next, *temp;
        cur = &cur_level;
        next = &next_level;
        cur_level.push(root);
        while(cur->size()!=0){
            if(cur->front()->left) next->push(cur->front()->left);
            if(cur->front()->right) next->push(cur->front()->right);
            cur->pop();
            if(cur->size()==0){
                temp = cur;
                cur = next;
                next = temp;
                level++;
            }
        }
        return level;
    }
};