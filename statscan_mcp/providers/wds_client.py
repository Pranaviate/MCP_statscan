import httpx
from typing import Optional


class WDSClient:
    BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

    def __init__(self):
        self.client = httpx.AsyncClient()

    async def _request(self, method: str, endpoint: str, params: Optional[dict] = None, body=None) -> dict:
        try:
            response = await self.client.request(
                method,
                f"{self.BASE_URL}/{endpoint}",
                params=params,
                json=body
            )
            return response.json()
        except Exception as e:
            return {
                "error": str(e),
                "hint": f"Failed to fetch {endpoint} from StatsCan API"
            }

    async def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        return await self._request("GET", endpoint, params=params)

    async def post(self, endpoint: str, body) -> dict:
        return await self._request("POST", endpoint, body=body)


