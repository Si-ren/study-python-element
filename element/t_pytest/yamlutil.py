import yaml
class YamlUtil(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        读取yaml
        :return:
        """
        with open(self.yaml_file, 'r',encoding="utf-8") as f:
            values = yaml.load(f, Loader=yaml.FullLoader)
            return values


# if __name__ == '__main__':
#     YamlUtil('test.yaml').read_file()