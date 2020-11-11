import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5}, 'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}

    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePraice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculatetotalPurePriceTaxed(invoice, products):
    invoice.totalPurePriceTaxed(products)
    assert invoice.totalPurePriceTaxed(products) == 74.24

def test_CanCalculateSingleItemDiscountedPrice(invoice, products):
    invoice.singleProductDiscountedPrice(products, 'Pen')
    assert invoice.singleProductDiscountedPrice(products, 'Pen') == 3.56