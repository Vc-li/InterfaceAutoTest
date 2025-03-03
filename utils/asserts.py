import logging

import allure
import jsonpath

from utils.send_requests import send_sql_request


@allure.step("http 响应断言")
def http_assert(case, res):  # http 响应断言
    if case["check"]:
        json_check = jsonpath.jsonpath(res.json(), case["check"])[0]  # 读取json响应结果
        assert case["expected"] == json_check
        logging.info(f"HTTP响应断言  预期结果({case['expected']}) == 实际结果({json_check})")
    elif case["expected"]:
        logging.info(f"HTTP响应断言  预期结果({case['expected']}) in 实际结果({res.text})")
        assert case["expected"] in res.text


@allure.step("sql 响应断言")
def sql_assert(case):
    if case["sql_check"] and case["sql_expected"]:
        request = send_sql_request(case["sql_check"])
        assert request[0] == case["sql_expected"]
        logging.info(f"SQL断言  sql语句：{case['sql_check']}  预期结果({case['sql_expected']}) == 实际结果({request[0]})")
