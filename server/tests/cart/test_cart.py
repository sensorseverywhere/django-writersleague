import pytest
from cart.cart import Cart
from user.models import CustomUser
from products.models import Product


@pytest.mark.django_db
def test_add_to_cart(client):
    user = CustomUser.objects.create_user(
        "test@test.com",
    )

    product = Product(
        name="Test Product",
        description="This is a product",
        price=1.00,
        stock_qty=5,
        active=True,
        in_stock=True 
    )
    product.save()
    assert product.name == "Test Product"
    assert product.description == "This is a product"
    assert product.price == 1.00
    assert str(product) == product.name