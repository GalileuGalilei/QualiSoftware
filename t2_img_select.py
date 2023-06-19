from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    #abre imagens em uma nova aba
    def _openImageInNewTab(self):
        actions = ActionChains(self.browser)
        original_window = self.browser.current_window_handle

        #pega a primeira imagem a ser aberta
        img = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[6]/div/div/div/div[1]/div/picture/img')

        #scroll até a imagem e verifica se ela esta visivel
        actions.scroll_to_element(img).perform()
        time.sleep(2)
        self.assertTrue(img.is_displayed())

        #pega a url e o titulo da imagem 
        img_url = img.get_attribute("src")
        img_title = img.get_attribute("title")

        #cria uma nova aba e verifica se o numero de abas agora é 2 
        self.browser.switch_to.new_window('tab')
        assert len(self.browser.window_handles) == 2

        # abre a imagem da nova aba
        self.browser.get(img_url)
        time.sleep(2)
        img2 = self.browser.find_element(By.XPATH, '/html/body/img')

        #entao compara os titulos e url da imagem e fecha a nova aba
        assert img2.get_attribute("title") == img_title
        assert img2.get_attribute("src") == img_url
        self.browser.close()

        #volta a aba original e verifica se o número de abas é 1
        self.browser.switch_to.window(original_window)
        assert len(self.browser.window_handles) == 1

        #outra imagem 
        img3 = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[8]/div/div/div/div[1]/picture/img')

        #scroll até a nova imagem e verifica se ela esta visivel
        actions.scroll_to_element(img3).perform()
        time.sleep(2)
        self.assertTrue(img3.is_displayed())

        #pega a url e titulo da nova imagem 
        img3_url = img3.get_attribute("src")
        img3_title = img3.get_attribute("title")

        #cria uma nova aba novamente, verifica se o numero de abas é 2
        self.browser.switch_to.new_window('tab')
        assert len(self.browser.window_handles) == 2

        # abre a imagem da nova aba
        self.browser.get(img3_url)
        time.sleep(2)
        img4 = self.browser.find_element(By.XPATH, '/html/body/img')

        #entao compara os titulos e url da imagem e fecha a nova aba
        assert img4.get_attribute("title") == img3_title
        assert img4.get_attribute("src") == img3_url
        self.browser.close()

    #faz seleções em comboboxes 
    def test_select(self):
        actions = ActionChains(self.browser)
        #faz o caminho até o 'select'
        visit_bt = self.browser.find_element(By.XPATH, '//*[@id="block-utilitymenu"]/ul/li[4]/a')
        visit_bt.click()
        time.sleep(2)
        sched_bt = self.browser.find_element(By.XPATH, '//*[@id="modal_footer_cta_visit"]/div/div/div[2]/div[1]/p[2]/a')
        sched_bt.click()
        time.sleep(2)
        reg_bt = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/div/div[5]/div/div/div[2]/ul/li/a')
        actions.scroll_to_element(reg_bt).perform()
        time.sleep(2)
        reg_bt.click()
        #aqui está no destino

        #pega a primeira combobox (select)
        select1 = self.browser.find_element(By.XPATH, '//*[@id="form_42e06feb-85d7-4c7e-8ac4-cd6422754814"]')
        select = Select(select1)
        #seleciona a opçao, espera um pouco e testa
        select.select_by_visible_text('2024 Fall')
        time.sleep(2)
        s = select.first_selected_option
        assert s.text == '2024 Fall'

        #seleciona outra opçao, espera e testa
        select.select_by_visible_text('2026 Fall')
        time.sleep(2)
        s = select.first_selected_option
        assert s.text == '2026 Fall'

        #pega outra combobox, seleciona brazil e testa
        select2 = self.browser.find_element(By.XPATH, '//*[@id="form_c027c3d2-e002-4875-bb05-6fcd4a56eb49_country"]')
        select = Select(select2)
        select.select_by_visible_text('Brazil')
        time.sleep(2)
        s = select.first_selected_option
        assert s.text == 'Brazil'

        #pega mais uma combobox, desta vez dependente da anterior, seleciona Rio Grande do Sul, e testa
        select3 = self.browser.find_element(By.XPATH, '//*[@id="form_c027c3d2-e002-4875-bb05-6fcd4a56eb49_region"]')
        select = Select(select3)
        select.select_by_visible_text('Rio Grande do Sul')
        time.sleep(2)
        s = select.first_selected_option
        assert s.text == 'Rio Grande do Sul'

        #fecha o browser ao final
        self.browser.close()






        
        


if __name__ == '__main__':
    unittest.main(verbosity=2)