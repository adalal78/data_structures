class DNode:
    def __init__(self, val):
        
        self.val = val
        self.next = None
        self.prev = None
        
    def traverse(self):
        
        vals = []
        while(self != None):
            vals.append(self.val)
            self = self.next
            
        return vals
            
    def delete(self):
        
        if (self == None):
            return
        
        if (self.prev != None and self.next != None):
            if (self.prev == None):
                self.next.prev = None
                
            elif (self.next == None):
                self.prev.next = None
                
            else:
                self.prev.next = self.next
                self.next.prev = self.prev
                
        self.val = None
        self.next = None
        self.prev = None
        

class Node:
    def __init__(self,val):
        
        self.val = val
        self.next = None
        
    def traverse(self):
        
        while(self != None):
            print(self.val)
            self = self.next
            
    def insert(self,val):
        
        if(self == None):
            return Node(val)
        
        else:
            new_node = Node(val)
            new_node.next = self
            return new_node
            
    def delete(self, node):
        
        if(node == None or self == None):
            return
                
        if (node != self):
            iter_node = self
            while(iter_node.next != node):
                iter_node = iter_node.next
                
            #print(iter_node.val)
            iter_node.next = node.next
        
        node.next = None
        node.val = None
        
        return
        
    def reverse(self):
        
        if (self == None):
            print("ERROR: Passed None parameter into reverse")
            return
        
        elif (self.next == None):
            return self
        
        else:
            iter_node = self.next
            node = self
            next_node = iter_node
            self = iter_node
            iter_node = iter_node.next
            
            next_node.next = node
            node.next = None
            
            while(iter_node != None):
                #print(self.val, iter_node.val)
                node = self
                next_node = iter_node
                self = iter_node
                iter_node = iter_node.next
                
                next_node.next = node
            
        return self
            
            
def remove_duplicates(head):
    
    node_dict = {}
    iter_node = head
    node_dict[iter_node.val] = 1
    prev_node = iter_node
    iter_node = iter_node.next
    while(iter_node != None):
        if(iter_node.val in node_dict.keys()):
            prev_node = remove_node(prev_node,iter_node)
            iter_node = prev_node.next
        else:
            node_dict[iter_node.val] = 1
            prev_node = iter_node
            iter_node = iter_node.next
            
    return head

def get_kth(head,k):
    if k == 1:
        return head.val
    else:
        for i in range(k-1):
            head = head.next
        
    return head.val

def get_nodes(head, val):
    node_list = []
    
    iter_node = head
    while(iter_node != None):
        if iter_node.val == val:
            node_list.append(iter_node)
        iter_node = iter_node.next
    
    return node_list

def list_length(head):
    length = 1
    while head.next != None:
        length += 1
        head = head.next
        
    return length
