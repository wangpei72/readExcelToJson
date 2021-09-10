import os
import xlrd
import json

# 当前系统路径
curDir = os.path.dirname(os.path.realpath(__file__))

# 把你的文件存到此文件同级目录，并且把'data1.xlsx'替换程你的文件名称
fileName = 'data1.xlsx'
excelPath = os.path.join(curDir, fileName)

#如果只需要读取 第一行 的数据，请把button改成True
button = False

# 新建一个空字典
jsonData = {}
dataList = []
jsonKeyList = []
num_cols = 0
num_rows = 0

# 打开一个workbook
workBook = xlrd.open_workbook(excelPath)
# 从workbook获取所有的sheets名称
workSheets = workBook.sheet_names()
print("workbook中所有表格名称：", workSheets)

# 这一层循环range里的数字表示遍历的工作簿个数 只看sheet1所以是1
# 获得json豹纹中的key
for i in range(1):
    print('正在读取第%d' % (i+1), '个sheet')
    table = workBook.sheets()[i]
    num_rows = table.nrows
    num_cols = table.ncols
    for j in range(num_cols):
        jsonKeyList.append(table.cell_value(0, j))


for i in range(num_rows):
    if(button and i == 2):
        break
    if (i == 0):
        continue
    new_item_for_dataList = {}
    table = workBook.sheets()[0]
    for j in range(num_cols):

        jsonKey = jsonKeyList[j]# 得到key
        jsonValue = table.cell_value(i, j)# 得到key对应的数据 value
        # print(jsonValue)
        new_item_for_dataList[jsonKey] = jsonValue
    dataList.append(new_item_for_dataList)
    print("new_item_to_append:", new_item_for_dataList)

print("json报文data字段的value（列表形式）---------->>", dataList)
jsonData['data'] = dataList
print("json报文对象------->> ", jsonData)

jsonString = json.dumps(jsonData, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
print("jsonString报文的字符串-------->>", jsonString)
# 将jsondata字典(python数据对象） 格式化输出json字符串

# 写文件
fw = open(os.path.join(curDir, 'data_from'+fileName+'.json'), 'w')
fw.write(jsonString)
fw.close()
