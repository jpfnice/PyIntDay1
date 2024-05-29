class StackSizeError(Exception):
    pass
class StackFullError(Exception):
    pass
class StackEmptyError(Exception):
    pass

class Stack:
    def __init__(self, maxSz=10): # initialize the 2 attributes (maxi and content)
                               # Does not return anything
        if isinstance(maxSz, int) and maxSz > 0:
            self.maxi=maxSz
        else:
            raise StackSizeError("Wrong size given !!")
            
        self.content=[]
        
    def push(self, item):   # add an item at the end of the inner list
                            # "content" if the stack is not full
                            # Does not return anything
        if len(self.content)<self.maxi:
            self.content.append(item)
        else:
           raise StackFullError("Stack is full!")
            
    def __str__(self):      # Construct and return a string representing the
                            # stack
        return f"({len(self.content)}/{self.maxi}) {self.content}"
    
    def __len__(self):      # Return the current size of the inner list "content"
        return len(self.content)
    
    def pop(self):          # Remove and return the last element of the inner
                            # list "content" if content is not empty
        if len(self.content)>0:
            return self.content.pop()
        else:
            raise StackEmptyError("Stack is empty!")
        
    def peek(self):         # Return the last element of the inner
                            # list "content" if content is not empty
        if len(self.content)>0:
            return self.content[-1]
        else:
            raise StackEmptyError("Stack is empty!")
            
    def __eq__(self, other):# Return a bool: True if the self == other False if not
        return self.maxi == other.maxi and self.content == other.content
    
    def __iter__(self):
        self.ix=len(self)-1
        return self
    
    def __next__(self):
        if self.ix >= 0:
            temp=self.content[self.ix]
            self.ix -= 1
            return temp
        else:
            raise StopIteration

def sqr(a):
    return a**2

if __name__ == "__main__":
    s2=Stack(10)
    s2.push(200)
    s2.push(300)

    s2.push(56)
    s2.push(99)
    print(s2) 
    
    for e in s2:
        print(e)
        # it=s2.__iter__()
        # try:
        #     while True:
        #         e=it.__next__()
        #         print(e)
        # except StopIteration:
        #     pass    
 
#   l=list(map(lambda a:a**2, s2))
    l=list(map(sqr, s2))
    print(l)
    
    