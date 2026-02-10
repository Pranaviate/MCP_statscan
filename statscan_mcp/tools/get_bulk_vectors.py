from typing import List
from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_bulk_vectors(
    vector_ids: List[int],
    start_release_date: str,
    end_release_date: str
) -> dict:
    """
    Get bulk vector data by release date range for multiple Statistics Canada vectors.

    Fetches data for multiple vectors based on when the data points were released.

    :param vector_ids: List of vector ID numbers (e.g., [74804, 1])
    :param start_release_date: Start datetime in ISO format (e.g., "2015-12-01T08:30")
    :param end_release_date: End datetime in ISO format (e.g., "2018-03-31T19:00")
    :return: Dictionary with bulk vector data or error details
    """
    request_body = {
        "vectorIds": [str(vid) for vid in vector_ids],
        "startDataPointReleaseDate": start_release_date,
        "endDataPointReleaseDate": end_release_date
    }
    return await client.post("getBulkVectorDataByRange", request_body)
