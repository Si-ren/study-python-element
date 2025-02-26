from pathlib import Path

import pytest
import test_all_case

if __name__ == '__main__':
    with open("extract.yaml", "w", encoding="utf-8") as f:
        f.write("")
    pytest.main([])