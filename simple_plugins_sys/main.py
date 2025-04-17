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

from simple_plugins_sys.plugins_loader import load_plugins

if __name__ == "__main__":
    plugins = load_plugins()
    print(f"🔌 Loaded {len(plugins)} plugins: {plugins}")
    for plugin in plugins:
        plugin.run()
