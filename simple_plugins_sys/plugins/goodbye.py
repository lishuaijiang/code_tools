from simple_plugins_sys.plugins import PluginBase


class GoodbyePlugin(PluginBase):
    def run(self):
        print("👋 Run from GoodbyePlugin")
