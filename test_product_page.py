import time
import pytest

from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# @pytest.mark.parametrize('promo', range(10))
# def test_for_all(browser, promo):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_product_name()
#     product_page.should_be_product_price()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_be_message()
#     product_page.product_name_should_be_equal_message_name()
#     product_page.product_price_should_be_equal_message_price()
#
#
# def test_guest_can_add_product_to_basket(browser):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_product_name()
#     product_page.should_be_product_price()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.should_be_message()
#
#
# def test_product_name_is_equal_message_name(browser):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_product_name()
#     product_page.should_be_product_price()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.product_name_should_be_equal_message_name()
#
#
# def test_product_price_is_equal_message_price(browser):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_product_name()
#     product_page.should_be_product_price()
#     product_page.add_to_basket()
#     product_page.solve_quiz_and_get_code()
#     product_page.product_price_should_be_equal_message_price()


@pytest.mark.xfail
def test_guest_cant_see_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_disappeared_message()
