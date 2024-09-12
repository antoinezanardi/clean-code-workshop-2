class OrderProcessor:
    def __init__(self, order_repository, email_service):
        self.order_repository = order_repository
        self.email_service = email_service

    def process_order(self, order):
        total = order.calculate_total()
        print(f"Total: {total}")
        self.order_repository.save_to_database(order)
        self.email_service.send_confirmation_email(order)


# Dependency Injection
order_repository = OrderRepository()
email_service = EmailService()
order_processor = OrderProcessor(order_repository, email_service)

order = Order(1, "john.doe@example.com", [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 1}])
order.set_discount(PercentageDiscount(10))
order_processor.process_order(order)
