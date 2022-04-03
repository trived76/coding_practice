#include <iostream>

struct LinkedListNode {
    int val = -1;
    LinkedListNode *next;
};

void add_node_end_linkedlist(const int val_to_be_added, LinkedListNode** ptr) {

    struct LinkedListNode *node = new LinkedListNode;

    node->val = val_to_be_added;
    node->next = (*ptr);

    (*ptr) = node;
}

void add_node_in_ascending_order(const int val_to_be_added, LinkedListNode** ptr) {

    auto ptr_next_node = (*ptr);
    while (true) {
        if (ptr_next_node->val >= val_to_be_added && val_to_be_added >= ptr_next_node->next->val) {
            //TODO replacement
            LinkedListNode* new_node = new LinkedListNode;
            new_node->val = val_to_be_added;
            new_node->next = ptr_next_node->next;
            
            ptr_next_node->next = nullptr;
            ptr_next_node->next = new_node;
            break;
        }
        else if (ptr_next_node->val != -1 && ptr_next_node->next != nullptr) {
            //Keep on traversing
            ptr_next_node = ptr_next_node->next;
        }
        else {
            add_node_end_linkedlist(val_to_be_added, ptr);
            break;
        }

    }
}

void print_linkedin_list(LinkedListNode** ptr) {
    std::cout << "LinkedList nodes in the sequence: " << std::endl;
    auto new_ptr = (*ptr);
    while (true) {
        
        if (new_ptr->next == nullptr) {
            std::cout << "-1" << std::endl;
            break;
        }
        
        std::cout << new_ptr->val << " -> ";

        LinkedListNode* next_node = new_ptr->next;
        new_ptr = nullptr;
        new_ptr = next_node;
    }
}

int main() {

    LinkedListNode *ls = new LinkedListNode;

    add_node_in_ascending_order(10, &ls);

    print_linkedin_list(&ls);

    add_node_in_ascending_order(17, &ls);

    print_linkedin_list(&ls);

    add_node_in_ascending_order(15, &ls);

    print_linkedin_list(&ls);

    add_node_in_ascending_order(7, &ls);

    print_linkedin_list(&ls);

    add_node_in_ascending_order(3, &ls);

    print_linkedin_list(&ls);   

    add_node_in_ascending_order(0, &ls);

    print_linkedin_list(&ls);  

    return 1;
}