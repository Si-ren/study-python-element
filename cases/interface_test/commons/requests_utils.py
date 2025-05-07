import logging
import time
import pytest
import requests
import os
import json
from commons.assert_utils import AssertUtils
from commons.utils import verify_yaml, ExtractUtils

eu = ExtractUtils()


class RequestsUtils(object):
    sess = requests.Session()

    def send_request(self, http_request):
        name = http_request["name"]
        url = http_request.get("request").get("url")
        method = http_request.get("request").get("method")
        headers = http_request.get("request").get("headers")
        json_data = http_request.get("request").get("json")
        params = http_request.get("request").get("params")
        show_response = http_request.get("show_response", True)  # 新增参数，默认为True
        
        files_data = {}
        logging.info(f"请求url: {url} \n 请求method: {method} \n 请求headers: {headers} \n 请求params: {params} \n 请求json: {json_data}")

        if "files" in http_request["request"]:
            if headers and "Content-Type" in headers:
                del headers["Content-Type"]
                
            for field_name, file_info in http_request["request"]["files"].items():
                try:
                    files_data[field_name] = (
                        os.path.basename(file_info["path"]),
                        open(file_info["path"], 'rb'),
                        file_info.get("type", "application/octet-stream")
                    )
                except Exception as e:
                    logging.error(str(e) + " 文件路径错误")
                    
        logging.info("start time ...")
        if not files_data:
            files_data = None
            
        resp = self.sess.request(method=method, url=url, headers=headers, 
                               params=params,  
                               files=files_data, json=json_data)
        
        # 根据show_response参数决定是否打印响应体
        if show_response:
            if "json" in resp.headers.get("Content-Type",""):
                logging.info(resp.json())
            else:
                logging.info(resp.text)
        return resp

    def start_standard_process(self, http_request):
        verify_yaml(http_request)
        new_http_request = eu.use_extract_value(http_request)
        # logging.info(f"请求为: {new_http_request}")
        retry_count = 0
        max_retries = http_request.get("retry", 1)
        retry_interval = http_request.get("retry_interval", 1)
        fail_fast = http_request.get("fail_fast", False)   
        while retry_count <= max_retries:
            try:
                resp = self.send_request(http_request=new_http_request)
                
                if "extract" in new_http_request:
                    for key, value in http_request["extract"].items():
                        eu.extract(resp, key, *value)
                
                if "validate" in new_http_request:
                    for assert_type, value in http_request["validate"].items():
                        AssertUtils().assert_all_case(resp, assert_type, value)
                    break
                else:
                    print("此用例无断言。")
                    break
            except AssertionError as e:
                retry_count += 1
                if retry_count > max_retries:
                    error_msg = f"用例 {http_request['name']} 执行失败，重试 {max_retries} 次后仍然失败"
                    logging.error(error_msg)
                    logging.error(f"失败原因: {str(e)}")
                    if fail_fast:
                        pytest.exit(error_msg, returncode=1)
                    else:
                        logging.warning("继续执行后续用例")
                        break
                logging.warning(f"断言失败，等待 {retry_interval} 秒后进行第 {retry_count} 次重试")
                time.sleep(retry_interval)  # 添加重试间隔
