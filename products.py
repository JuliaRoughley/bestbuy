class Product:

    def __init__(self, name, price, quantity):
        try:
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
        except ValueError as value_error:
            print(f"Error creating product: {value_error}")

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
        total_price = quantity * self.price
        self.quantity -= quantity
        return total_price


