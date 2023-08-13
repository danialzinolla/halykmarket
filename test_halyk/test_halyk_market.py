import pytest
from pytest_bdd import given
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from main_page.main_page import MainPage
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given("I am on the Halyk Market homepage") #попозже
def test_halykmarket(driver):
    # Инициализация страницы
    page = MainPage(driver)
    page.open()

    # Проверка заголовка страницы
    assert "Halyk Market - Выгодные покупки в рассрочку" in driver.title

    product_name = "iPhone 14 Pro 128 Deep Purple"
    product_name_with_gb = product_name.replace("128", "128Gb")
    product_page_title = f"Смартфон Apple {product_name_with_gb}"

    # Поиск товара
    page.search_for_product(product_name)
    assert page.check_search_results()

    # Поиск и проверка результата поиска
    product_result = page.find_product(product_name)
    assert product_result is not None
    assert product_name in product_result.text

    # Переход на страницу продукта
    page.click_product()
    product_page = MainPage(driver)

    # Проверка заголовка продукта
    title_product = product_page.get_product_title()
    assert title_product in product_page_title

    # Добавление в избранное
    favorite_butt = product_page.find_favorite_button()
    assert favorite_butt.is_enabled()
    favorite_butt.click()
    time.sleep(3) #Знаю что sleep лучше не использовать, но пусть тут будет

    # Переход в раздел избранного
    page.click_favorite_link()

    # Проверка наличия товара в избранном
    assert page.is_product_favorite(product_name)
    assert page.is_favorite_product_displayed()

    # Получение имени товара в избранном
    try:
        favorite_product_name = page.get_favorite_product_name()
        expected_favorite_product_name = f"Смартфон Apple {product_name_with_gb}"
        assert expected_favorite_product_name in favorite_product_name
    except NoSuchElementException:
        print("Favorite product name element not found.")

    # Возвращение на предыдущую страницу
    try:
        driver.back()
    except TimeoutException:
        print("Timeout occurred while trying to go back.")
    time.sleep(3)

    # Проверка наличия товара на странице продукта
    assert expected_favorite_product_name in product_page.get_product_title()

    # Сравнение цен товара
    product_price_card = product_page.get_product_price()
    product_price_search = page.get_product_price_search()
    assert product_price_search == product_price_card

    # Завершение теста
    driver.quit()

