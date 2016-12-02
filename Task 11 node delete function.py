class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
 
class List(object):
  def __init__(self):
      self.head=None
      self.tail=None
    
  def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x              
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x
            
  def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print ("List: ",",".join(values))
    
  def delete(self, value):
      if value.prev != None:
          value.prev.next = value.next
      else:
          self.head = value.next
      if value.next != None:
          value.next.prev = value.prev
      else:
          self.tail = value.prev
    
    
     
if __name__ == '__main__':
  l=List()
  a = (Node(4))
  b = (Node(6))
  c = (Node(8))
  l.insert(None, a)
  l.insert(l.head, b)
  l.insert(l.head, c)
  l.display()
  l.delete(b) 
  l.display()
