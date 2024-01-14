from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'Que o navegador esteja aberto')
def step_impl(context):
    if not context.browser:
        raise Exception(
            "O navegador não está aberto. Certifique-se de que a configuração inicial foi feita corretamente.")


@when(u'Acessar a página home da plataforma')
def step_impl(context):
    context.browser.get('https://www.google.com/')


@then(u'Todos os recursos da página serão carregados')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    context.browser.find_element(By.NAME, 'q')
