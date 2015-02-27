/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode *sortedListToBST(ListNode *head) {
        if(head==NULL) return NULL;
        else if(head->next==NULL){
            TreeNode *root = new TreeNode(head->val);
            delete(head);
            return root;
        }
        else{
            ListNode *pre, *middle, *tail;
            ListNode fakehead(0);
            fakehead.next = head;
            pre = &fakehead;
            middle = tail = head;
            while(tail!=NULL && tail->next!=NULL){
                tail = tail->next->next;
                middle = middle->next;
                pre = pre->next;
            }
            TreeNode *root = new TreeNode(middle->val);
            pre->next=NULL;
            root->left=sortedListToBST(head);
            root->right = sortedListToBST(middle->next);
            delete(middle);
            
            return root;
            
        }
    }
};
