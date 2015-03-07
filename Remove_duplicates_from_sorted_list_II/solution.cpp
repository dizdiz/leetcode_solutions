/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *cur,*pre, *temp;
        ListNode fakehead(0);
        fakehead.next = head;
        cur = head;
        pre = &fakehead;
        /*while(cur!=NULL && cur->next!=NULL){
            if(cur->val==cur->next->val){
                int x = cur->val;
                while(cur!=NULL && cur->val==x){
                    temp = cur;
                    cur = cur->next;
                    delete(temp);
                }
                pre->next=cur;
            }else{
                pre = pre->next;
                cur = cur->next;
            }
        }
        return fakehead.next; */
        while(true){
            if (cur == NULL) {
                return fakehead.next;
            }
            if (cur->next == NULL){
                return fakehead.next;
            }
            if (cur->val != cur->next->val){
                pre = cur;
                cur = cur->next;
                continue;
            }
            while(cur->next != NULL && cur->val == cur->next->val){
                temp = cur;
                cur = cur->next;
                delete (temp);
            }
            temp = cur;
            cur = cur->next;
            pre->next = cur;
            delete (temp);
        }
       return fakehead.next; 
       
    }
};