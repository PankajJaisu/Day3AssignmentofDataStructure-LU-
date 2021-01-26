class add:
    def operation(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print("Additon:",c)
ob=add()
in1=int(input("Enter 1st Number:"))
in2=int(input("Enter 2nd Number:"))
ob.operation(in1,in2)