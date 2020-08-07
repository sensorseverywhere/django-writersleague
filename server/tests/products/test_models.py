import pytest
from products.models import Category, Plan, Product, Review
from user.models import CustomUser


@pytest.mark.django_db
def test_product_model(client):
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


@pytest.mark.django_db
def test_category_model(client):
    cat = Category(
        name="Test Category",
        description="This is a category",
        active=True,

    )
    cat.save()
    assert cat.name == "Test Category"
    assert cat.description == "This is a category"
    assert cat.active == True
    assert str(cat) == cat.name


@pytest.mark.django_db
def test_plan_model(client):
    p = Plan(
        name="Test Plan",
        text="This is a Plan",
        price=1.00,

    )
    p.save()
    assert p.name == "Test Plan"
    assert p.text == "This is a Plan"
    assert p.price == 1.00
    assert str(p) == p.name


@pytest.mark.django_db
def test_review_model(client):
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
    r = Review(
        author=user,
        product=product,
        rating=5,
        comment="This is a Review",
    )
    r.save()
    assert r.rating == 5
    assert r.comment == "This is a Review"
    assert str(product) == product.name
