from typing import List
from django.apps import AppConfig
import pkg_resources


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    parse_plugins = []
    render_plugins = []

    def ready(self):
        print(f"{self.name}::ready()")

        self.parse_plugins = load_plugins('kenigsberg.parse')
        self.render_plugins = load_plugins('kenigsberg.render')

        print(f"parse_plugins={self.parse_plugins}, render_plugins={self.render_plugins}")


def load_plugins(plugin_group: str) -> List:
    """Dynamically load plugins of the given group of plugins.

    Args:
        plugin_group (str): Name of the plugin group.
        This is defined as the entry point in each of
        the plugins' setup.py (e.g. 'kenigsberg.parse')

    Returns:
        List: List of plugins installed under this group.
    """

    print(f"Loading plugins [group = {plugin_group}]")

    plugins = []
    for ep in pkg_resources.iter_entry_points(group=plugin_group):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)

    print(f"Loaded plugins: {plugins}")
    return plugins