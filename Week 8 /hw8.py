class MySet:
    def __init__(self, items = None):
        """Initializes MySet object with optional starting collection items"""
        self.buckets = [[]for _ in range(8)]
        self.bucket_size = len(self.buckets)
        self.size = 0
        if items is not None:
            for item in items:
                self.put(item)

    def __len__(self):
        """Returns number of items in MySet"""
        return self.size
    
    def __repr__(self):
        """returns a string representation of MySet"""
        items = [str(item) for item in self.buckets]
        return "MySet ({" +  ", ".join(items) + "})"
    
    def __iter__(self):
        return iter(self.items)
    
    def __eq__(self, other):
        """returns True (False) if self and other do (do not) contain exactly the same items"""
        if len(self) != len(other):
            return False
        # Get items in self
        self_items = []
        for bucket in self.buckets:
            self_items += bucket
            
        # Get items in other
        other_items = []
        for bucket in other.buckets:
            other_items += bucket
        
    # Compare the items in self and other
        for item in self_items:
            if item not in other_items:
                return False
        return True
        
    def _get_bucket(self, key):
        """ returns bucket (or index of bucket) for key """
        return hash(key) % len (self.buckets)

    def put(self, item):
        """adds item to MySet. Duplicate items will only be stored once."""
        bucket = self._get_bucket(item)
        if item not in self.buckets[bucket]:
            self.buckets[bucket].append(item)
            self.size += 1
            if self.size > self.bucket_size * 0.7:
                self._rehash(self.bucket_size * 2)


    def remove(self, item):
        """ removes item from MySet. If item is not in set, raise a KeyError"""
        bucket = self._get_bucket(item)
        try:
            self.buckets[bucket].remove(item)
            self.size -= 1
        except ValueError:
            raise KeyError(item)
        
    def __contains__(self, item):
        """returns True (False) if an item is (is not) in MySet"""
        bucket = self._get_bucket(item)
        return item in self.buckets[bucket]

    def _rehash(self, new_size):
        """rehashes MySet to have new_size buckets"""
        old_buckets = self.buckets
        self.bucket_size = new_size
        self.size = 0
        self.buckets = [[] for i in range(new_size)]
        for bucket in old_buckets:
            for item in bucket:
                self.put(item)
    
    

    
        

