from simple_plugins_sys.plugins import PluginBase


class HelloPlugin(PluginBase):
    def run(self):
        print("👋 Run from HelloPlugin")
