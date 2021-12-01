from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "This is not basket page!"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket with items, but should not be"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is empty, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Basket empty message is not presented, but should be"

    def should_not_be_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Basket empty message is presented, but should not be"
