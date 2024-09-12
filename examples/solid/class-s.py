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


class OrderRepository:
    def save_to_database(self, order):
        # Simulating database save
        print(f"Saving order {order.id} for customer {order.customer}")


class EmailService:
    def send_confirmation_email(self, order):
        # Simulating sending email
        print(f"Sending confirmation email to {order.customer}")


order = Order(1, "john.doe@example.com", [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 1}])
print(f"Total: {order.calculate_total()}")

order_repository = OrderRepository()
order_repository.save_to_database(order)

email_service = EmailService()
email_service.send_confirmation_email(order)
