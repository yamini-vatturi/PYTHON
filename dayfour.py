class person:
    def __init__(self,name,age):
      self.name = name
      self.age = age
    
    def __str__(self):
        return f"{self.name},{self.age} years old"
person = person("yamini",17)
print(person)
