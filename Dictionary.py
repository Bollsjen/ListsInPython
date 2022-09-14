class Dictionary(dict):
    
    def __init__(self, mapping = None, /, **kwargs):
        if mapping != None:
            mapping = {
                str(key): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        
        if kwargs:
            mapping.update(
                {str(key): value for key, value in kwargs.items()}
            )
        super().__init__(mapping)
    
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
    
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        raise KeyError(key)
    
    def Count(self):
        return len(self)
    
    def IsEmpty(self):
        return len(self) == 0
    
    def Remove(self, key):
        del self[key]
            
    

# Help from https://realpython.com/inherit-python-dict/