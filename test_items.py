import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed()
