### requests使用的几种方式

```python
import requests

params={
    "name": "wxr",
    "age": "29"
}
datas = {
    "uploads": open("./test.yaml","rb")
}
datas_multi= {
    "uploads": open("./test.yaml","rb"),
    "uploads": ("test.png", "<file content>","image/png")
}
headers = {
    "Accept": "application/json, text/javascript",
    "X-Requested-With": "XMLHttpRequest"
}
#传参数
requests.get(url="www.baidu.com",params=params)
#传表单参数
requests.get(url="www.baidu.com",data=params)
#传json数据
requests.get(url="www.baidu.com",json=params)
#传文件
requests.get(url="www.baidu.com",files=datas)
#传多个文件
requests.get(url="www.baidu.com",files=datas_multi,headers=headers,verify=False)

requests.request()
```