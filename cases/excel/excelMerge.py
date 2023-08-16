import json
import os
import glob
import xlwings as xw

# 指定工作目录
os.chdir("C:\\Users\sirius\\百度网盘")
# 指定目录路径
directory = 'C:\\Users\sirius\\百度网盘\\gdc_download_20230808_062718.413552\\'

# 初始化xlwings配置
app = xw.App(visible=True, add_book=False)
app.display_alerts = False
app.screen_updating = False

# 创建或打开excel
try:
    wb = app.books.open('count.xlsx')
    print("成功打开现有的Excel文件")
except FileNotFoundError:
    wb = app.books.add()
    # 这个保存应该最后做
    # wb.save('count.xlsx')
    print("创建并保存了新的Excel文件")
sht = wb.sheets['Sheet1']
rng = sht.range('A1')

try:
    with open('metadata.cart.2023-08-08.json', 'r') as f:
        # 读取文件内容
        data = f.read()
        # 解析JSON数据
        json_data = json.loads(data)
        # print(json_data[0]["associated_entities"][0]["entity_submitter_id"])
    for data in json_data:
        # 名称
        entity_submitter_id = data["associated_entities"][0]["entity_submitter_id"]
        # 获取文件目录
        folder = directory + data["file_id"]
        # 检查文件是否存在,不存在下一个
        if not os.path.exists(folder):
            print(folder + " does not exist")
            continue
        # 从文件目录下获取excel文件名
        file_name = glob.glob(folder + '\*rna_seq.augmented_star_gen')
        print(f"folder is {folder}, file_name is {file_name}")
        # 操作excel
        # 获取对应列的值
        tmp_books = app.books.open(file_name[0])
        tmp_excel_sheet = tmp_books.sheets[0]
        d_column_range_value = tmp_excel_sheet.range('D7:D60666').value
        # 给新建表赋值
        # 移动列
        rng = rng.offset(0, 1)
        rng.value = entity_submitter_id
        # 当前列
        column_index = rng.column
        # 从第二行还是给列赋值
        for index, value in enumerate(d_column_range_value):
            cell = sht.range(2 + index, column_index)
            cell.value = value
        tmp_books.close()

    wb.save(r'count.xlsx')
    wb.close()
except KeyboardInterrupt:
    tmp_books.close()
    wb.save(r'count.xlsx')
    wb.close()
