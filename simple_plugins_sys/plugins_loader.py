import importlib
import os
from simple_plugins_sys.plugins import PluginBase


def load_plugins(plugins_folder="plugins"):
    plugins = []
    plugins_folder_path = os.path.join(os.path.dirname(__file__), plugins_folder)
    for filename in os.listdir(plugins_folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{plugins_folder}.{filename[:-3]}"
            mod = importlib.import_module(module_name)

            for attr in dir(mod):
                obj = getattr(mod, attr)
                # 过滤出 HelloPlugin 和 GoodbyePlugin
                if isinstance(obj, type) and issubclass(obj, PluginBase) and obj is not PluginBase:
                    plugins.append(obj())
    return plugins


if __name__ == "__main__":
    print(load_plugins())
