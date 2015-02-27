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
    ListNode *swapPairs(ListNode *head) {
        ListNode fakehead(0);
        ListNode *cur,*tail,*temp;
        cur = head;
        tail = &fakehead;
        while(cur!=NULL){
            if(cur->next==NULL){
                tail->next = cur;
                return fakehead.next;
            }
            else{
                temp = cur;
                cur = cur->next->next;
                temp->next->next = NULL;
                tail->next = temp->next;
                tail = tail->next;
                tail->next = temp;
                temp->next = NULL;
                tail = tail->next;
            }
        }
        return fakehead.next;
    }
};
