from setting_info import cese_excel,requests_setting
import difflib;



def test_login():
    #定义接口响应状态码列表
    resp_code_list = [];

    resp_text_list = [];

    result_list = [];


    #首先将配置层中的用例信息读取到用例层中
    inter_list = cese_excel.read_case(r"C:\Users\Administrator\Desktop\hospital_case.xls","login");

    #调用requests对象进行接口测试
    for i in inter_list:
        #i = {'jk_name': '用户名非空验证', 'jk_url': 'http://192.168.1.22:8080/login', 'jk_fs': 'post', 'jk_cs': '{"uname":"","upwd":"123456"}'}
        #接口的路径

        inter_url = i.get("jk_url");

        inter_method = i.get("jk_fs");

        inter_parm = i.get("jk_cs");

        inter_think = i.get("jk_think");

        resp = requests_setting.requests_strong(inter_url,inter_method,inter_parm);

        resp_code_list.append(resp.status_code);

        resp_text_list.append(resp.text)

        #通过判断响应的状态码和预期结果以及实际测试结果的相似度对其得出测试结果

        if resp.status_code == 200 and difflib.SequenceMatcher(None,resp.text,inter_think).ratio() > 0.8:

            result_list.append("√")

        else:

            result_list.append("×")


    #接口测试完毕后，将测试结果写入用例中
    cese_excel.write_case_result(resp_code_list,resp_text_list,result_list,r"C:\Users\Administrator\Desktop\hospital_case.xls","login");

def test_goods():
    # 定义接口响应状态码列表
    resp_code_list = [];

    resp_text_list = [];

    result_list = [];

    # 首先将配置层中的用例信息读取到用例层中
    inter_list = cese_excel.read_case(r"C:\Users\Administrator\Desktop\hospital_case.xls", "goods");

    # 调用requests对象进行接口测试
    for i in inter_list:
        # i = {'jk_name': '用户名非空验证', 'jk_url': 'http://192.168.1.22:8080/login', 'jk_fs': 'post', 'jk_cs': '{"uname":"","upwd":"123456"}'}
        # 接口的路径

        inter_url = i.get("jk_url");

        inter_method = i.get("jk_fs");

        inter_parm = i.get("jk_cs");

        inter_think = i.get("jk_think");

        resp = requests_setting.requests_strong(inter_url, inter_method, inter_parm);

        resp_code_list.append(resp.status_code);

        resp_text_list.append(resp.text)

        # 通过判断响应的状态码和预期结果以及实际测试结果的相似度对其得出测试结果

        if resp.status_code == 200 and difflib.SequenceMatcher(None, resp.text, inter_think).ratio() > 0.8:

            result_list.append("√")

        else:

            result_list.append("×")

    # 接口测试完毕后，将测试结果写入用例中
    cese_excel.write_case_result(resp_code_list, resp_text_list, result_list,
                                 r"C:\Users\Administrator\Desktop\hospital_case.xls", "goods");