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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *temp1, *temp2,*tail;
        ListNode fakehead(0);
        temp1 = l1;
        temp2 = l2;
        tail = &fakehead;
        while(temp1!=NULL && temp2!=NULL){
            if(temp1->val <= temp2->val){
                tail->next = temp1;
                tail = tail->next;
                temp1 = temp1->next;
            }
            else{
                tail->next = temp2;
                tail = tail->next;
                temp2 = temp2->next;
            }
        }
        if(temp1 == NULL){
            tail->next = temp2;
        }
        if(temp2 == NULL){
            tail->next = temp1;
        }
        return fakehead.next;

    }
};
