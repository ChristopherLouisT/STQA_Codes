from behave import given, when, then
import requests

@given('the counter is reset')
def step_impl(context):
    """Resets the hit counter via an API call."""
    response = requests.post(f"{context.base_url}/reset")
    assert response.status_code == 200

@when('a user clicks the "Hit" Button')
def step_impl(context):
    """Simulates a button click with an API call."""
    response = requests.post(f"{context.base_url}/hit")
    assert response.status_code == 200

@then('the counter should be at {count}')
def step_impl(context, count):
    """Verifies that the counter has the expected value."""
    response = requests.get(f"{context.base_url}/")
    assert f'<span id=\"counter\">' + count + '</span>' in response.text