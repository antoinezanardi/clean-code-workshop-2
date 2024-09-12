class OrderProcessor:
    def process_regular_order(self, order):
        self.validate_order(order)
        self.calculate_totals(order)
        self.apply_discounts(order)
        self.save_order(order)

    def process_bulk_order(self, order):
        self.validate_order(order)
        self.calculate_totals(order)
        self.apply_bulk_discounts(order)
        self.save_order(order)

    def process_subscription_order(self, order):
        self.validate_order(order)
        self.calculate_totals(order)
        self.apply_subscription_discounts(order)
        self.save_order(order)

    def validate_order(self, order):
        # validation logic

    def calculate_totals(self, order):
        # total calculation logic

    def apply_discounts(self, order):
        # discount logic for regular orders

    def apply_bulk_discounts(self, order):
        # discount logic for bulk orders

    def apply_subscription_discounts(self, order):
        # discount logic for subscription orders

    def save_order(self, order):
        # save order to database
