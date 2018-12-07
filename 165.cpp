
Definition of singly-linked-list:
class ListNode {
    public:
        int val;
        ListNode *next;
        ListNode(int val) {
        this->val = val;
        this->next = NULL;
    }
}


class Solution {
public:
    /**
     * @param l1: ListNode l1 is the head of the linked list
     * @param l2: ListNode l2 is the head of the linked list
     * @return: ListNode head of linked list
     */
    ListNode * mergeTwoLists(ListNode * l1, ListNode * l2) {
        // write your code here
        if(l1 == NULL){
            return l2;
        }
        if(l2 == NULL){
            return l1;
        }

        ListNode *tmp = NULL;
        ListNode *head = NULL;
        if(l1->val < l2->val){
            head = new ListNode(l1->val);
            l1 = l1->next;
        }
        else{
            head = new ListNode(l2->val);
            l2 = l2->next;
        }
        ListNode *front = head;
        while(l1 != NULL && l2 != NULL){
            if(l1->val < l2->val){
                tmp = new ListNode(l1->val);
                l1 = l1->next;
            }
            else{
                tmp = new ListNode(l2->val);
                l2 = l2->next;
            }
            front->next = tmp;
            front = tmp;
        }
        while(l1 != NULL){
            tmp = new ListNode(l1->val);
            front->next = tmp;
            front = tmp;
            l1 = l1->next;
        }
        while(l2 != NULL){
            tmp = new ListNode(l2->val);
            front->next = tmp;
            front = tmp;
            l2 = l2->next;
        }

        return head;
    }
};
