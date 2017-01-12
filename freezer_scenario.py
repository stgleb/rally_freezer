from rally import osclients
from rally.plugins.openstack.scenarios.nova import utils as nova_utils
from rally.plugins.openstack.scenarios.cinder import utils as cinder_utils
from rally.task import atomic


@osclients.configure(name="BackupServers")
class BackupServers(nova_utils.NovaScenario, cinder_utils.CinderScenario):
    """Base class for Freezer scenarios with basic atomic actions."""
    def run(self, **kwargs):
        server_id = self.context[...]
        with atomic.ActionTimer(self, "backup_server"):
            backup = self.clients("freezer").backup_server(server_id)


@osclients.configure(name="BackupServers")
class BackupVolumes(cinder_utils.CinderScenario):
    """Base class for Freezer scenarios with basic atomic actions."""
    def run(self, **kwargs):
        server_id = self.context[...]
        with atomic.ActionTimer(self, "backup_server"):
            backup = self.clients("freezer").backup_server(server_id)
