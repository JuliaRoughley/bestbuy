from abc import ABC, abstractmethod
import products


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * ((100 - self.percentage) / 100)


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        if quantity % 2 == 0:
            return product.price * 0.75 * quantity

        return (product.price * 0.75 * (quantity - 1)) + product.price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        num_discounted = quantity // 3
        total_price = (quantity - num_discounted) * product.price
        return total_price
