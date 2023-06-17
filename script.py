#pesquise um site no google e o abra usando selenium
#pesquise um site no google e o abra usando selenium

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class DenverUniversityTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(2)

        self.browser.get("https://www.du.edu")
        cookie = self.browser.find_element(By.XPATH, '//*[@id="c-right"]/a').click()

        self.addCleanup(self.browser.quit)

    # scrolla ate um botao, verifica se ele esta sendo mostrado, verifica o titulo dele e depois de clicar, verifica se levou ao lugar certo
    def test_button_click(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/form/div[2]/div[2]/div[1]/button')

        actions = ActionChains(self.browser)
        actions.scroll_to_element(button).perform()
        
        self.assertTrue(button.is_displayed())
        self.assertTrue(button.get_attribute('title') == "Search Undergraduate Programs")

        button.click()
        time.sleep(2)

        self.assertIn('https://www.du.edu/academics/undergraduate-programs?search=', self.browser.current_url)
        time.sleep(2)

        # pesquisa AMOGUS
    #     string = 'AMOGUS'
    #     search = self.browser.find_element(By.ID, 'search-input')
    #     actions.scroll_to_element(search).perform()
    #     search.send_keys(string + Keys.RETURN)
    #     time.sleep(2)

    #     # apaga AMOGUS e pesquisa alan turing filho
    #     search = self.browser.find_element(By.ID, 'search-input')
    #     actions.scroll_to_element(search).perform()

    #     for i in range (len(string)):
    #         search.send_keys(Keys.BACKSPACE)
    #         time.sleep(0.2)
    #     search.send_keys('computer science' + Keys.RETURN)
    #     time.sleep(1)

    #     hiddenMenu = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div/div/div[7]')
    #     actions.scroll_to_element(hiddenMenu).perform()
    #     hiddenMenu.click()
    #     time.sleep(1)

    #     gamedev = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div/div/div/div[7]/div/div[2]/div/div[2]/ul/li[2]/a')
    #     actions.scroll_to_element(gamedev).perform()
    #     gamedev.click()

    #     time.sleep(2)

    # def test_testa(self):
    #     coisa = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[6]/div/div/div/div[2]/div/p[2]/a')
    #     actions = ActionChains(self.browser)
    #     actions.scroll_to_element(coisa).perform()
    #     coisa.click()
    #     time.sleep(2)

if _name_ == '_main_':
    unittest.main(verbosity=2)