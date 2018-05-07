#create a ADT called hashtable
class HashTable:
    
    def __init__(self, prime):
        
        self.size = prime
        self.keys = [None]*self.size
        self.vals = [None]*self.size
        
    def hashfunct(self, key, size):
        return key**29 % size
    
    def rehash(self, oldhash, i, size):
        #return (oldhash+i**2) % size
        #return (oldhash + np.random.randint(low = 0, high = 298)) % size
        return (oldhash + 1) % size
        
    
    def put(self, key, val):
        hashval = self.hashfunct(key,len(self.keys))
        
        if (self.keys[hashval] == None):
            self.keys[hashval] = key
            self.vals[hashval] = val
        elif (self.keys[hashval] == key):
            self.vals[hashval] = val
        else:
            list_size = len(self.keys)

            hashval = self.rehash(hashval,0,list_size)
            counter = 1
            not_found = True
            
            while( not_found and counter < list_size ):
                if( self.keys[hashval] == None ):
                    not_found = False
                    self.keys[hashval] = key
                    self.vals[hashval] = val
                    
                elif( self.keys[hashval] == key):
                    not_found = False
                    self.vals[hashval] = val
                    
                else:
                    print("Collision has occured for key " + str(key))
                    notfound = False
                    break
                    #hashval = self.rehash(hashval, counter, list_size)
                    #counter += 1
                    
            if (not_found):
                print("ERROR: No empty spot can be found to put " + str((key,val)) + " (key, value) pair")
                return
        
        return
        
    def __setitem__(self, key,val):
        self.put(key,val)
        
        
    def get(self, key):
        
        hashval = self.hashfunct(key, len(self.keys))
        counter = 0
        found = False
        
        while( counter < len(self.keys) and found == False):
            if (self.keys[hashval] == key):
                found = True
                return self.vals[hashval]
            else:
                counter += 1
                hashval = self.rehash(hashval, counter, len(self.keys))        
        
        if (found == False):
            print("ERROR: No such key " + str(key) + " exists.")
            return
        
    def __getitem__(self,key):
        return self.get(key)
        
    def is_in(self, key):
        
        hashval = self.hashfunct(key, len(self.keys))
        counter = 0
        found = False
        
        while (counter < len(self.keys) and found == False):
            if (self.keys[hashval] == key):
                found = True
            else:
                counter += 1
                hashval = self.rehash(key, counter, len(self.keys))
                
        if (found):
            #print ("The key " + str(key) + " does exist in the table.")
            return found
            
        else:
            #print ("The key " + str(key) + " does not exist in the table.")
            return found
            
    def __contains__(self, key):
        return self.is_in(key)
    
    def length(self):
        counter = 0
        for key in self.keys:
            if (key != None):
                counter += 1
        return counter
    
    def __len__(self):
        return self.length()
            
