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
    ListNode *sortList(ListNode *head) {
        //using merge sort
        if(head==NULL){
            return head;
        }
        if(head!=NULL && head->next==NULL){
            return head;
        }
        //divide
        ListNode *mid, *tail, *head1, *head2;
        mid = head;
        tail = head;
        while(tail->next!=NULL && tail->next->next!=NULL){
            mid = mid->next;
            tail = tail->next->next;
        }
        head1 = sortList(mid->next);
        mid->next = NULL;
        head2 = sortList(head);
        //merge
        ListNode fakehead(0);
        tail = &fakehead;
        while(head1!=NULL && head2!=NULL){
            if(head1->val < head2->val){
                tail->next = head1;
                head1 = head1->next;
            }else{
                tail->next = head2;
                head2 = head2->next;
            }
            tail = tail->next;
            tail->next = NULL;
        }
        if(head1==NULL){
            tail->next = head2;
        }else{
            tail->next = head1;
        }
        return fakehead.next;
    }
};