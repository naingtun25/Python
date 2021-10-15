class Students:
    count = 0;

    def __init__(self):
        Students.count += 1
    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def program(self):
        print(self.name)

koko = Students()
koko.setname("koKo")
print(koko.name)
print(koko.count)





