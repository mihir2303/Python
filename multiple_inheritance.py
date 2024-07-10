class calc1():
    def sum(self,a,b):
        return a + b

class calc2():
    def mul(self,a,b):
        return a * b
    
class calc3():
    def div(self,a,b):
        return a / b
    
c= calc3()
print(c.sum(10,20))
print(c.sub(10,20))
print(c.mul(10,20))
print(c.div(10,20))