from rally import osclients
from rally.plugins.openstack.scenarios.nova import utils as nova_utils
from rally.plugins.openstack.scenarios.cinder import utils as cinder_utils
from rally.task import atomic


@osclients.configure(name="BackupServers")
class BackupServers(nova_utils.NovaScenario, cinder_utils.CinderScenario):
    """Base class for Freezer scenarios with basic atomic actions."""
    def run(self, **kwargs):
        iteration_count = self.context["iteration_count"]
        step = self.context["step"]
        server_base_name = self.context["base_name"]
        user, tenant_id = self.context["users"]
        servers = self.context["tenants"][tenant_id]["servers"]

        for i in range(iteration_count):
            with atomic.ActionTimer(self, "backup_nova"):
                for j in range(step):
                    index = i * step + j
                    self.clients("freezer").\
                        backup_nova("{0}+_{1}".format(server_base_name,
                                                      servers[index].name))


@osclients.configure(name="BackupServers")
class BackupVolumes(cinder_utils.CinderScenario):
    """Base class for Freezer scenarios with basic atomic actions."""
    def run(self, **kwargs):
        iteration_count = self.context["iteration_count"]
        step = self.context["step"]
        server_base_name = self.context["base_name"]

        for i in range(iteration_count):
            with atomic.ActionTimer(self, "backup_cinder"):
                for j in range(step):
                    self.clients("freezer").\
                        backup_cinder("{0}+_{1}".format(server_base_name,
                                                        i * step + j))
