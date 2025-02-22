import logging
import time
import pytest
import requests

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
        # print(name + url + method + str(headers))
        files_data = {}
        if "files" in http_request["request"]:
            for file_name in http_request["request"]["files"]:
                try:
                    files_data[file_name] = open(file_name, 'rb')
                except Exception as e:
                    logging.error(e+" 文件路径错误")
        logging.info("start time ...")
        resp = self.sess.request(method=method, url=url, headers=headers, files=files_data)
        # print(resp.headers)
        if "json" in resp.headers.get("Content-Type",""):
            logging.info(resp.json())
        else:
            logging.info(resp.text)
        return resp

    def start_standard_process(self, http_request):
        verify_yaml(http_request)
        new_http_request = eu.use_extract_value(http_request)
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
