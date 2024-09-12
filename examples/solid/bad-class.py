class Order:
    def __init__(self, id, customer, items):
        self.id = id
        self.customer = customer
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def save_to_database(self):
        # Simulating database save
        print(f"Saving order {self.id} for customer {self.customer}")

    def send_confirmation_email(self):
        # Simulating sending email
        print(f"Sending confirmation email to {self.customer}")


order = Order(1, "john.doe@example.com", [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 1}])
print(f"Total: {order.calculate_total()}")
order.save_to_database()
order.send_confirmation_email()
