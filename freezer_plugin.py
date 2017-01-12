from rally.common.plugin import plugin
from rally.task import scenario


@scenario.configure(name="my_new_plugin_name")
class MyNewPlugin(plugin.Plugin):
    pass
