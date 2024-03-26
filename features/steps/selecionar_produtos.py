# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()     # instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()        # maximizar a janela do navegador
    context.driver.implicitly_wait(10)      # esperar até 10 segundos por qualquer elemento
    # Passo em si
    context.driver.get("https://www.saucedemo.com") # abrir o navegador no endereço do site alvo


@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login
   
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
        # não preencher o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

# Preencher com usuario, mas deixar com a senha em branco    
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
        # não preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

# Clica no botão de login, sem ter preenchido usuario e a senha    
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
        # não preencher o usuário
        # não preencher a senha
    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

# preencher com usuario e senha atraves da desição (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':    
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
        # se o ususario estiver em branco não há ação de preenchimento

    if usuario != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha

    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2) # espera por 2 segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()
  

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()