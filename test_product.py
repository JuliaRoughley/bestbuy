import pytest
from products import Product


def test_normal_product_instantiation():
    item = Product("Windows laptop", price=560, quantity=50)
    assert item is not None
    assert item.name == "Windows laptop"
    assert item.price == 560
    assert item.quantity == 50


def test_name_invalid_product_instantiation():
    with pytest.raises(ValueError):
        item = Product("", 50, 50)


def test_price_invalid_product_instantiation():
    with pytest.raises(ValueError):
        item = Product("Valid name", -50, 50)


def test_quantity_invalid_product_instantiation():
    with pytest.raises(ValueError):
        item = Product("Valid name", 50, -50)


pytest.main()