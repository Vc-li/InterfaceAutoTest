import openpyxl

'''
读取测试用例Excel文件  解析返回测试用例列表[{key:value},{key:value}]
file_path=测试用例excel文件路径 
sheet=测试用例所在的表名，默认读取Sheet1
'''


def analysis_casedata(file_path, sheet="Sheet1"):
    # 打开Excel文件
    work_book = openpyxl.load_workbook(file_path)
    # 选择sheet1表
    work_sheet = work_book[sheet]

    case_data = []  # 空列表存储测试用例
    case_keys = [cell.value for cell in work_sheet[2]]  # 将Excel第二列设置为key

    # 变量sheet1的数据
    for row in work_sheet.iter_rows(min_row=3, values_only=True):
        cell = dict(zip(case_keys, row))
        if cell["is_true"]:
            case_data.append(cell)  # 使用zip函数将key和测试数据打包为键值对形式存入字典
    # print(case_data)
    work_book.close()
    return case_data


# print(analysis_casedata("../data/测试用例.xlsx"))
