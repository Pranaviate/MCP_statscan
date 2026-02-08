import httpx
from typing import List

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_vectors_latest(vector_ids: List[int], latest_n: int) -> dict:
    """
    Get latest N periods of data for multiple Statistics Canada vectors.

    Fetches the most recent data points for one or more vectors in a single request.

    :param vector_ids: List of vector ID numbers (e.g., [32164132, 41690973])
    :param latest_n: Number of latest periods to retrieve (must be > 0)
    :return: Dictionary with vector data or error details
    """
    try:
        # Build request body - array of objects, each with vectorId and latestN
        request_body = [{"vectorId": vid, "latestN": latest_n} for vid in vector_ids]

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/getDataFromVectorsAndLatestNPeriods",
                json=request_body
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch vectors latest data from StatsCan API"
        }
