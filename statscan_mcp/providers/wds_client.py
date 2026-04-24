import logging
import time

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential, before_sleep_log
from typing import Optional

from statscan_mcp.config import settings

logger = logging.getLogger(__name__)


class WDSClient:
    BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(
                connect=settings.timeout_connect,
                read=settings.timeout_read,
                write=settings.timeout_write,
                pool=settings.timeout_pool,
            )
        )
        self._fetch = retry(
            stop=stop_after_attempt(settings.retry_attempts),
            wait=wait_exponential(min=settings.retry_min_wait, max=settings.retry_max_wait),
            retry=retry_if_exception_type((httpx.TimeoutException, httpx.NetworkError)),
            before_sleep=before_sleep_log(logger, logging.WARNING),
            reraise=True,
        )(self._do_fetch)

    async def _do_fetch(self, method: str, url: str, params: Optional[dict], body) -> httpx.Response:
        return await self.client.request(method, url, params=params, json=body)

    async def _request(self, method: str, endpoint: str, params: Optional[dict] = None, body=None) -> dict:
        url = f"{self.BASE_URL}/{endpoint}"
        logger.info("%s %s", method, url)
        start = time.monotonic()
        try:
            response = await self._fetch(method, url, params, body)
            duration = time.monotonic() - start
            logger.info("%s %s → %d (%.2fs)", method, endpoint, response.status_code, duration)
            return response.json()
        except Exception as e:
            duration = time.monotonic() - start
            logger.error("%s %s failed after %.2fs: %s", method, endpoint, duration, e)
            return {
                "error": str(e),
                "hint": f"Failed to fetch {endpoint} from StatsCan API"
            }

    async def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        return await self._request("GET", endpoint, params=params)

    async def post(self, endpoint: str, body) -> dict:
        return await self._request("POST", endpoint, body=body)


