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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode *slow, *fast,*temp;
        ListNode fakehead(0);
        slow = head;
        fast = head;
        temp = &fakehead;
        fakehead.next = head;
        if(head==NULL) return head;
        if(head!=NULL && head->next == NULL) return NULL;
        for(int i=1; i<n; i++){
            fast = fast->next;
        }
        while(fast->next!=NULL){
            temp = slow;
            slow = slow->next;
            fast = fast->next;
        }
        
        temp->next = slow->next;
        delete(slow);
        return fakehead.next;
        
    }
};
