class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer Name: {self.name}, Address: {self.address}"





customer = Customer("Chris Hemsworth", "MUKONO")
print(customer.toString())
