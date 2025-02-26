import yaml
import logging


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
        

# if __name__ == '__main__':
#     print(Function.read_extract_yaml('task_id'))