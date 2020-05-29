# import json
# import requests
# url = "http://www.tuling123.com/openapi/api"
# message =input("请输入你想说的话：")
# data = {"key":"ec961279f453459b9248f0aeb6600bbe","info":message}
# response = requests.get(url,json.dumps(data))
# print(response.text)
# print(response.json()['code'])
# # 解码方式
# print(response.encoding)
# # 用到的cookies
# print(response.cookies())
# print(response.url)
# print(response.status_code)
# # 二进制
# print(response.content)


# # 序列化与反序列化
# import json
# # data ={"name":"test","sex":"man","age":13}
# data = {"name":"董赫","sex":"man","age":13}
# # 转换为文本/文件句柄
# # 此处False需大写，否则报错
# string = json.dumps(data,indent=2,ensure_ascii=False)
# print(string)
# # 转换为json能识别的对象（字典）
# object = json.loads(string)
# print(object)
# print(object['age'])

# 保留同一个会话，（用同一个会话，会保留登录状态）用到requests.session(),否则每发一次请求，会创建一个会话
# import requests
#
#
# s = requests.session() # 新建一个会话
# s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
# res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
# print(res.text)

# # python操作数据库
# import pymysql
#
# # 1. 建立连接
# conn = pymysql.connect(host='127.0.0.1',
#                        port=3306,
#                        user='root',
#                        passwd='123456',  # password也可以
#                        db='api_test',    #数据库名
#                        charset='utf8')  # 如果查询有中文需要指定数据库编码
#
# # 2. 从连接建立游标（有了游标才能操作数据库）
# cur = conn.cursor()
#
# # 3. 查询数据库（读），返回的是影响的行数
# cur.execute("select * from user where name='张三'")
#
# # 4. 获取查询结果，游标获取的数据将会被删除;如果后面要重复使用数据，将其赋值给变量
# result = cur.fetchall()
# print(result)
#
# # 3. 更改数据库（写）
# cur.execute("delete from user where name='李四'")
#
# # 4. 提交更改
# conn.commit()  # 注意是用的conn不是cur
#
# # 5. 关闭游标及连接
# cur.close()
# conn.close()

# python操作excel
import xlrd
filepath = "./data.xlsx"
# file = open(filepath,'r')
data = xlrd.open_workbook(filepath)
# 获取sheet数
print(data.nsheets)
# 获取sheet名
print(data.sheet_names())
table=data.sheet_by_index(0)
print(data.sheet_by_name("adress"))
print(data.sheets()[0])
# data.sheet_loaded(0)
rows = table.nrows
# cols= table.ncols
# print(rows)
# print(cols)
# # 返回某行的元素列表（内容类型:内容）
# # 返回列表中的某值，用相应的索引即可
# print(table.row(0)[1])
# print(table.row(1))
# print(table.row_slice(1))
# # 返回某行，由某列开始到结束单元格组成的列表
# print(table.row_values(3,2,4))
# print(table.row_values(4))
# # 表格某行的单元格个数（不管有多少单元格，返回sheet表格中的最多单元格数量）
# print(table.row_len(1))
# print(table.col(2))
# print(table.col_slice(2))
# print(table.col_values(2))
# #获取某单元格的值
# print(table.cell_value(2,3))
# print(table.cell_value(0,0).value)
# print(table.row_values(1))
# print(table.row_values(0))
head = table.row_values(0)
# print(head)
for i in range(1,rows):
    # print(table.row_values(i))
    #将excel某一行的值与头组合起来，并形成字典组合
    case = dict(zip(head,table.row_values(i)))
    print(case)
    print(case['name'])

