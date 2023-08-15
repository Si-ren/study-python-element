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

# 保存文件
wb.save(r'count.xlsx')
wb.close()
