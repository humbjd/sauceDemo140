# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classes
class Test_Login_Criacao():
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

        nome_fake = 'Quentin Tarantino'
        nome_boas_vindas = 'Quentin'
        cpf_fake = '932.966.723-62'
        email_fake = 'yuma2876@uorak.com'
        senha_valida = 'Teste@123'
        CEP_valido = '05206-150'

        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'perfil-hidden').click()
        assert self.driver.find_element(By.ID, 'UrlLogin').text == 'LOGIN / CADASTRAR'
        self.driver.find_element(By.ID, 'UrlLogin').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#title-defaut').text == 'IDENTIFICAÇÃO'
        self.driver.find_element(By.CSS_SELECTOR,'#ContentSite_ibtNewCustomer').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#title-defaut').text == 'MINHA CONTA'
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtName').send_keys(nome_fake)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtCpf').send_keys(cpf_fake)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtEmail').send_keys(email_fake)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtPasswordNew').send_keys(senha_valida)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_CustomerAddress_txtZip').send_keys(CEP_valido)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_CustomerAddress_txtAddressNumber').send_keys('123')
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_CustomerAddress_txtPhoneCelularNum').send_keys('11999996857')
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_btnCreateCustomer').click()
        self.driver.find_element(By.CSS_SELECTOR, '#perfil-hidden').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#lblWelcome').text == (f'Boa Tarde, {nome_boas_vindas}!')


    





