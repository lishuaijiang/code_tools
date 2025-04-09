import importlib
import os
from plugins_notifier.plugins import NotifierBase


def load_plugins(*args, **kwargs):
    plugins = []
    plugins_folder = kwargs.get("plugins_folder", "plugins")
    socketio = kwargs.get("socketio", None)
    plugins_folder_path = os.path.join(os.path.dirname(__file__), plugins_folder)
    for filename in os.listdir(plugins_folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{plugins_folder}.{filename[:-3]}"
            mod = importlib.import_module(module_name)

            for attr in dir(mod):
                obj = getattr(mod, attr)
                if isinstance(obj, type) and issubclass(obj, NotifierBase) and obj is not NotifierBase:
                    if obj.name == "WebSocket":
                        plugins.append(obj(socketio))
                    else:
                        plugins.append(obj())
    return plugins


if __name__ == "__main__":
    print(load_plugins())
