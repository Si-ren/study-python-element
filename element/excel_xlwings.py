import xlwings as xw

# xlwings默认配置 程序可见，只打开不新建工作薄，屏幕更新关闭
app = xw.App(visible=True, add_book=False)
app.display_alerts = False
app.screen_updating = False


# 创建或打开excel
try:
    wb = app.books.open('count.xlsx')
    print("成功打开现有的Excel文件")
except FileNotFoundError:
    wb = app.books.add()
    print("创建新的Excel文件")

sht = wb.sheets['Sheet1']
rng = sht.range('A1')
rng.value = 'A1单元格'
rng = rng.offset(0, 1)
rng.value = '应当为B1'
values = [0, 1, 2, 3, 4, 5]
column_index = rng.column
print(column_index)
for index, value in enumerate(values):
    cell = sht.range(2 + index, column_index)
    cell.value = value
rng = rng.offset(0, 1)
rng.value = '应当为C1'

d_column_range_value = sht.range('B3:B7').value
print(f"Values in column G from row 8 to the end: {d_column_range_value}")

# 保存文件
wb.save(r'count.xlsx')
wb.close()
