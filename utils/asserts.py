import allure
import jsonpath

from utils.send_requests import send_sql_request


@allure.step("http 响应断言")
def http_assert(case, res):  # http 响应断言,
    if case["check"]:
        assert case["expected"] == jsonpath.jsonpath(res.json(), case["check"])[0]
    elif case["expected"]:
        assert case["expected"] in res.text


@allure.step("sql 响应断言")
def json_assert(case):
    if case["sql_check"] and case["sql_expected"]:
        request = send_sql_request(case["sql_check"])
        assert request[0] == case["sql_expected"]
