from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'Que esteja na página home')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    img_google = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//img[@alt="Google"]')))


@when(u'Confirmar a informação no campo de pesquisa')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)


@then(u'As informações relacionadas serão exibidas')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    first_link = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
    first_link.click()
    wait.until(EC.title_contains('Selenium'))
