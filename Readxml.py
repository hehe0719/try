import xlrd
# 读取excel的第二列的值（不要第一行）
def readxml_second(filepath,index):
    liebiao= []
    table = xlrd.open_workbook(filepath)
    return table.sheet_names()
    # 通过sheet名定位table
    # info = table.sheet_by_name(index)
    # 通过sheet索引定位table
    info =table.sheet_by_index(index)
    rows = info.nrows
    cols = info.ncols
    for i in range(0,rows):
        # print(info.cell_value(i,1),end=' ')
        # 将某列的值存储到列表里
        liebiao.append(info.cell_value(i,1))
    return liebiao

# 读取某一列的值
def readxml_col(filepath,name,number):
    data = xlrd.open_workbook(filepath)
    table = data.sheet_by_name(name)
    rows = table.nrows
    # 不要表头写1，要表头写0
    for i in range(1,rows):
        # print(table.cell_value(i,number))
        return table.cell_value(i,number)
#读取某一行的值
def readxml_row(filepath,name,number):
    data = xlrd.open_workbook(filepath)
    table = data.sheet_by_name(name)
    cols = table.ncols
    # 不要表头写1，要表头写0
    for i in range(0,cols):
        # print(table.cell_value(number,i),end= ' ')
        return table.cell_value(number, i)

#将表头与行组合起来，形成字典
def readxml_case(filepath,name):
    case = []
    data = xlrd.open_workbook(filepath)
    table = data.sheet_by_name(name)
    rows = table.nrows
    head = table.row_values(0)
    for i in range(1, rows):
        #将excel某一行的值与头组合起来，并形成字典组合
        da = dict(zip(head,table.row_values(i)))
        case.append(da)
    # 返回用例数据列表
    return case
    # print(case)

# 多个接口的用例数据维护在一张表格，针对某个接口取测试用例
def readxls_testcase(list,case_name):
    for ca in list:
        if case_name ==ca["test_name"]:
          # print(ca)
          return ca






if __name__ == '__main__':
    # A = readxml_col("./data.xlsx","adress",0)
    # print("-----------")
    # B =readxml_row("./data.xlsx","adress",1)
    # c =readxml_case("./data.xlsx","用户信息")
    d= readxml_case("./data.xlsx","用户信息")
    e=readxls_testcase(d,1)



# 具体到模块中用的时候，再遍例取列表的值
# nlist = len(list)
# for i in range(nlist):
#         # 具体列表中的某个值
#         list[i]



