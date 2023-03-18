class BankAccount:
    def __init__(self, name, money, address):
        self.name = name #public
        self.__money = money #private
        self.address = address

    def getMoney(self):
        return self.__money
    def setMoney(self, amount):
        self.__money = amount
    def __increase(self):
        self.__money = self.__money + 1500

person1 = BankAccount("Messi", 5000, "Argentina")
person2 = BankAccount("Ronaldo", 4000, "Portugal")
print("get method: ", person1.getMoney())
#print("get method: ", person1.__money()) because "money" is private
person1.setMoney(8000)
print("set method: ", person1.getMoney())
#person2.increase()
# person2.__increase()
# print("after increase: ", person2.getMoney())