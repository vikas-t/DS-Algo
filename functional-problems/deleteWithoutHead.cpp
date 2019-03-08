// https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

void deleteNode(Node *node)
{
   if (node->next == NULL) {
       node = NULL;
       return;
    // If the node is the last node, make it null
   }
   else {
       node->data = node->next->data;
       node->next = node->next->next;
    // Copy the data of the next node to the current node
    // Let the current one point to the next of the next, there by deleting the
    // next node, but its value is copied to the current one. So value of the
    // current node gets deleted
   }
}