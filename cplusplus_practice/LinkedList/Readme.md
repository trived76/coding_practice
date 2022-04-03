# LinkedList Sorted

I once came across a question to generate a very simple solution for a basic problem - `LinkedList` in any order (ascending/descending), unfortunately, I could not come up with the solution right away. The issue was that I was not knowing how I should use pointers to handle this manipulation.

The assumption is that we assume that we already have a sorted `LinkedList` and every time a user inserts an element to the `LinkedList`, we put it in a way that the final `LinkedList` that we keep in the storage always remains sorted in any order that we are interested in.

As a starter point, I first checked this reference: https://www.softwaretestinghelp.com/linked-list/ to understand how the `struct LinkedList` should be constructed, more precisely, the element `next` which is the pointer to its own struct data type because that's the thing I could not answer immediately. Nevertheless, from this ref, I just understood the `struct LinkedList` and how a node is inserted in the `LinkedList`, that's it. 

The function to add a new node and keep the `LinkedList` sorted while adding a new node was written by me entirely based on my understanding with raw pointers. Please note that this is for the first time, I used raw pointers on my own from scratch.

# How to run this?

```shell
g++ --std=c++17 -o SortLinkedList SortedLinkedList.cpp; ./SortLinkedList; rm SortLinkedList
```

It prints the following message on the terminal:

```
LinkedList nodes in the sequence: 
10 -> -1
LinkedList nodes in the sequence: 
17 -> 10 -> -1
LinkedList nodes in the sequence: 
17 -> 15 -> 10 -> -1
LinkedList nodes in the sequence: 
17 -> 15 -> 10 -> 7 -> -1
LinkedList nodes in the sequence: 
17 -> 15 -> 10 -> 7 -> 3 -> -1
LinkedList nodes in the sequence: 
17 -> 15 -> 10 -> 7 -> 3 -> 0 -> -1
```