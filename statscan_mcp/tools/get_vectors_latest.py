from typing import List
from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_vectors_latest(vector_ids: List[int], latest_n: int) -> dict:
    """
    Get latest N periods of data for multiple Statistics Canada vectors.

    Fetches the most recent data points for one or more vectors in a single request.

    :param vector_ids: List of vector ID numbers (e.g., [32164132, 41690973])
    :param latest_n: Number of latest periods to retrieve (must be > 0)
    :return: Dictionary with vector data or error details
    """
    request_body = [{"vectorId": vid, "latestN": latest_n} for vid in vector_ids]
    return await client.post("getDataFromVectorsAndLatestNPeriods", request_body)
