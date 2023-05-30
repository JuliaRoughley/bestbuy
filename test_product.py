import pytest
from products import Product


def test_normal_product_instantiation():
    """Test that creating a normal product works."""
    item = Product("Windows laptop", price=560, quantity=50)
    assert item is not None
    assert item.name == "Windows laptop"
    assert item.price == 560
    assert item.quantity == 50


def test_name_invalid_product_instantiation():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(ValueError):
        item = Product("", 50, 50)


def test_price_invalid_product_instantiation():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(ValueError):
        item = Product("Valid name", -50, 50)


def test_quantity_invalid_product_instantiation():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(ValueError):
        item = Product("Valid name", 50, -50)


def test_inactive_product():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    item = Product("Windows laptop", price=560, quantity=50)
    item.buy(50)
    assert item.active == False


def test_product_purchase():
    """Test that product purchase modifies the quantity and returns the right output."""
    item = Product("Windows laptop", price=560, quantity=50)
    item.buy(25)
    assert item.quantity == 25


def test_excess_quantity():
    """Test that buying a larger quantity than exists invokes exception."""
    item = Product("Windows laptop", price=560, quantity=50)
    with pytest.raises(ValueError):
        item.buy(60)


pytest.main()