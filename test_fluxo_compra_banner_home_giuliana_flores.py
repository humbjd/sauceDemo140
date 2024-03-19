# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classes
class Test_Fluxo_Compra():
    # 2.1 Atributos
    url = 'https://www.giulianaflores.com.br/'
    # 2.2 - Funções e metodos

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def teardown_method(self,method):
        self.driver.quit()

    def test_fluxo_compra(self):

        nome_boas_vindas = 'Quentin'
        email_fake = 'yuma2876@uorak.com'
        senha_valida = 'Teste@123'
        CEP = '05206150'

        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'perfil-hidden').click()
        assert self.driver.find_element(By.ID, 'UrlLogin').text == 'LOGIN / CADASTRAR'
        self.driver.find_element(By.ID, 'UrlLogin').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#title-defaut').text == 'IDENTIFICAÇÃO'
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtEmail').send_keys(email_fake)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtPassword').send_keys(senha_valida)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_ibtContinue').click()
        self.driver.find_element(By.CSS_SELECTOR, '#perfil-hidden').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#lblWelcome').text == (f'Boa Noite, {nome_boas_vindas}!')


        #self.driver.get(self.url)
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == 'Box de Páscoa com Kopenhagen'
        self.driver.find_element(By.TAG_NAME, 'h3').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_lblProductDsName').text == 'BOX DE PÁSCOA COM KOPENHAGEN'
        assert self.driver.find_element(By.CSS_SELECTOR, '#lblIdProduct').text == 'Cód. Produto: 32212'
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_txtZip').send_keys(CEP)
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_lbtBuy').click()
        self.driver.find_element(By.XPATH, '//body[1]/form[1]/div[3]/div[4]/div[7]/div[1]/div[2]/div[10]/div[3]/div[6]/div[1]/ul[1]/li[2]/input[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, '#btConfirmShippingData').click()
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_lbtBuy').click()
        #assert self.driver.find_element(By.CSS_SELECTOR, '#imgBasket').text == 'Carrinho'
        self.driver.find_element(By.CSS_SELECTOR, '#ContentSite_Basketcontrol1_rptBasket_imbFinalize_0').click()



        


