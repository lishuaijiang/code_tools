from simple_plugins_sys.plugins_loader import load_plugins


if __name__ == "__main__":
    plugins = load_plugins()
    print(f"🔌 Loaded {len(plugins)} plugins: {plugins}")
    for plugin in plugins:
        plugin.run()
