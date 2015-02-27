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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode *temp, *flag, *pre,*post;
        ListNode fakehead1(0);
        ListNode fakehead2(0);
        int i = 1;
        
        if (head == NULL) return head;
        
        fakehead1.next = head;
        temp = head;
        pre = &fakehead1;
        post = &fakehead2;
        for(i=1; i< n+1; i++){
            if(i<m){
                pre = pre->next;
                temp = temp->next;
            }
            else{
                flag = temp;
                temp = temp->next;
                flag->next = fakehead2.next;
                fakehead2.next = flag;
                
            }
        }
        while(post->next!=NULL){
            post = post->next;
        }
        pre->next = fakehead2.next;
        post->next = temp;
        return fakehead1.next;
    }
};