import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from behave import use_fixture
from selenium.webdriver.common.keys import Keys


def create_screenshot_folder():
    folder_name = "screenshots"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    context.browser = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), options=options)
    # context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    context.screenshot_folder = create_screenshot_folder()


def after_all(context):
    context.browser.quit()


def after_step(context, step):
    screenshot_name = f"step_{step.name.replace(' ', '_')}.png"
    screenshot_path = f"{context.screenshot_folder}/{screenshot_name}"
    context.browser.save_screenshot(screenshot_path)
    print(f"Screenshot salvo como {screenshot_path}")

# def before_step(context, step):
#     screenshot_name = f"step_{step.name.replace(' ', '_')}.png"
#     screenshot_path = f"{context.screenshot_folder}/{screenshot_name}"
#     if os.path.exists(screenshot_path):
#         step.embed(screenshot_path, "image/png")

# def before_feature(context, feature):
#     use_fixture(before_all, context)

# def before_scenario(context, scenario):
    # Antes de cada cenário, você pode adicionar configurações específicas, se necessário
#     pass
