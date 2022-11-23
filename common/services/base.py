import requests

from common.exceptions import (
    ClientConnectionError,
    ClientHttpException,
    ClientRequestException,
    ClientTimeoutException,
    UnhandledErrorException,
)

BASE_HEADERS = {
    "Accept" : "application/json",
    "content-type" : "application/json",
}


class Client:
    
    def __init__(self, headers:dict=None, timeout=10) -> None:
        self.headers = headers if headers is not None else BASE_HEADERS
        self.timeout = timeout
        self.client = requests.Session()

    def get(self, url:str):
        """ Send a GET request """

        try:
            response = self.client.get(
                url=url,
                headers=self.headers,
            )
            return response.text
        except requests.exceptions.HTTPError as exc:
            raise ClientHttpException(f" - HTTP error: {exc}") from exc
        except requests.exceptions.ConnectionError as exc:
            raise ClientConnectionError(f" - Connection error: {exc}") from exc
        except requests.exceptions.Timeout as exc:
            raise ClientTimeoutException(f" - Timeout error: {exc}") from exc
        except requests.exceptions.RequestException as exc:
            raise ClientRequestException(f" - Request error: {exc}") from exc
        except Exception as exc:
            raise UnhandledErrorException(f" - Unhandled error: {exc}") from exc