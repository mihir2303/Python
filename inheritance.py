class abc():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def Display(self):
        print(self.name,self.id)
        
nm=abc("ABCD",101)
nm.Display()