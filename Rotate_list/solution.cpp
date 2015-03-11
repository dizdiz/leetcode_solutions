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
    ListNode *rotateRight(ListNode *head, int k) {
        if(head==NULL) return head;
        if (k==0) return head;
        
        ListNode *p, *pre, *tail;
        ListNode fakehead(0);
        fakehead.next = head;
        //calculate the length of list
        int count = 0;
        tail = &fakehead;
        p = head;
        while(p!=NULL){
            p = p->next;
            tail = tail->next;
            count++;
        }
        //find out where to start the rotate
        if(k%count==0) return head;
        count = count - k%count;
        pre = &fakehead;
        p = head;
        while(count>0){
            count--;
            p = p->next;
            pre = pre->next;
        }
        //the rotate
        fakehead.next = p;
        tail->next = head;
        pre->next = NULL;
        
        return fakehead.next;
    }
};