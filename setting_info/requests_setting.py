import requests;

import json;

'''

方法: 将requests对象测试接口时具体调用哪个方法进行逻辑判断，接口测试方式(get/post/delete/put)

参数: 接口的路径，接口的请求方式，接口的请求头信息，请求的参数

返回值: 接口的响应体
'''

def requests_strong(inter_url,inter_method,inter_parm):

    if inter_method == "get" or inter_method == "delete":

        resp = requests.get(url=inter_url,params=inter_parm,verify=False);

    elif inter_method == "post" or inter_method == "put":

        resp = requests.post(url=inter_url,data=json.loads(inter_parm),verify=False);

    else:

        print("没有此类的接口请求方式!");

    return resp;
