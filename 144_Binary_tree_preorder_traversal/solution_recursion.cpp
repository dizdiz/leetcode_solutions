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
    vector<int> preorderTraversal(TreeNode *root) {
        //recursive
        vector<int> v,temp;
        if(root==NULL){
            return v;
        }else{
            v.push_back(root->val);
        }
        temp = preorderTraversal(root->left);
        v.insert(v.end(),temp.begin(),temp.end());
        temp = preorderTraversal(root->right);
        v.insert(v.end(),temp.begin(),temp.end());
        return v;
    }
};