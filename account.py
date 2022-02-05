class Account:

    def __init__(self, num, name, bal):
        self.accountNo = num
        self.ownerName = name
        self.balance = bal

    def deposit(self,money):
        self.balance += money

    def withdraw(self,money):
        self.balance -=money

    def printAccount(self):
        print('계좌번호 : '+self.accountNo)
        print('예금주 이름 : '+ self.ownerName)
        print('잔액 : '+str(self.balance)+'\n')


obj1 = Account('111-222-33333', '정수아', 50000)
obj2 = Account('555-666-77777777', '손이안', 100000)

obj1.deposit(100000)
obj2.withdraw(30000)

obj1.printAccount()

obj2.printAccount()


