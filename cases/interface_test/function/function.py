import yaml
import logging
import base64
import os

class Function:
    @staticmethod
    def read_extract_yaml(key: str, index=None) -> str:
        with open("./extract.yaml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            if yaml_data is None:
                logging.error("extract.yaml is empty")
                return None
                
            if key not in yaml_data:
                logging.error(f"Key '{key}' not found in extract.yaml")
                return None
                
            value = yaml_data[key]
            if isinstance(value, list):
                if index is None:
                    # 如果是数组且没有指定索引，返回YAML格式的数组字符串
                    return yaml.dump(value, default_flow_style=True)
                # 如果指定了索引，返回特定索引的值
                return str(value[int(index)]) if len(value) > int(index) else None
            # 如果不是数组，直接返回值
            return str(value)
        
    @staticmethod
    def base64_file(file_path: str) -> str:
        try:
            # 获取当前工作目录的绝对路径
            abs_path = os.path.abspath(file_path)
            with open(abs_path, 'rb') as f:
                # 读取文件内容并转换为base64
                file_content = f.read()
                base64_content = base64.b64encode(file_content).decode('utf-8')
                return base64_content
        except Exception as e:
            logging.error(f"文件转base64失败: {str(e)}")
            return None
# if __name__ == '__main__':
#     print(Function.read_extract_yaml('task_id'))