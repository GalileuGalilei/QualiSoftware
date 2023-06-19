from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
import unittest

from urllib.parse import unquote

class DenverUniversityTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(2)

        self.browser.get("https://www.du.edu")
        cookie = self.browser.find_element(By.XPATH, '//*[@id="c-right"]/a').click()

        self.addCleanup(self.browser.quit)

    def test_search(self):
        # obtem o botao e scrolla a tela ate ele
        button = self.browser.find_element(By.XPATH, '//*[@id="search-toggler"]/li/a')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(button).perform()

        # clicamos no botao para aparecer a barra de pesquisa
        button.click()

        # definimos o que desejamos procurar
        string = 'computer science'
        # encontramos pelo ID a nossa barra de pesquisa
        search = self.browser.find_element(By.ID, 'site-search-input')
        actions.scroll_to_element(search).perform()

        # pesquisamos a string desejada e clicamos ENTER
        search.send_keys(string + Keys.RETURN)

        # testa se a string pesquisada eh substring da url atual
        self.assertTrue(string in unquote(self.browser.current_url))

        self.browser.close()

    def test_checkbox(self):

        self.browser.get("https://admission.du.edu/register/requestinformation")

        actions = ActionChains(self.browser)
        student_race = self.browser.find_element(By.XPATH, '//*[@id="form_85be5b2f-b4fd-47d7-85cc-8ae518525ec9_1"]')
        student_race_label = self.browser.find_element(By.XPATH, '//*[@id="form_85be5b2f-b4fd-47d7-85cc-8ae518525ec9"]/div[2]/div[1]/label')
        actions.scroll_to_element(student_race).perform()

        # testa se a checkbox começa sem estar selecionada
        self.assertFalse(student_race.is_selected())

        # selecionamos a checkbox
        student_race_label.click()

        # testa se a checkbox realmente foi selecionada
        self.assertTrue(student_race.is_selected())

        # segunda checkbox 
        student_race2 = self.browser.find_element(By.XPATH, '//*[@id="form_85be5b2f-b4fd-47d7-85cc-8ae518525ec9_2"]')

        # testa se a data-text das checkboxes sao diferentes
        self.assertNotEqual(student_race.get_attribute('data-text'), student_race2.get_attribute('data-text'))
        
        # testa se apenas uma checkbox esta selecionada entre essas duas opcoes
        assert (student_race.is_selected() != student_race2.is_selected())

        self.browser.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)
