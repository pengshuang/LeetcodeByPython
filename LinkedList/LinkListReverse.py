# coding: utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def nonrecurse(head):
    if head is None or head.next is None:
        return head
    newhead = None
    while head:
        temp = head.next
        head.next = newhead
        newhead = head
        head = temp
    return newhead


def recurse(head):
    if head is None or head.next is None:
        return head
    newhead = recurse(head.next)
    head.next.next = head
    head.next = None
    return newhead

head = ListNode(1)
p1 = ListNode(2)      # 建立链表1->2->3->4->None;
p2 = ListNode(4)
p3 = ListNode(3)
head.next = p1
p1.next = p2
p2.next = p3
p = nonrecurse(head)   # 输出链表 4->3->2->1->None
while p:
    print p.val
    p = p.next

