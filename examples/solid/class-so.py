from abc import ABC, abstractmethod

class Order:
    def __init__(self, id, customer, items):
        self.id = id
        self.customer = customer
        self.items = items
        self.discount = None

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        if self.discount:
            total -= self.discount.apply_discount(total)
        return total

    def set_discount(self, discount):
        self.discount = discount


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass


class NoDiscount(Discount):
    def apply_discount(self, total):
        return 0


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total * (self.percentage / 100)


order = Order(1, "john.doe@example.com", [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 1}])
order.set_discount(PercentageDiscount(10))
print(f"Total: {order.calculate_total()}")
