from openai._base_client import Transport
import rnet  # hypothetical Rust-backed HTTP client

class RNetTransport(Transport):
    """
    Rust-backed HTTP transport using rnet.
    """
    def __init__(self, **kwargs):
        self._client = rnet.Client(**kwargs)

    async def request(self, method, url, headers=None, data=None, stream=False):
        response = await self._client.request(
            method=method, url=url, headers=headers, body=data, stream=stream
        )
        return {
            "status": response.status,
            "headers": response.headers,
            "body": await response.text()
        }
if kwargs.get("http_client") == "rnet":
    self._transport = RNetTransport(**kwargs.get("http_client_options", {}))
else:
    self._transport = DefaultTransport(**kwargs.get("http_client_options", {}))
#from openai import OpenAI
client = OpenAI(http_client="rnet", http_client_options={"timeout": 30})
