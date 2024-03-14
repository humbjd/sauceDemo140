# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# 2 - Classe (Opcional)
class Test_Products():
# 2.1 - Atributos
    url = "https://www.saucedemo.com"                     # endereço do site alvo
# 2.2 - Funções e Métodos

    def setup_method(self, method):                       # método de inicialização dos testes 
        self.driver = webdriver.Chrome()                  # instanciar o projeto do Selenium Webdriver como Chrome
        self.driver.implicitly_wait(10)                   # irá esperar qualquer elemento por até 10 segundos (recomendado)

    def teardown_method(self, method):                    # método de finalização dos teste
        self.driver.quit()                                # encerra / destrói o objeto do Selenium Webdriver da memória

    def test_select_products(self):                         # método de teste
        self.driver.get(self.url)                           # abre o navegador
        self.driver.find_element(By.ID,'user-name').send_keys('standard_user')              # escreve no campo user-name
        self.driver.find_element(By.NAME,'password').send_keys('secret_sauce')              # escreve no campo password
        self.driver.find_element(By.CSS_SELECTOR,'input.submit-button.btn_action').click()  # clique no botão login

        # transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.title').text == 'Products'   # checa o elemento está escrito Products
        assert self.driver.find_element(By.ID, 'item_4_title_link').text == 'Sauce Labs Backpack' # confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, '.inventory_item:nth-child(1) .inventory_item_price').text == '$29.99' # confere preço