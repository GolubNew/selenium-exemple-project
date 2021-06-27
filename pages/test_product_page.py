import pytest

from pages.product_page import ProductPage

link_promo_new_year = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_available_item = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                              "?promo=offer4", "?promo=offer5", "?promo=offer6",
                              pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
                              "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        link = link_available_item + promo_offer
        page = ProductPage(browser, link)
        # Act
        page.open()
        page.add_to_basket_product()
        page.solve_quiz_and_get_code()
        # Assert
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()