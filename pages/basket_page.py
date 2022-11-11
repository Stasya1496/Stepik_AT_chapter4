from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_message(self):
        # Поверка, что есть сообщение Your basket is empty.
        message = self.browser.find_elements(*BasketPageLocators.EMPTY_MESSAGE)[0].text
        assert 'Ваша корзина пуста' in message, "basket isn't empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_HEADER), \
            "There are products in the basket"

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'basket' in self.browser.current_url

    def should_be_basket_header(self):
        # Поверка, что есть загловок "Корзина"
        header = self.browser.find_elements(*BasketPageLocators.BASKET_HEADER)[0].text
        assert header == 'Корзина', "This page doesn't contain header 'Корзина'"
