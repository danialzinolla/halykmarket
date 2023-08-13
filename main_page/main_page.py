from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from base_page.base_page import BasePage


class MainPage(BasePage):
        url = "https://halykmarket.kz/"
        search_input = (By.CLASS_NAME, "search-input")
        search_result = (By.CLASS_NAME, "category-page-title")
        product_click = (By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div/div/div/div[2]/div[1]/a")
        product_title = (By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/section/h1")
        favorite_button = (By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/button[2]")
        link_favorite = (By.XPATH, "/html/body/div[1]/div/div/header/div[2]/div/div[3]/a[1]/div/div")
        find_favorite_product = (By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div/a")
        price_product = (By.CLASS_NAME, "product-card-value-value")
        price_search = (By.CLASS_NAME, "product-card-value-value")

        def open(self):
            self.driver.get(self.url)
            if "Halyk Market" not in self.driver.title:
                print("Failed to open Halyk Market page.")

        def search_for_product(self, product_name):
            try:
                search_input = self.wait_for_element(self.search_input)
                search_input.clear()
                search_input.send_keys(product_name)
                search_input.submit()
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while searching for the product.")

        def check_search_results(self):
            try:
                self.wait_for_element(self.search_result)
                return True
            except TimeoutException:
                return False

        def find_product(self, product_name):
            search_results = self.wait_for_elements(self.search_result)
            for result in search_results:
                if product_name in result.text:
                    return result
            return None

        def click_product(self):
            try:
                product_element = self.wait_for_element(self.product_click)
                product_element.click()
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while clicking on the product.")

        def get_product_title(self):
            try:
                product_title_element = self.wait_for_element(self.product_title)
                return product_title_element.text
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while getting the product title.")
                return None

        def find_favorite_button(self):
            try:
                return self.wait_for_element(self.favorite_button)
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while finding the favorite button.")
                return None

        def click_favorite_button(self):
            try:
                fav_button = self.find_favorite_button()
                fav_button.click()
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while clicking the favorite button.")

        def favorite_button_enabled(self):
            try:
                fav_button = self.find_favorite_button()
                return fav_button.is_enabled()
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while checking if the favorite button is enabled.")
                return False

        def click_favorite_link(self):
            try:
                link_fav_element = self.wait_for_element(self.link_favorite)
                link_fav_element.click()
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while clicking the link to favorite.")

        def is_product_favorite(self, product_name):
            try:
                return product_name in self.driver.page_source
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while checking if the product is favorite.")
                return False

        def find_fav_product(self):
            try:
                return self.wait_for_element(self.find_favorite_product)
            except (TimeoutException, NoSuchElementException):
                print("An error occurred while finding the favorite product.")
                return None

        def is_favorite_product_displayed(self):
            try:
                fav_product_element = self.find_fav_product()
                return fav_product_element.is_displayed()
            except NoSuchElementException:
                return False

        def get_favorite_product_name(self):
            try:
                fav_product_element = self.wait_for_element(self.find_favorite_product)
                return fav_product_element.text
            except NoSuchElementException:
                return None

        def get_product_price_in_search_results(self):
            try:
                price_el = self.wait_for_element(self.price_product)
                return price_el.text
            except NoSuchElementException:
                return None

        def get_product_price_search(self):
            try:
                price_elem = self.wait_for_element(self.price_search)
                return price_elem.text.strip()
            except NoSuchElementException:
                return None

        def get_product_price(self):
            try:
                price_element = self.wait_for_element(self.price_product)
                return price_element.text.strip()
            except NoSuchElementException:
                return None