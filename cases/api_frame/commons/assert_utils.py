import copy

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

    def assert_all_case(self, resp, assert_type, value):
        new_resp = copy.deepcopy(resp)
        try:
            new_resp.json = new_resp.content.json()
            # print(new_resp.json)
        except Exception:
            new_resp.json = {"msg": "response not json data"}
        for assert_content, expected_value in value.items():
            get_value = getattr(new_resp, assert_content)
            print(assert_type + " " + assert_content + " " + str(expected_value) + " " + str(get_value))
            match assert_type:
                case "equals":
                    assert get_value == expected_value
                # case "contains":
                #     assert expected_value in get_value
                # case "db_contains":
                #     # TODO 这里不准确
                #     get_value = self.execute_sql(assert_type)
                #     assert expected_value in get_value
