from myclass import Color
class Mybox:
     def __init__( self,color):
        self.color = []
     def __len__(self):
        return len(self.color)
     def add(self,item):
        self.color.append(item)
     def remove(self):
        return self.color.pop()
     def __contains__(self,item):
        if item in self.color: 
            return True
        else:
            return False
     def __iter__(self):
            return Mybox (self.color)
     


