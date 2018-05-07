class binary_heap():
    
    def __init__(self):
        
        self.heap = []
        self.current_size = 0
        
    def show(self):
        
        print self.heap
        

    def perc_up(self, indx):
        
        counter = indx
        while( (counter != 0) and (self.heap[counter // 2] > self.heap[counter]) ):
            
            self.heap[counter], self.heap[counter // 2] = self.heap[counter // 2], self.heap[counter]
            counter = counter // 2
            
    
    def insert(self, val):
        
        self.heap.append(val)
        self.current_size += 1
        self.perc_up(self.current_size-1)
        
    
    def perc_down(self, indx):
        
        counter = indx
        while( (2*(counter+1) < self.current_size) and (self.heap[counter] > self.heap[2*counter+1] or self.heap[counter] > self.heap[2*counter+2]) ):
            
            if (self.heap[2*counter+1] < self.heap[2*counter+2]):
                self.heap[counter], self.heap[2*counter+1] = self.heap[2*counter+1], self.heap[counter]
                counter = 2*counter+1
            
            else:
                self.heap[counter], self.heap[2*counter+2] = self.heap[2*counter+2], self.heap[counter]
                counter = 2*counter+2
        
    
    def del_root(self):
    
        self.heap[0] = self.heap[self.current_size-1]
        self.heap.pop()
        self.current_size -= 1
        self.perc_down(0)
        
    
    def build_heap(self, alist):
        
        indx = (len(alist) // 2) - 1
        print(indx)
        
        self.current_size = len(alist)
        self.heap = alist
        while (indx >= 0):
            self.perc_down(indx)
            indx = indx - 1
        
    def depth(self):
        return int(np.ceil(np.log2(self.current_size)))
