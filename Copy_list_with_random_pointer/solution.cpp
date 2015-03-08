/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
 
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head==NULL){
            return head;
        }
        
        //create new listnodes and interleave them with oldlist
        RandomListNode *p,*newnode,*temp,*f;
        p = head;
        while(p!=NULL){
            newnode = new RandomListNode(p->label); 
            newnode->next = p->next;
            p->next = newnode;
            p = newnode->next;
        }
        //copy random pointer
        p = head;
        while(p!=NULL){
            if(p->random==NULL){
                p->next->random = NULL;
            }else{
                p->next->random = p->random->next;
            }
            p = p->next->next;
        }
        //extract newlist from oldlist
        RandomListNode fakehead(0);
        f = &fakehead;
        p = head;
        while(p!=NULL){
            //temp points to new node,p points to old node
            temp = p->next;
            p->next = temp->next;
            p = p->next;
            temp->next = NULL;
            f->next = temp;
            f = f->next;
        }
        return fakehead.next;
        /*
        unordered_map<RandomListNode*,RandomListNode*> htable;
        RandomListNode *p;
        p = head;
        while(p!=NULL){
            htable[p] = new RandomListNode(p->label);
            p = p->next;
        }
        p = head;
        while(p!=NULL){
            htable[p]->next = htable[p->next];
            htable[p]->random = htable[p->random];
            p = p->next;
        }
        return htable[head];
        */
    }
};