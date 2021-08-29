class Father():
    def Firstname(self):
        print("Mg")

class Mother():
    def Middlename(self):
        print("Naing")

class Son(Father, Mother):
    def Lastname(self):
        print("Tun")
s1=Son()
s1.Firstname()
s1.Middlename()
s1.Lastname()