from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_to_basket_form.click()

    def should_be_add_to_basket_form(self):
        # Проверка, что есть кнопка добавления в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), "Add to basket form is not presented"

    def should_be_add_the_right_product(self):
        # Проверка, что в сообщении о добавлении продукта указан нужный продукт
        product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET_PRODUCT_NAME).text
        add_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == add_product_name, "Add to basket product isn't right"

    def should_be_right_cost_of_product(self):
        # Проверка, что в сообщении о добавлении продукта указан нужный продукт
        assert self.browser.find_element(
            *ProductPageLocators.MESSAGE_COST_OF_BASKET).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_COST).text, "Add to basket cost isn't right"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message doesn't disappeared"
