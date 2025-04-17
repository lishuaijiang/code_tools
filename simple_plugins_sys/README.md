## 运行/调试说明
**1. 修改环境变量**  
目的：将`code_tools`添加到 Python 的`sys.path`中，避免使用从`simple_plugins_sys`开始导包报错
```
Traceback (most recent call last):
  File "/Users/xxx/Desktop/code_tools/simple_plugins_sys/main.py", line 16, in <module>
    from simple_plugins_sys.plugins_loader import load_plugins
ModuleNotFoundError: No module named 'simple_plugins_sys'
```

方式一（推荐）：在需要运行/调试的目标**文件最顶部**添加如下代码
```python
import os
import sys


def _add_root_path():
    # 添加项目根目录（code_tools）到 sys.path，os.pardir 表示上级目录（..）
    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)


# 在导入其他模块前执行
_add_root_path()
```

方式二：运行指定项目之前手动将`PYTHONPATH`导入到环境变量中  
**注意：是`code_tools`的绝对路径不是子项目的路径**
```
export PYTHONPATH="/absolute/path/of/your/code_tools:$PYTHONPATH"
```

**2. 运行**（进入项目目录中运行）
```
cd simple_plugins_sys/
python3 main.py
```
