import logging

import allure
import jsonpath

from utils.send_requests import send_sql_request


@allure.step("json提取器")
def json_extractor(case, res, all):
    if case["jsonExData"]:
        for key, value in eval(case["jsonExData"]).items():
            var = jsonpath.jsonpath(res.json(), value)[0]
            all[key] = var
            logging.info(f"根据 {case['jsonExData']} 提取 {res.json()}中的数据  此时全局变量为{all}")


@allure.step("sql提取器")
def sql_extractor(case, all):
    if case["sqlExData"]:
        for key, value in eval(case["sqlExData"]).items():
            var = send_sql_request(value)[0]
            all[key] = var
            logging.info(f"根据 {case['sqlExData']} 提取数据库中的数据  此时全局变量为{all}")
