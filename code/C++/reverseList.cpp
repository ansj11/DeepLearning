#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
};

ListNode* reverseList(ListNode* Head){
    ListNode pre,cur,nxt;
    pre = Head;
    cur = pre->next;
    nxt = cur->next;
    Head->next = nullptr;
    while(nxt){
        cur->next = pre;
        pre = cur;
        cur = next;
        nxt = nxt->next;
    }
    cur->next = pre;

    return cur;
}

