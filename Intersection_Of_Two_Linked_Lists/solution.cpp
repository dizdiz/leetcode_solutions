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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA==NULL || headB==NULL){
            return NULL;
        }
        //calculate list size
        int countA = 0;
        int countB = 0;
        ListNode *pa, *pb;
        pa = headA;
        pb = headB;
        while(pa!=NULL){
            countA++;
            pa = pa->next;
        }
        while(pb!=NULL){
            countB++;
            pb = pb->next;
        }
        //put pa and pb at the same distance from the intersection
        pa = headA;
        pb = headB;
        if(countA>countB){
            for(int i=0; i<countA-countB; i++){
                pa = pa->next;
            }
        }else{
            for(int i=0; i<countB-countA; i++){
                pb = pb->next;
            }
        }
        //move pa and pb until they reach the intersection
        while(pa!=pb){
            pa = pa->next;
            pb = pb->next;
        }
        return pa;
    }
};