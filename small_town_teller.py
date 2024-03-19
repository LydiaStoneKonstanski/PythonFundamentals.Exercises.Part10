import pickle
class Person:
    pid = 100
    def __init__(self, first_name, last_name):
        Person.pid += 1
        self.id = Person.pid
        self.first_name = first_name
        self.last_name = last_name

def __str__(self):
    return "%d %s %s %f" % (self.id, self.first_name, self.last_name)

# def getid = pid

class Account:
    acct_number = 1500
    balance = 0.0
    def __init__(self, acct_type, owner):
        Account.acct_number +=1
        self.acct_type = acct_type
        self.owner = owner
        self.balance = Account.balance

    def __str__(self):
        return "acct_number %d: %s %s %f" % (self.pid, self.type, self.owner, self.balance)

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, cust):
        cid = cust.getid()
        if cid in self.customers:
            raise Exception("Customer already exists")
        else:
            self.customers[cid] = cust

    def remove_customer(self, acct):
        pass
    def add_account(self, acct):
        aid = acct.getid()
        if aid in self.accounts:
            raise Exception("Account already exists")
        else:
            self.accounts[acct.getid()]

    def remove_account(self, acct):
        del self.accounts[acct.getid()]

    def deposit_money(self, acctid, amt):
        self.accounts[acctid] = self.accounts[acctid].balance + amt

    def withdraw_money(self, acctid, amt):
        #exception for overdraw
        self.accounts[acctid].balance = self.accounts[acctid].balance - amt

    def balance_inquiry(self, acctid):
        print('${:,.2f}'.format(self.accounts[acctid()].balance))

    def __str__(self):
        return str(self.accounts) + str(self.customers)

    def printCustomers(self):
        for c in self.customers.items():
            print(c[1])

    def runsomething(bank):
        p1 = Person('Joe', "Blow")
        p2 = Person("Jill", "Blow")
        a1 = Account("SAVINGS", p1)
        a2 = Account("CHECKING", p2)

        bank = Bank()
        bob = Person(1, "Bob", "Smith")
        bank.add_customer(bob)
        bank.add_customer(bob)

        bank.printCustomers()

        bob_savings = Account("SAVINGS", bob)
        bank.add_account(bob_savings)
        bank.balance_inquiry(1001)
        # 0
        bank.deposit(1001, 256.02)
        bank.balance_inquiry(1001)
        # 256.02
        bank.withdrawal(1001, 128)
        bank.balance_inquiry(1001)
        # 128.02

        print(p1)

if __name__ == "__main__":

    with open('KrisBank.pickle', 'wb') as handle:
        zc_bank = pickle.load(handle)

        runsomething(zc_bank)


    zc_bank = Bank()
    bob = Person("Bob", "Smith")
    zc_bank.add_customer(bob)

    with open('filename.pickle', 'wb') as handle:
        pickle.dump(zc_bank, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('filename.pickle', 'rb') as handle:
        zc_bank2 = pickle.load(handle)
        print(zc_bank, zc_bank2)


