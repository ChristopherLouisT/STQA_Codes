"""
Web Steps
Steps file for web interactions with Selenium
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from behave import given, when, then

@given('the following pets')
def step_impl(context):
    """Refresh pets in database"""
    # This ensures a clean database before loading the data table
    requests.post(f"{context.base_url}/pets/reset")
    
    for row in context.table:
        result = {
            "name": row['name'],
            "category": row['category'],
            "available": row['available'] in ['True', 'true', '1'],
            "gender": row['gender'],
            "birthday": row['birthday']
        }
        response = requests.post(f"{context.base_url}/pets", json=result)
        assert(response.status_code == 201)

    
ID_PREFIX = 'pet_'

@given('I am on the "Home Page"')
def step_impl(context):
    context.driver.get(context.base_url)

# Cara 1 pake variable
# @when('I set the "{element_name}" to "{text_string}"')
# def step_impl(context, element_name, text_string):
#     element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
#     element = context.driver.find_element(By.ID, element_id)
#     element.clear()
#     element.send_keys(text_string)

# Cara 2 tanpa variable
@when('I set the "Category" to "dog"')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'pet_category')
    element.clear()
    element.send_keys("dog")

# Cara 1 pake variable
# @when('I click the "{button}" button')
# def step_impl(context, button):
#     button_id = button.lower() + '-btn'
#     context.driver.find_element(By.ID, button_id).click()

# Cara 2 tanpa variable
@when('I click the "Search" button')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'search-btn')
    element.click()

# Cara 1 pake variable
# @then('I should see the message "{message}"')
# def step_impl(context, message):
#     found = WebDriverWait(context.driver, context.wait_seconds).until(
#         expected_conditions.text_to_be_present_in_element(
#             (By.ID, 'flash_message'),
#             message
#         )
#     )
#     assert(found)

# Cara 2 tanpa variable
@then('I should see the message "Success"')
def step_impl(context):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'flash_message'),
            "Success"
        )
    )
    assert(found)


# Cara 1 pake variable
# @then('I should see "{name}" in the results')
# def step_impl(context, name):
#     found = WebDriverWait(context.driver, context.wait_seconds).until(
#         expected_conditions.text_to_be_present_in_element(
#             (By.ID, 'search_results'),
#             name
#         )
#     )
#     assert(found)

# Cara 2 tanpa variable
@then('I should see "Fido" in the results')
def step_impl(context):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'search_results'),
            "Fido"
        )
    )
    assert(found)

# Cara 1 pake variable
# @then('I should not see "{name}" in the results')
# def step_impl(context, name):
#     element = context.driver.find_element(By.ID, 'search_results')
#     error_msg = "I should not see '%s' in '%s'" % (name, element.text)
#     assert(name not in element.text)

# Cara 2 tanpa variable
@then('I should not see "Kitty" in the results')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'search_results')
    assert("Kitty" not in element.text)

@then('I should not see "Leo" in the results')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'search_results')
    assert("Leo" not in element.text)