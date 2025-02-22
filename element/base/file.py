import os

# w: 写  r: 读  a: 追加
# f = open("test.txt", mode='r')
# # f.write("Hello World")
# # read()单位字节，不传参读取全部数据
# print(f.read(3))
# # readline()读取当前行，如果加了参数，那么就是返回指定字符。readline(2)
# print(f.readline())
# # readlines() 读取所有行返回列表
# print(f.readlines())
#
# f.close()

# # os.rename("源文件名","目标文件名")重命名
# os.rename("test.txt", "test1.txt")
# # os.remove("目标为件")删除文件
# os.remove("test1.txt")
# # os.mkdir("dir name") make dir
# os.mkdir("test")
#获取当前目录
print(os.getcwd())
# os.chdir("dir name") 切换到指定目录
# os.listdir()获取文件夹下所有文件，返回列表，默认为当前目录
print(os.listdir())