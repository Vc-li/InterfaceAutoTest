import logging

import allure

from config.config import URL

'''
解析case中参数  规格化为request请求参数
'''


@allure.step("1.解析请求参数")
def analyse_case(case):
    method = case["method"]
    url = URL + case["path"]
    headers = eval(case["headers"]) if isinstance(case["headers"], str) else None
    params = eval(case["params"]) if isinstance(case["params"], str) else None
    data = eval(case["data"]) if isinstance(case["data"], str) else None
    json = eval(case["json"]) if isinstance(case["json"], str) else None
    files = eval(case["files"]) if isinstance(case["files"], str) else None
    request_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
    }
    logging.info(f"解析请求数据，解析结果：{request_data}")
    return request_data
