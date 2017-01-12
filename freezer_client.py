from rally.common import logging
from rally import osclients
from rally import exceptions

LOG = logging.getLogger(__name__)


@osclients.configure("freezer", default_version="4")
class Freezer(osclients.OSClient):
    @classmethod
    def validate_version(cls, version):
        from novaclient import api_versions
        from novaclient import exceptions as nova_exc

        try:
            api_versions.get_api_version(version)
        except nova_exc.UnsupportedVersion:
            raise exceptions.RallyException(
                "Version string '%s' is unsupported." % version)

    def create_client(self, version=None, service_type=None):
        """Return nova client."""
        from novaclient import client as nova

        client = nova.Client(
            session=self.keystone.get_session()[0],
            version=self.choose_version(version),
            endpoint_override=self._get_endpoint(service_type))
        return client
