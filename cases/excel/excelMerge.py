import json
import os
import glob
import xlwings as xw

os.chdir("E:\\BaiduNetdiskDownload")
# 指定目录路径
directory = 'E:\\BaiduNetdiskDownload\\gdc_download_20230808_062718.413552'

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
col = wb.sheets['Sheet1']
col.offset(0, 1)

def getjson():
    with open('metadata.cart.2023-08-08.json', 'r') as f:
        # 读取文件内容
        data = f.read()

        # 解析JSON数据
        json_data = json.loads(data)
        print(json_data[0]["associated_entities"][0]["entity_submitter_id"])

    for data in json_data:
        # 名称
        entity_submitter_id = data["associated_entities"][0]["entity_submitter_id"]
        # 获取文件目录
        folder = directory + data["file_id"]

        # 检查文件是否存在,不存在下一个
        if not os.path.exists(folder):
            continue

        # 从文件目录下获取excel文件名
        file_name = glob.glob(folder + '/*rna_seq.augmented_star_gen')

        # 操作excel
        # 获取对应列的值
        tmp_excel_sheet = app.books.open(file_name).sheets[0]
        d_column_range_value = tmp_excel_sheet.range('D7:D').value
        col.cells[0] = entity_submitter_id


def __main__():
    getjson()


# __main__()
wb.save('count.xlsx')