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
    void reorderList(ListNode *head) {
        if(head==NULL){
            return;
        }
        if(head!=NULL && head->next==NULL){
            return;
        }
        //divide the list, find the last half(starts with head2)
        ListNode *mid, *tail, *head2, *temp,*l, *r;
        mid = head;
        tail = head;
        while(tail->next!=NULL && tail->next->next!=NULL){
            mid = mid->next;
            tail = tail->next->next;
        }
        head2 = mid->next;
        mid->next = NULL;
        //reverse the last half
        ListNode fakehead(0);
        while(head2!=NULL){
            temp = head2;
            head2 = head2->next;
            temp->next = fakehead.next;
            fakehead.next = temp;
        }
        //interleave the two lists
        r = fakehead.next;
        l = head;
        while(r!=NULL){
            temp = r;
            r = r->next;
            temp->next = l->next;
            l->next = temp;
            l = temp->next;
        }
        return;
    }
};