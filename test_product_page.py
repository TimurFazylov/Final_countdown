import time

from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_book_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(600)
