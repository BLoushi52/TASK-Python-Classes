class Wallet:
    def __init__(self, money):
        self.money = money
        

    def credit(self, amount):
        money = self.money + amount
        print(f"Amount in wallet is {money}")

    def debit(self, amount):
        money = self.money - amount
        print(f"Amount in wallet is {money}")


wallet = Wallet(0)  # This should default money inside the wallet to 0
#print(wallet.credit(2))    #Testing


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location =  location
        self.wallet = Wallet(money)
    
    def moveTo(self, point):
        self.location = point
        print(f"New location has been set to {self.location}")


person = Person("Moh", 5, 50)
# print(person.moveTo(2))   #Testing

class Vendor:
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        customer.location = person.location
        # moveTo(self,customer.location )
        customer.wallet.debit(number_of_icecreams * self.price)
        self.wallet.credit(number_of_icecreams * self.price)
        

    # implement Vendor!
    


vendor = Vendor("Abdallah", 3, 6)


class Customer:
    # implement Customer!
    pass


# customer = Customer("Abdallah", 3, 6)
