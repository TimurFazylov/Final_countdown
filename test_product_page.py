import pytest
import time
import random
import string

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def get_random_string():
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return result_str


@pytest.mark.skip
@pytest.mark.parametrize('promo', range(10))
def test_for_all(browser, promo):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message()
    product_page.product_name_should_be_equal_message_name()
    product_page.product_price_should_be_equal_message_price()


@pytest.mark.reg_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, url)
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(get_random_string())
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_name()
        product_page.should_be_product_price()
        product_page.add_to_basket()
        product_page.should_be_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.add_to_basket()
    product_page.should_be_message()


@pytest.mark.skip
def test_product_name_is_equal_message_name(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_should_be_equal_message_name()


@pytest.mark.skip
def test_product_price_is_equal_message_price(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_price_should_be_equal_message_price()


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


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_message()
