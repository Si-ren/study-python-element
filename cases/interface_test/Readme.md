# 使用说明
```shell
#打包镜像
docker build -t interface_test:py3.11 .

#运行容器
docker run -it -v ${PWD}:/app interface_test:py3.11 bash

#执行命令
python ./main.py -p ./cases/hetong
```

# 测试用例配置文件详解
```yaml
- name: "获取解析结果 API"   #用例名称
  retry: 3   #重试次数，比如异步接口需要等结果返回后继续
  retry_interval: 15 # 失败后等待2秒再重试
  fail_fast: false   # 是否失败立马退出
  request:  #请求配置
    url: http://192.168.28.118:35888/api/contracts/v3/parser/external/result  #请求接口
    method: POST  #http方法
    headers:  #请求头
      Content-Type: application/json
    json:  #data
      task_id: "${read_extract_yaml(task_id,0)}"  #函数在function.py配置，需要用${}配置起来
  extract:  #从返回中提取的数据，输出到extract.yaml中
    PageStrID: [text, "$.data.parse_result.pages[0].PageStrID", 0] 
  validate:  #验证请求是否成功
    equals:  
      status_code: 200  #http返回值
      "$.code": 200  #从响应体中获取值，jsonpath
      "$.msg": "success" #从响应体中获取值，jsonpath
```