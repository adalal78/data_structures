class BstNode():
    
    def __init__(self, key, val, leftChild = None, rightChild = None, parent = None):
        
        self.key = key
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
       
    def hasLeftChild(self):
        return self.leftChild
        
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return (self.parent and self.leftChild.parent == self)
    
    def isRightChild(self):
        return (self.parent and self.rightChild.parent == self)
        
    def isRoot(self):
        return (not self.parent)
    
    def isLeaf(self):
        return (not (self.leftChild or self.rightChild) )
        
    def hasAnyChildren(self):
        return (self.leftChild or self.rightChild)
        
    def hasBothChildren(self):
        return (self.leftChild and self.rightChild)
        
    def replaceNodeData(self, key, val, leftChild, rightChild):
        self.key, self.val, self.leftChild, self.rightChild = key, val, leftChild, rightChild
        if (self.hasLeftChild):
            self.leftChild.parent = self
        if (self.hasRightChild):
            self.rightChild.parent = self
    

class BinarySearchTree():
    
    def __init__(self):
        
        self.root = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    
    #in-order iteration using yield
    def __iter__(self):
        
        if (self):
            if (self.hasLeftChild()):
                for node in self.leftChild:
                    yield node
            
            yield (self.key, self.val)
            if (self.hasRightChild()):
                for node in self.rightChild:
                    yield node
    
    
    def put(self, key, val):
        if (self.root):
            self._put(self.root, key, val)
        
        else:
            self.root = BstNode(key,val)
        
        self.size += 1
        
    def _put(self, node, key, val):
        
        if (key < node.key):
            
            if (node.hasLeftChild()):
                self._put(node.leftChild(), key, val)
                
            else:
                node.leftChild = BstNode(key, val, parent = node)
                
        else:
            
            if (node.hasRightChild()):
                self._put(node.rightChild(), key, val)
                
            else:
                node.rightChild = BstNode(key, val, parent = node)
                
    def __setitem__(self, key, val):
        return self.put(key,val)
    
    def get(self, key):
        
        if (self.root):
            node = self._get(self.root, key)
            
            if (node):
                return node.val
            else:
                print ("There is no node with the key " + str(key) + ".")
                return None
            
        else:
            print ("The binary tree is empty, so such key " + str(key) + " exists.")
            return None
        
    def _get(self, node, key):
        
        if (not node):
            return None
        
        elif (node.key == key):
            return node
        
        elif (key < node.key):
            if (node.hasLeftChild()):
                self._get(node.leftChild(), key)
            
            else:
                return None
        
        else:
            if (node.hasRightChild()):
                self._get(node.rightChild(), key)
                
            else:
                return None
                
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if (self._get(self.root, key)):
            return True
        else:
            return False
        
    def delete(self, key):
        
        if (self.size == 1 and self.root.key == key):
            self.root = None
            self.size -= 1
            
        elif (self.size > 1):
            node = self._get(self.root, key)
            
            if (node):
                self.remove(node)
                self.size -= 1
                
            else:
                raise KeyError("Error: There is no such key " + str(key) + " in the tree.")
                
        else:
            raise KeyError("Error: The tree is empty.")
            
    def __delitem__(self,key):
        return self.delete(key)
    
    def remove(self, node):
        
        if (node.isLeaf()):
            
            if (node.parent.leftChild == node):
                node.parent.leftChild = None
                
            else:
                node.parent.rightChild = None
                
        elif (node.hasBothChildren()):
                node.leftChild.parent = node.parent
                node.rightChild.parent = node.parent
                node.parent.leftChild = node.leftChild
                node.parent.rightChild = node.rightChild
        
        else: #node has only one child
            
            #node has a left child
            if (node.hasLeftChild()):    
                if (node.isLeftChild()):
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                    
                elif (node.isRightChild()):
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                    
                else:
                    node.replaceNodeData(node.leftChild.key, node.leftChild.val, node.leftChild.leftChild, node.leftChild.rightChild)
            
            #node has a right child
            else:
                if (node.isLeftChild()):
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                    
                elif (node.isRightChild()):
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                    
                else:
                    node.replaceNodeData(node.rightChild.key, node.rightChild.val, node.rightChild.leftChild, node.rightChild.rightChild)
                    
    def findSuccesor(self):
        
        successorNode = None
        if (self.hasRightChild()):
            successorNode = self.rightChild.findMin()
            
        else:
            if (self.parent):
                if (self.isLeftChild()):
                    successorNode = self.parent
                    
                else:
                    self.parent.rightChild = None
                    successorNode = self.parent.findSuccessor()
                    self.parent.rightChild = self
                    
        return successorNode
    
    def findMin(self):
        minKeyNode = self
        while (minKeyNode.hasLeftChild()):
            minKeyNode = minKeyNode.leftChild
            
        return minKeyNode
    
    def spliceNode(self):
        
        if (self.isLeaf()):
            if (self.isLeftChild()):
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
                
        elif (self.hasChildAnyChildren()):
            if (self.hasLeftChild()):
                if (self.isLeftChild()):
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
                
            else:
                if (self.isLeftChild()):
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
