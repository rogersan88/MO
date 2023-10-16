from behave import *
from utilities.requests_api import RequestsApi
api_util = RequestsApi()


@step("User verifies POST response body contains following information")
def step_impl(context):
    api_util.Verify_POST(context.table)
    response_body = response.json()
    assert response_body['name'] == context.table[0][0]
    assert response_body['job'] == context.table[0][1]
    assert int(response_body['id']) > 0


@when('User sends "{method}" call to endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_util.Method_Call(context.table, method, endpoint)


@then('User verifies the status code is "{status_code}"')
def step_impl(context, status_code):
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)