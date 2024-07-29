import xlrd;
import xlutils.copy as copy;
import xlwt;

'''

方法: 该方法的作用是将传入方法中的excel表格中的接口信息读取出来，然后封装成接口列表并返回

参数信息: excel表格的路径       sheetname

返回值: 接口信息列表

'''

{"inter_name":"登录","inter_url":"","inter_method":"post","inter_parm":{}}

def read_case(case_url,sheet_name):

    #定义一个接口列表用于存放接口信息
    inter_list = [];
    #通过调用xlrd对象的openworkbook方法读取指定的用例文件中的用例信息；
    case_file = xlrd.open_workbook(case_url);

    #通过读取到的文件中的sheet
    case_info = case_file.sheet_by_name(sheet_name)

    #获取sheet中的用例条数
    case_num = case_info.nrows

    #通过循环获取每一行的数据信息
    for i in range(1,case_num):

        inter_info = {};
        #[text:'login_user_001', text:'用户名非空验证', text:'登录', text:'http://192.168.1.22:8080/login', text:'post', text:'{"uname":"","upwd":"123456"}', text:'用户不能为空', empty:'', empty:'']
        #case_info.row(i)[1].value获取接口的名称    case_info.row(i)[3].value接口的路径
        #case_info.row(i)[4].value接口的请求方式    case_info.row(i)[5].value接口的参数

        inter_info["jk_name"] = case_info.row(i)[1].value;
        inter_info["jk_url"] = case_info.row(i)[3].value;
        inter_info["jk_fs"] = case_info.row(i)[4].value;
        inter_info["jk_cs"] = case_info.row(i)[5].value;
        inter_info["jk_think"] = case_info.row(i)[6].value;

        #将拼接好的接口信息存入接口列表中
        inter_list.append(inter_info);

    #for执行完毕后，将存放接口信息的列表返回
    return inter_list;

'''
方法: 将传入该方法的信息写入excel表格中

参数: 写入的信息（响应状态码，响应报文，测试结果），写入的文件路径，写入的sheet名称   

返回值: 无返回值
'''

def write_case_result(resp_code_list,resp_text_list,result_list,file_url,sheet_name):

    #通过xlrd读取操作的文件
    case_file = xlrd.open_workbook(file_url);

    #通过xlutils对象的copy方法将用例文件拷贝一份，后期操作的是拷贝的文件
    new_case_file = copy.copy(case_file);

    #通过读取的用例文件读取相应的sheet
    case_sheet = new_case_file.get_sheet(sheet_name);

    #通过遍历传入的响应状态码或者报文信息或者结果都可以，因为三个元素的个数是相同的
    for i in range(len(resp_code_list)):

        case_sheet.write(i+1,7,resp_code_list[i]);
        case_sheet.write(i+1,8,resp_text_list[i]);
        case_sheet.write(i+1,9,result_list[i]);
    #当所有的测试结果写入完成后，通过调用缓存中的文件对象的save方法进行保存，保存至用例文件
    new_case_file.save(file_url);





