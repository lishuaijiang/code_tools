## 运行/调试说明
**1. 创建独立虚拟环境并安装依赖库**
```bash
cd code_tools/
python3 -m venv plugins_notifier/venv/
source plugins_notifier/venv/bin/activate
python3 -m pip install -r plugins_notifier/requirements.txt
```

**2. 修改环境变量**  
目的：将`code_tools`添加到 Python 的 `sys.path` 中

方式一（推荐）：运行指定项目之前手动将`PYTHONPATH`导入到环境变量中  
**注意：是`code_tools`的绝对路径不是子项目的路径**
```
export PYTHONPATH="/absolute/path/of/your/code_tools:$PYTHONPATH"
```
```
python3 plugins_notifier/main.py
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
python3 plugins_notifier/main.py
```
