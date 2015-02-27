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
    ListNode *partition(ListNode *head, int x) {
        ListNode fakehead1(0);
        ListNode fakehead2(0);
        ListNode *tail1,*tail2;
        tail1 = &fakehead1;
        tail2 = &fakehead2;
        if(head==NULL) return head;
        if(head!=NULL && head->next == NULL) return head;
        while(head!=NULL){
            //put small value after fakehead1
            if(head->val < x){
                tail1->next = head;
                tail1 = tail1->next;
                head = head->next;
                tail1->next = NULL;
            }
            //put bigger value after fakehead2
            else{
                tail2->next = head;
                tail2 = tail2->next;
                head = head->next;
                tail2->next = NULL;
            }
        }
        //connect these two lists, then return
        tail1->next = fakehead2.next;
        return fakehead1.next;
    }
};