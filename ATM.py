class ATM:
    def __init__(self,inamt):
        self.inamt=inamt

    def atm(self):
        w=int(input("Enter the amount to withdraw: "))
        self.inamt=self.inamt-w
        print(f"Remaining balance: {self.inamt}")
        d=int(input("Enter the amount to deposit: "))
        self.inamt=self.inamt+d
        print(f"Updated balance: {self.inamt}")
inamt=50000
obj=ATM(inamt)
obj.atm()