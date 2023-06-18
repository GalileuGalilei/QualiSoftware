#pesquise um site no google e o abra usando selenium
#pesquise um site no google e o abra usando selenium
__package__ = 'selenium'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import validators

#Button
#Search 
#Top Bar
#scroll
#hide things
#imagens
#video
#hyperlink 
#text field

class DenverUniversityTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(2)

        self.browser.get("https://www.du.edu")
        cookie = self.browser.find_element(By.XPATH, '//*[@id="c-right"]/a').click()

        self.addCleanup(self.browser.quit)

    def test_button1(self):
        # obtem o botao e scrolla a tela ate ele
        button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/form/div[2]/div[2]/div[1]/button')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(button).perform()
        
        # verifica se o botao esta sendo mostrado, e se o titulo dele condiz com o site
        self.assertTrue(button.is_displayed())
        self.assertEqual(button.get_attribute('title'), "Search Undergraduate Programs")
        
        # guarda o url de destino e clica no botao
        data_action = button.get_attribute('data-action')
        button.click()
        time.sleep(2)

        # verifica se o botao levou ate a url certa
        self.assertIn(data_action, self.browser.current_url)
        time.sleep(2)

    def test_button2(self):
        # obtem o botao com imagem e scrolla a tela ate ele
        image_button = self.browser.find_element(By.XPATH, '//*[@id="off-canvas-content"]/footer/div[1]/div/div/div/div[3]/a')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(image_button).perform()

        # verifica se o botao esta sendo mostrado, e se o titulo dele condiz com o site
        self.assertTrue(image_button.is_displayed())
        self.assertEqual(image_button.get_attribute('title'), "Find your program representative and schedule a visit")
        
        # obtem a imagem do botao e verifica se ela esta sendo mostrada
        image = image_button.find_element(By.XPATH, '//*[@id="off-canvas-content"]/footer/div[1]/div/div/div/div[3]/a/img')
        self.assertTrue(image.is_displayed())
        time.sleep(2)

        # obtem a url da imagem e abre ela
        image_link = image.get_attribute('src')
        self.browser.get(image_link)
        time.sleep(2)

    def test_topbar(self):
        # obtem a top bar
        top_bar = self.browser.find_element(By.XPATH, '//*[@id="top-bar-sticky-wrap"]/div[2]')
        self.assertTrue(top_bar.is_displayed())

        # obtem a lista com os elements da top bar
        ul = top_bar.find_element(By.TAG_NAME, 'ul').find_elements(By.XPATH, '*')

        urls = []
        texts = []

        # para cada elemento da lista de elementos da top bar, salva a href e o texto do elemento
        for li in ul:
            self.assertTrue(li.is_displayed())

            a = li.find_element(By.TAG_NAME, 'a')
            url = a.get_attribute('href')
            text = a.text

            urls.append(url)
            texts.append(text)

        # para cada url salva, acessa a mesma e verifica se o titulo da pagina corresponde ao texto do elemento
        for i in range (len(urls)):
            self.browser.get(urls[i])
            time.sleep(1)

            self.assertIn(texts[i], self.browser.title)
            time.sleep(2)

    def test_submenu(self):
        random.seed()
        # avanca a pagina e obtem o submenu e sua lista de elementos (opcoes)
        self.browser.find_element(By.XPATH, '//*[@id="block-pl-drupal-main-menu"]/ul/li[3]/a').click()
        submenu = self.browser.find_element(By.XPATH, '//*[@id="sub-menu"]')
        ul = submenu.find_element(By.TAG_NAME, 'ul').find_elements(By.XPATH, '*')

        # verifica se o submenu esta sendo mostrado
        self.assertTrue((submenu.is_displayed()))

        # verifica se a ordem do submenu esta de acordo
        submenu_order = ['Overview', 'Centers & Institutes', 'Health & Wellness', 'Society & Culture', 'Technology & Science', 'In the News', 'About DU Research', 'Research Showcase']
        for i in range (len(ul)):
            text = ul[i].find_element(By.TAG_NAME, 'a').text
            self.assertEqual(text, submenu_order[i])

        # escolhe uma das opcoes aleatoriamente para cliclar
        idx = random.randint(0, len(ul)-1)
        ul[idx].find_element(By.TAG_NAME, 'a').click()
        time.sleep(2)

        # apos o clique, obtem novamente a lista de elementos, e verifica se o elemento clicado esta como ativo
        ul = self.browser.find_element(By.XPATH, '//*[@id="sub-menu"]').find_element(By.TAG_NAME, 'ul').find_elements(By.XPATH, '*')
        self.assertTrue(ul[idx].get_attribute('class') == "active")

        # verifica se a url atual condiz com a url da opcao selecionada
        self.assertIn(ul[idx].find_element(By.TAG_NAME, 'a').get_attribute('href'), self.browser.current_url)
        time.sleep(2)

    def test_video_play(self):
        iframe = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div/div/div/div/div/iframe')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(iframe).perform()
        time.sleep(1)
        #play no vídeo
        iframe.click()
        #espera o vídeo chegar a 6 segundos
        time.sleep(6)
        #verifica se o vídeo está rodando
        self.assertTrue(iframe.is_displayed())
        #pausa o vídeo
        iframe.click()
        time.sleep(1)

    def test_video_title(self):
        iframe = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div/div/div/div/div/iframe')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(iframe).perform()
        time.sleep(1)
        self.browser.switch_to.frame(iframe)
        #pega o título do vídeo
        title = self.browser.find_element(By.CLASS_NAME, 'ytp-title-link').text
        self.assertIn('University of Denver', title)
        
    def test_hyperlink_using_url_validator(self):
        link = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/p[2]/a[1]')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(link).perform()
        time.sleep(1)
        #valida se o link é valido
        self.assertTrue(validators.url(str(link.get_attribute('href'))))
        time.sleep(1)
        #clica no link
        link.click()

    def test_hyperlink_using_window_title(self):
        link = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/p[2]/a[1]')
        actions = ActionChains(self.browser)
        actions.scroll_to_element(link).perform()
        time.sleep(1)
        #pega o link
        link_url = link.get_attribute('href')
        #clica no link
        link.click()
        time.sleep(2)
        #troca para a nova aba aberta
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(1)
        #verifica se o link levou ao lugar certo
        self.assertIn('Kennedy Mountain Campus', self.browser.title)

    
        
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

if __name__ == '_main_':
    unittest.main(verbosity=2)
