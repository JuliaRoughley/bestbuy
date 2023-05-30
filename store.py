class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products:
                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"A problem occurred placing your order: {e}")
            else:
                print(f"Product {product.name} is not available in the store.")
        return total_price
