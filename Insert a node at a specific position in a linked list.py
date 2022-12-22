                                                        Insert a node at a specific position in a linked list  
 import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def length(llist):
    cnt=0
    while(llist!=None):
        cnt+=1
        llist=llist.next
    return cnt

def insertNodeAtPosition(llist, data, position):
    if(position==0 or position>length(llist)):
        return llist
    nn=SinglyLinkedListNode(data)
    if(position==0):
        nn.next=llist
        return nn
    tmp=llist
    for i in range(position-1):
        llist=llist.next
    nn.next=llist.next
    llist.next=nn
    return tmp
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
