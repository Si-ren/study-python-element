import yaml


class Function:

    @staticmethod
    def read_yaml(key: str) -> str:
        with open("./extract.yaml", encoding="utf-8") as f:
            return yaml.safe_load(f)[key]

