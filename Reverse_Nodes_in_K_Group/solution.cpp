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
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(k==1){
            return head;
        }
        int count = 0;
        ListNode *p1,*p2,*tail,*temp;
        p1 = head;
        while(p1!=NULL){
            p1 = p1->next;
            count++;
        }
        if(count/k < 1){
            return head;
        }
        ListNode fakehead(0);
        tail = &fakehead;
        p1 = head;
        for(int i=0; i<(count/k);i++){
            int m = k;
            while(m>0){
                m--;
                p2 = tail->next;
                temp = p1;
                p1 = p1->next;
                temp->next = p2;
                tail->next = temp;
            }
            while(tail->next!=NULL){
                tail = tail->next;
            }
        }
        tail->next = p1;
        return fakehead.next;
    }
};