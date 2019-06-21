import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

EXPLICIT_WAIT_TIME = 5

class Reporter():
    def __init__(self, driver):
        self.driver = driver

    def allure_attach_snapshot(self):
        try:
            import allure
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        # pylint: disable=W0703;
        # pylint: disable=W0612;
        except Exception as err:
            # Exception will be ignored if allure is ginore
            pass


    def additional_wait(self, seconds):
        time.sleep(seconds)

    def verify_webpage_title(self, title_name):
        try:
            bool_element_visible = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(
                EC.title_contains(title_name)
            )
            return bool_element_visible
        except Exception as err:
            self.allure_attach_snapshot()
            displayed_title = self.driver.title
            raise Exception(
                'Expected title %s not displayed, displayed title is - %s. Error message is - %s'
                %(title_name, displayed_title, err))

    def check_element_and_click(self, xpath):
        try:
            web_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            if web_element:
                web_element.click()
            else:
                self.allure_attach_snapshot()
                raise Exception('Unable to click the expected element.')
        except Exception as err:
            self.allure_attach_snapshot()
            raise Exception('Element click failed with an err. - '+err)

    def mouse_hover_on_element(self, xpath):
        try:
            web_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            if web_element:
                hover = ActionChains(self.driver).move_to_element(web_element)
                hover.perform()
            else:
                self.allure_attach_snapshot()
                raise Exception('Unable to find visibility of the element')
        except Exception as err:
            self.allure_attach_snapshot()
            raise Exception('Mouse hover on the element failed with error -'+ err)

    def switch_to_new_window_and_verify(self, window_id):
        try:
            self.driver.switch_to.window(self.driver.window_handles[int(window_id)])
        except Exception as err:
            self.allure_attach_snapshot()
            raise Exception('Switch to new window_failed.'+ err)

    def check_element_and_send_keys(self, xpath, value):
        try:
            web_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            if web_element:
                web_element.send_keys(value)
            else:
                self.allure_attach_snapshot()
                raise Exception('Unable to find visibility of the element')
        except Exception as err:
            self.allure_attach_snapshot()
            raise Exception('sending keys to xpath failed with err - '+err)
