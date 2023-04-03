class MySet:
    def __init__(self, items = None):
        """Initializes MySet object with optional starting collection items"""
        self.buckets = [[]for _ in range(8)]    #create the bucket containers 
        self.bucket_size = len(self.buckets)    #get the size of all the buckets 
        self.size = 0                           
        if items is not None:                   #if items are passed put them into a bucket
            for item in items:
                self.put(item)

    def __len__(self):
        """Returns number of items in MySet"""
        return self.size                        #returns the number of items within the set
    
    def __repr__(self):
        """returns a string representation of MySet"""
        items = [str(item) for item in self.buckets]    #Iterate through buckets
        return "MySet ({" +  ", ".join(items) + "})"    #Return a concacated list of all items in buckets
    
    def __iter__(self):
        return iter(self.items)
    
    def __eq__(self, other):
        """returns True (False) if self and other do (do not) contain exactly the same items"""
        if len(self) != len(other):                     #check if the two sets have the same amount of items
            return False
        # Get items in self
        self_items = []                                 #Initialize an empty list
        for bucket in self.buckets:                     #Iterate through buckets
            self_items += bucket                        #add to self_items
            
        # Get items in other
        other_items = []                                #same as above but with other
        for bucket in other.buckets:
            other_items += bucket
        
    # Compare the items in self and other
        for item in self_items:                         #compare item of self_items with item of other_items
            if item not in other_items:                 #if items aren't contained in both list return false
                return False
        return True                                     #if sets are identical return True
        
    def _get_bucket(self, key):
        """ returns bucket (or index of bucket) for key """
        return hash(key) % len (self.buckets)           #return the hashing location

    def put(self, item):
        """adds item to MySet. Duplicate items will only be stored once."""
        bucket = self._get_bucket(item)                 #get a bucket to store item
        if item not in self.buckets[bucket]:            #check if it isn't already stored, append and add to size
            self.buckets[bucket].append(item)           
            self.size += 1
            if self.size > self.bucket_size * 0.7:      #if the size of items is bigger than bucket, double size of bucket 
                self._rehash(self.bucket_size * 2)

    def remove(self, item):
        """ removes item from MySet. If item is not in set, raise a KeyError"""
        bucket = self._get_bucket(item)                 #call up bucket item
        try:
            self.buckets[bucket].remove(item)           #try to remove bucket item
            self.size -= 1                              #reduce size by 1
        except ValueError:
            raise KeyError(item)                        #raise key error if buckets are empty
        
    def __contains__(self, item):
        """returns True (False) if an item is (is not) in MySet"""
        bucket = self._get_bucket(item)                 #get bucket item
        return item in self.buckets[bucket]             #return if item is in bucket

    def _rehash(self, new_size):
        """rehashes MySet to have new_size buckets"""
        old_buckets = self.buckets                      #cache current bucket list into old_buckets
        self.bucket_size = new_size                     #set bucket size to the current size
        self.size = 0                                   #Reset size 
        self.buckets = [[] for i in range(new_size)]    #create buckets for the new_size variable
        for bucket in old_buckets:                      #place items from old bucks into new buckets
            for item in bucket: 
                self.put(item)
    
    

    
        

