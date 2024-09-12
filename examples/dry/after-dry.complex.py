class OrderProcessor:
    def process_order(self, order, discount_strategy):
        self.validate_order(order)
        self.calculate_totals(order)
        discount_strategy.apply_discounts(order)
        self.save_order(order)

    def validate_order(self, order):
        # validation logic

    def calculate_totals(self, order):
        # total calculation logic

    def save_order(self, order):
        # save order to database

class RegularDiscountStrategy:
    def apply_discounts(self, order):
        # discount logic for regular orders

class BulkDiscountStrategy:
    def apply_discounts(self, order):
        # discount logic for bulk orders

class SubscriptionDiscountStrategy:
    def apply_discounts(self, order):
        # discount logic for subscription orders

# Usage
order_processor = OrderProcessor()
order_processor.process_order(order, RegularDiscountStrategy())
order_processor.process_order(order, BulkDiscountStrategy())
order_processor.process_order(order, SubscriptionDiscountStrategy())
