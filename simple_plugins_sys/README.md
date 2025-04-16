## 运行/调试说明
目的：将`code_tools`添加到 Python 的 `sys.path` 中

方式一（推荐）：运行指定项目之前手动将`PYTHONPATH`导入到环境变量中
```
export PYTHONPATH="/absolute/path/of/your/code_tools:$PYTHONPATH"
```
```
python3 simple_plugins_sys/main.py
```

方式二：在需要运行/调试的目标文件内容最顶部添加如下代码
```python
import os
import sys

# 添加项目根目录（code_tools）到 sys.path，os.pardir 表示上级目录（..）
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
```
```
python3 simple_plugins_sys/main.py
```
