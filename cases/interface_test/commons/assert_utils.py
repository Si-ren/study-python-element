import copy
import jsonpath
import pymysql


class AssertUtils(object):
    def __init__(self):
        self.conn = None

    def conn_database(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='<PASSWORD>',
        )

        return self.conn

    def execute_sql(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        values = cursor.fetchall()
        cursor.close()
        return values

    @staticmethod
    def assert_all_case(resp, assert_type, value):
        new_resp = copy.deepcopy(resp)
        try:
            new_resp.json = new_resp.json()  # 直接使用 resp.json()
        except Exception:
            new_resp.json = {"msg": "response not json data"}
            
        for assert_content, expected_value in value.items():
            if assert_content.startswith("$."):
                # 处理 JSON 路径断言
                actual_value = jsonpath.jsonpath(new_resp.json, assert_content)
                if actual_value:
                    get_value = actual_value[0]
                else:
                    raise AssertionError(f"JSON path {assert_content} not found in response")
            else:
                # 处理原有的响应属性断言
                get_value = getattr(new_resp, assert_content)
                
            print(f"{assert_type} {assert_content} expected: {expected_value}, actual: {get_value}")
            
            match assert_type:
                case "equals":
                    assert get_value == expected_value
                case "contains":
                    assert expected_value in get_value
                # case "db_contains":
                #     # TODO 这里不准确
                #     get_value = self.execute_sql(assert_type)
                #     assert expected_value in get_value
