#Sep 12 Notes

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error


#use __somthing to assign a private property
#why is it called private property?
#   ————because it can only be called in class instead of using or calling it from the outside.