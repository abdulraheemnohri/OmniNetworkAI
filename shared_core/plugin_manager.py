import os
import importlib.util

class PluginManager:
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = {}
        if not os.path.exists(self.plugin_dir):
            os.makedirs(self.plugin_dir)

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                plugin_name = filename[:-3]
                file_path = os.path.join(self.plugin_dir, filename)
                spec = importlib.util.spec_from_file_location(plugin_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.plugins[plugin_name] = module
                print(f"🧩 Plugin Loaded: {plugin_name}")

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            return self.plugins[name].run(*args, **kwargs)
        return f"Plugin {name} not found"

    def list_plugins(self):
        return list(self.plugins.keys())
