class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Invalid name, name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be less than 0")
        if quantity < 0:
            raise ValueError("Invalid quantity, quantity cannot be negative.")
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True
        self.promotion = None

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate_self(self):
        self.active = True

    def deactivate_self(self):
        self.active = False

    def show(self) -> str:
        product_desc = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return product_desc

    def buy(self, quantity) -> float:
        if quantity <= 0 or quantity > self.quantity:
            raise ValueError("Invalid quantity")

        total_price = self.calculate_total(quantity)
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate_self()
        return total_price

    def calculate_total(self, quantity):
        total_price = 0
        if self.promotion is None:
            total_price = quantity * self.price
        else:
            total_price = self.promotion.apply_promotion(self, quantity)

        return total_price

    def set_promotion(self, promotion):
        self.promotion = promotion


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity <= 0 or quantity > self.quantity or quantity > self.maximum:
            raise ValueError("Invalid quantity")
        total_price = super().buy(quantity)
        return total_price

    def show(self):
        return f"{super().show()}, Limited Stock Product, Maximum: {self.maximum}"


class NonStockProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        raise AttributeError("Cannot change the quantity of non-physical product.")

    def show(self):
        return f"{super().show()}, Non-Stocked Product"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Invalid quantity")
        total_price = self.calculate_total(quantity)
        return total_price
