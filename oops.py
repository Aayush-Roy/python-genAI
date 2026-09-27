class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    def orderSummary(self):
        return f"{self.size}ml of {self.type}"

order = ChaiOrder("Masala",200)
print(order.orderSummary())
        