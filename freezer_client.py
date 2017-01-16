import freezerclient.v1.client as freezer_client

from rally.common import logging
from rally import osclients

LOG = logging.getLogger(__name__)


@osclients.configure("freezer", default_version="4")
class Freezer(osclients.OSClient):
    def create_client(self, version=None, service_type=None):
        """Return freezer client."""
        client = freezer_client.Client(self.choose_version(version),
                                       session=self.keystone.get_session()[0],
                                       endpoint=self._get_endpoint
                                       (service_type))
        return client
