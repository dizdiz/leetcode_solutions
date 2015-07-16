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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *p1, *p2, *f;
        p1 = l1;
        p2 = l2;
        ListNode fakehead(0);
        f = &fakehead;
        int carry = 0;
        while(p1!=NULL || p2!=NULL){
            if(p1!=NULL && p2!=NULL){
                int sum = p1->val + p2->val + carry;
                if(sum>9){
                    f->next = new ListNode(sum-10);
                    carry = 1;
                }else{
                    f->next = new ListNode(sum);
                    carry = 0;
                }
                p1 = p1->next;
                p2 = p2->next;
            }else if(p1==NULL){
                if((p2->val+carry)>9){
                    f->next = new ListNode(0);
                    carry = 1;
                }else{
                    f->next = new ListNode(p2->val+carry);
                    carry = 0;
                }
                p2 = p2->next;
            }else{
                if((p1->val+carry)>9){
                    f->next = new ListNode(0);
                    carry = 1;
                }else{
                    f->next = new ListNode(p1->val+carry);
                    carry = 0;
                }
                p1 = p1->next;
            }
            f = f->next;
        }
        if(carry==1){
            f->next = new ListNode(1);
        }
        return fakehead.next;
    }
};