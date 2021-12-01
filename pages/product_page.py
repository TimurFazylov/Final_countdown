from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE), "Message is not presented"

    def product_name_should_be_equal_message_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text
        assert product_name == message_name, "Product name are not equal message name"

    def product_price_should_be_equal_message_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert product_price == message_price, "Product name are not equal message name"
