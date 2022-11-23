from common.services.base import Client

class RdapClient(Client):
    """ Rdap client, in charge of doing the respective requests
    into the rdap servers to gather information about the domains. """

    def __init__(self, headers: dict = None, timeout=10) -> None:
        super().__init__(headers, timeout)
        self._renew_dns_file()
    
    def _renew_dns_file(self):
        """ Renew the DNS json file where
        the API knows where to get the domain name servers hosts. """