#5) Take input of age of 3 people by user and determine oldest and youngest among them.


person1= int(input("person1"))
person2= int(input("person2"))
person3= int(input("person3"))

# oldest
if (person1 > person2):
   if (person1 > person3):
      print("oldest:",person1)
   else:   
      print("oldest:",person3)
else:
   if (person2 > person3):
      print("oldest:",person2)
   else:   
      print("oldest:",person3)      

# youngest
if (person1 < person2):
   if (person1 < person3):
      print("youngest:",person1)
   else:   
      print("youngest:",person3)
else:
   if (person2 < person3):
      print("youngest:",person2)
   else:   
      print("youngest:",person3)            
