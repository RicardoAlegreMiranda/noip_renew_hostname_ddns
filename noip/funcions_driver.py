# Internal
from noip.paths import Paths

# Python
import time

# External Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager  # webdriver_manager


class Funcions_Driver:
    def __init__(self, headless: bool):
        opts = Options()
        if headless:
            opts.add_argument("--headless")
        opts.add_argument(f"user-agent={Paths.USER_AGENT}")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opts
        )

        self.wait = WebDriverWait(self.driver, 10)

    def get_url(self, url: str):
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            # self.driver.implicitly_wait(5)

            print("URL open", url)
        except Exception as e:
            print("exception get_url: ", e)

    def find_element(self, XPATH):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
            element = self.driver.find_element(By.XPATH, value=XPATH)
            return element
        except Exception as e:
            print(f"find_element {XPATH} fail\n {e}")
            return False

    def clic(self, XPATH):
        element = self.find_element(XPATH)
        try:
            element.click()
            print("Clic in ", XPATH)
        except:
            self._click_by_script(element, XPATH)

    def _click_by_script(self, element, xpath):
        try:

            self.driver.execute_script("arguments[0].click();", element)
            print("Clic_by_script: ", xpath)
        except Exception as e:
            print("Cant clic in: ", xpath)
            print(f"error: {str(e)}")

    def write(self, xpath, text):
        element = self.find_element(xpath)
        try:
            element.send_keys(text)
            print("Write in ", xpath)

        except Exception as e:
            print("write Exception :", e)

    def read(self, xpath):
        element = self.find_element(xpath)
        try:
            text = element.text
            print(f"read {text} in ", xpath)
            return text

        except Exception as e:
            print("write Exception :", e)

    def driver_close(self):
        self.driver.close()
        print("driver closed")
