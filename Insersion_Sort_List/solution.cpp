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
    ListNode *insertionSortList(ListNode *head) {
        ListNode fakehead(0);
        ListNode *temp, *temp2, *pretemp;
        
        temp = head;
        
        if (head==NULL){ 
            return NULL;
        }
        
        while(temp!=NULL){
            head = head->next;
            temp2 = fakehead.next;
            pretemp = &fakehead;
            
            while(temp2 != NULL && temp2->val < temp->val){
                
                pretemp = temp2;
                temp2 = temp2->next;
            }
            pretemp->next = temp;
            temp->next = temp2;
            temp = head;
        }
        
        return fakehead.next;
    }
};