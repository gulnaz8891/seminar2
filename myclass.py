class Rectangle:
   def __init__(self, color="red", width=50, height=50):
       self.color = color
       self.a = width
       self.b = height
   def square(self):
       return self.a * self.b
   def perimetr(self):
       return (self.a + self.b)*2

class Color(Rectangle):
     def __len__(self):
      return len(self.color)

c = Color(['pink','red'])

if __name__=="__main__":
   R = Rectangle()
   print("color:", R.color)
   print("square:", R.square())
   print("perimetr:",R.perimetr())
   R1 = Rectangle("pink", 20, 50)
   print("color:", R1.color)
   print("square:", R1.square())
   print("perimetr:",R1.perimetr())
   print(len(c))

  

  
   
  


