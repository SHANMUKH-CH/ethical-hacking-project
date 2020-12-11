class bank_account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return f'account owner:{self.owner}, balance:{self.balance}'
    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print('withdrawal successful')
        else:
            print('withdrawal failed')
    def deposit(self, dep_amoount):
        self.balance += dep_amoount
        print('deposit was accpeted! ')
if __name__ == '__main__':
    account1 = bank_account('shan', 100)
    account2 = bank_account('sai', 200)
    print(account1)
    print(account2)
    print(account1.owner)
    print(account1.balance)
    account1.deposit(50)
    account1.withdraw(200000)