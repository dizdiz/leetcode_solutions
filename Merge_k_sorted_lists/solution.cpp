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
//divide and conquer
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if(lists.size()==0) return NULL;
        return divide(lists, 0, lists.size()-1);
    }
    //conquer function, merge two divided part.
    ListNode *conquer(ListNode *l1, ListNode *l2){
        ListNode fakehead(0);
        ListNode *f;
        f = &fakehead;
        while(l1!=NULL && l2!=NULL){
            if(l1->val < l2->val){
                f->next = l1;
                l1 = l1->next;
            }else{
                f->next = l2;
                l2 = l2->next;
            }
            f = f->next;
        }
        if(l1==NULL){
            f->next = l2;
        }else{
            f->next = l1;
        }
        return fakehead.next;
    }
    //divide function, return a ListNode*
    ListNode *divide(vector<ListNode*> &lists, int start, int end){
        ListNode *l, *r;
        if(start>end){
            return NULL;
        }
        if(start==end){
            return lists[start];
        }
        int mid = (start+end)/2;
        l = divide(lists, start, mid);
        r = divide(lists, mid+1, end);
        
        return conquer(l,r);
    }
    
};