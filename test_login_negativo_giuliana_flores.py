# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classes
class Test_Login_Negativo():
    # 2.1 Atributos
    url = 'https://www.giulianaflores.com.br/'
    # 2.2 - Funções e metodos

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def teardown_method(self,method):
        self.driver.quit()
      
    def test_criacao_usuario(self):

        email_fake = 'yuma2876@uorak.com'
        senha_invalida = '123'

        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'perfil-hidden').click()
        assert self.driver.find_element(By.ID, 'UrlLogin').text == 'LOGIN / CADASTRAR'
        self.driver.find_element(By.ID, 'UrlLogin').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#title-defaut').text == 'IDENTIFICAÇÃO'
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtEmail').send_keys(email_fake)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtPassword').send_keys(senha_invalida)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_ibtContinue').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_divMessages').text == 'ATENÇÃO - e-mail ou senha inválidos!'